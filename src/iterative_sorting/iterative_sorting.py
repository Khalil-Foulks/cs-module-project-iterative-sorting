# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements; each item in list
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # for each item to the right of current index 
        for j in range(cur_index + 1, len(arr)):
            # if current item is less than current smallest 
            if arr[j] < arr[smallest_index]:
                # current smallest becomes current item
                smallest_index = j
        # TO-DO: swap
        # Your code here
        # Swap the element at current index with the smallest element found in above loop
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    length = len(arr)

    # for each item in list
    for i in range(length):
        # set swap to false
        swap = False

        # for each item in list, not including the last
        for j in range(0, length - 1):
            # if item at current index is greater than next item to the right 
            if arr[j] > arr[j+1]:
                # swap the items 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # update swap to true; repeat entire process until nothing is swapped
                swap = True
        # if swap is False stop the inner loop
        if swap == False: 
                break
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
