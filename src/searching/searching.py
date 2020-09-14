def linear_search(arr, target):
    # Your code here

    # for each item in array
    for i in range(len(arr)):
        # if value at current index = target 
        if arr[i] == target:
        # return index
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here

    # length // 2
    left = 0
    right = len(arr) - 1

    # keep iterating as long as left <= right
    while left <= right:    
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint
        
        elif arr[midpoint] > target:
            # toss out the left side of array
            # toss out midpoint since we know it's not the target
            right = midpoint - 1
        else: 
            left = midpoint + 1

        # if we didn't find what we're looking for
    return -1  # not found
