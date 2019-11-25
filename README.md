**Infrastructure architecture described in InfrastructureArchitecture.png contains the following infrastructure:**

1. A VPC with public and private subnets to separate external and internal components spanning an AWS region.

1. Amazon S3 and Cloudfront to serve static web content UI files. I chose AWS S3 and Cloudfront to serve the files over docker containers because:

	- It&#39;s cheaper as we are not paying for constantly running server and Elastic Block Storage (EBS) volumes.
	- We don&#39;t have to worry about patching and stability of the containers.
	- It&#39;s easy to version in S3.
	- AWS Cloudfront can help reduce the latency of the service.
	- S3 is designed to store and retrieve any number of files or objects from anywhere on the internet, so it will be easier to scale UI files and objects.

1. An Application Load Balancer (ALB) that is exposed to the internet to route Inbound traffic. The load balancer also handles HTTPS termination. HTTPS termination is done by adding an HTTPS listener to the load balancer and supply the SSL certificate. The requests are forwarded to ECS service and containers from the ALB.

1. A highly available AWS Elastic Container Service (ECS) cluster deployed across multiple Availability Zones in an Auto Scaling Group to configure and launch API service. The Autoscaling group takes care of horizontally scaling API service instances. The autoscaling group can be set up to scale automatically by setting a specific scaling policy (CPU, network, time of day, etc.). By default, the auto-scaling group policy in the cloudformation template launches and maintains a cluster of 4 ECS hosts distributed across 2 Availability Zones.

1. A pair of NAT Gateways in the public subnets to handle outbound traffic from the Prometheus service ECS cluster.

2. An ECS cluster in an auto-scaling group for Prometheus monitoring instance for the reasons mentioned in point 4 as well. I have deployed different ECS clusters for API and Prometheus services in order to decouple them. Decoupling them makes it easy to deploy and maintain different services that have different workloads and scalability needs. If one service goes down it does not affect the availability of others.

1. An AWS RDS instance for the database rather than a container because:

	- It&#39;s more stable to run the database in an RDS instance rather than on docker because if docker crashes it will destroy the valuable data it holds.
	- Using RDS reduces one extra layer in the tech stack that we need to patch and update.
	- Using RDS instance will simplify a lot of management tasks like updating minor versions, handling backups and scaling.

1. An AWS Elasticache cluster to save persistent data needed by the API service. Putting a cache between API service and the database is helpful in reducing the read load from the database which may allow resources to be used for writes. Additionally, the cache will also improve latency.

2. Centralized container logging with Amazon Cloudwatch Logs. Using AWS Cloudwatch to gain system wide visibility into resource utilization, application performance and operational health. The metrics can be used to configure alarms and statistics.

The code consists of the following templates. To run the code upload all the templates below in an S3 bucket and update their S3 urls in 00-master.yaml template in the \&lt;TemplateURL\&gt; parameter. Deploy 00-master.yaml in cloudformation and it includes all other templates automatically.

00-master.yaml

01-vpc.yaml

02-SecurityGroups.yaml

03-LoadBalancer.yaml

04-route53.yaml

05-cloudfront-and-s3.yaml

06-api-ecs-cluster.yaml

07-monitoring-ecs-cluster.yaml

08-RDS.yaml

09-elasticache.yaml



**Deploying with zero downtime:**

I would achieve code deployment with zero downtime by using the Canary Release/Deployment method. In this method of code release, the Continuous Deployment pipeline is configured in such a way to release new software versions on a very small percentage of production servers called canary servers. This way it&#39;s easy to monitor how a new version of the software behaves while minimizing the impact of breaking. If the error rate returned by the canary instances is acceptable then the software is released to the whole production environment or else rolled back.

The rollback is done by redeploying the old version on the canary instances.

**Backup and Disaster Recovery(DR) Plan:**

1. We use AWS Backup service to create backup policies to create snapshots of the ebs volumes attached to instances in ECS cluster. We use it to create RDS snapshots too. The snapshots from the backup plan can be stored in S3 bucket for Disaster Recovery.
2. Duplicate UI files in S3 to a different region. This can be done by enabling cross-region replication in S3.
3. Store AWS credentials in a safe place for example LastPass.
4. Assuming the Recovery Time Objective (RTO) is ~30 minutes my DR plan would be as follows:
	  1. Maintain a read replica RDS instance in the DR region running that is replicated and kept updated from the master RDS instance.
	  2. Duplicate UI files in S3 to the DR region. This can be done by enabling cross-region replication in S3.
	  3. Have pre-configured AMIs for UI and Prometheus instances that have been baked with the configuration, software, and packages that are needed to launch the app. These AMIs can be generated by creating AMI pipelines that are regularly updated and patched.
	  4. For recovery create a cloud formation template that creates the full-scale production environment except for the RDS instance. Then the existing database in the DR region can be resized to handle increased demand/traffic. We can have all the security best practices baked in the AMI and in the cloud formation template.
	  5. In the case of a disaster change DNS to point at the DR CloudFront distribution.
	  6. Automate and test the DR procedure multiple times in a year to be ready for Disaster recovery.

**Performance metrics I would collect from the system:**

Client related metrics:

- Request duration (Average and Max Latency)- Determines what amount of time the client should wait before getting a request( the value is generally defined in Service Level Agreement (SLA)). Helpful for determining if the API is responding slower than it should.
- Request count - This metric is helpful for answering the following questions:
  - Is anyone using the API? is the API broken? (both result in request count =0)
  - Is the API under DDOS attack? (request count during last hour is much larger than the average)
- Http Response code - Is helpful for determining whether the clients are properly calling the API (no 200s), if the API has crashed (500s), was the API request successful (200s)
- Do the requests finish - This metric is helpful for determining whether the clients receive the response.

Dev related metrics:

- Memory consumption - can help developers plan for resources and measure overall health.
- IOPS - can help developers plan for resources and measure overall health.
- Uptime - This metric is helpful for determining the availability of a service.
- CPU usage- can help developers plan for resources and measure overall health.
- Errors per minute - number of API calls with non-200 HTTP response code to track how error-prone is the API.

**The following things could be improved in the architecture/things architecture needs to run in production:**

1. Create pipelines that generate ECS optimized Amazon Machine Images (AMIs) that have code baked in them and are published to either Elastic Container Registry or to an S3 bucket so it&#39;s ready to be used by the ECS Cluster.
2. Have all the packages/ libraries that are used by the app available in AWS.
3. A test and staging environment to test the infrastructure templates on.
4. Need the index.html and 404.html files from the devs to upload on S3.
5. SSL termination on the Public Load Balancer depends on the SSL Certificate. The SSL cert should be created and uploaded someplace (S3 bucket) from where the 00-master.yaml/03-Loadbalancer.yaml template can access it.
6. The template 05-cloudfront-and-S3.yaml also needs the ACM certificate are for the CloudFront distribution.
