# insertion sort
# Best: O(n) if the list was already sorted; Worst: O(n ^ 2); Average case: O (n ^ 2); Space Complexity: O(1)

def insertionsort(lst):
    for i in range(1, len(lst)):
        e = lst[i] # element to be inserted
        j = i - 1  # position on the left side
        
        #back tracking, till the beginning of the lst
        while j >= 0 and e < lst[j]:
            lst[j + 1] = lst[j] # swap            
            j = j - 1           # shift to left 1 step
        
        lst[j+1] = e #insertion
    
    return lst
    

# testing
print(insertionsort([3, 5, 4, 6, 12, 8, 2, 1]))
