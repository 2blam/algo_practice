# quicksort - in place version

def quicksort(arr, start_idx, end_idx):
    if start_idx < end_idx:
        partition_idx = partition(arr, start_idx, end_idx)
        quicksort(arr, start_idx, partition_idx-1) #sort the smaller partition (again)
        quicksort(arr, partition_idx+1, end_idx)   #sort the larger partition (again)

# partition
def partition(arr, start_idx, end_idx):
    pivot = arr[end_idx] #last element as pivot
    i = start_idx - 1
    for j in range(start_idx, end_idx): #note: end_idx (exclusive)
        if arr[j] <= pivot: 
            i = i + 1 # grow the smaller parition
            arr[i], arr[j] = arr[j], arr[i] #swap
    
    #swap pivot element, i.e. lies between 2 partitions        
    arr[i+1], arr[end_idx] = arr[end_idx], arr[i+1]
    return i+1

ar = [3, 5, 4, 6, 12, 8, 2, 1]
quicksort(ar,0,len(ar)-1)
print(*ar) 