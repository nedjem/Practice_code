def BubbleSort(list1):
    length = len(list1)
    for n in range(length -1):
        for i in range(length -2):
            if list1[i] > list1[i + 1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list[i+1] = temp
                
def SelectionSort(list1):
    
    length = len(list1)
    
    for i in range(length-2):
        Imin = i
        for j in range(i+1,length-1):
            if list1[j] < list1[Imin]:
                Imin = j
                
        temp = list1[Imin]
        list1[Imin] = list1[j]
        list1[j] = temp

def MergeSort(listA):
    length = len(listA)
    if length < 2 :
        return 0
    left = []
    right = []
    mid = length // 2
    
    for i in range(mid - 1):
        left[i] = listA[i]
    for i in range(mid, length):
        right[i - mid] = listA[i]
        
    MergeSort(left)
    MergeSort(right)
    Merge(left,right)
    
def Merge(A,B):
    
    answer = []
    i = 0
    j = 0
    while len(A) != 0 and len(B) != 0:
        if A[i] < B[i]:
            answer.append(A[i])
            i = i + 1

        else:
            answer.append(B[j])
            j = j + 1
            
    while (i < len(answer)):
        answer = answer + A
        i = i + 1
    while (j < len(answer)):
        answer = answer + B
        j = j + 1
        
def InsertionSort(A):
    length = len(A)
    
    for i in range(1,length - 1):
        value = A[i]
        partition = i
        while( partition > 0 and A[partition - 1] > value):
            A[partition] = A[partition - 1]
            partition = partition -1
            
        A[partition] = value
        
def QuickSort(array):
    less = []
    equal = []
    greater = []
    
    
    if len(array > 1):
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
        
    else:
        return array
        
def BinarySearch(array,x,low,high):
    if low > high:
        return 0
    mid = low + high // 2
    if array[mid] < x:
        BinarySearch(array,x,mid + 1,high)
    elif array[mid] > x:
        BinarySearch(array,x,low,mid - 1)
    else:
        return mid
    