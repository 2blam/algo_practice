# quick sort
# Best: O(n log n); Worst: O(n ^ 2); Average case: O (n log n); Space Complexity: Best - log n, Average: n

def quicksort(lst):
    if len(lst) <=1:
        return lst
    less, equal, greater = [], [], []
    # pick the first element as pivot (can use last one / random element)
    pivot = lst[0]
    
    for e in lst:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            greater.append(e)
        else:
            equal.append(e)
    less = quicksort(less)
    greater = quicksort(greater)
    return less + equal + greater            
    
print(quicksort([3, 5, 4, 6, 12, 8, 2, 1]))        
