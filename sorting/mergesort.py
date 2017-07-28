# merge sort
# Best: O(n log n); Worst: O(n log n); Average case: O (n log n); Space Complexity: O(n)

def merge(left, right):
    l = 0
    r = 0
    lst = []
    while (l < len(left) and r < len(right)):
        if left[l] < right[r]:
            lst.append(left[l])
            l = l + 1
        else:
            lst.append(right[r])
            r = r + 1
    #tidy
    if l < len(left): # append left remaining
        lst.extend(left[l:])
    if r < len(right): # append right remaining
        lst.extend(right[r:])
    
    return lst

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left = mergesort(lst[0:middle])
    right = mergesort(lst[middle:])
    
    return merge(left, right)

# testing
print(mergesort([3, 5, 4, 6, 12, 8, 2, 1]))
