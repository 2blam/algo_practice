# bubble sort 
# Best: O(n) if the list was already sorted; Worst: O(n ^ 2); Average case: O (n ^ 2); Space Complexity: O(1) 
def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]: 
                lst[j+1], lst[j] = lst[j], lst[j+1]  #swap
    return lst

print(bubblesort([3, 5, 4, 6, 12, 8, 2, 1]))      
