def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1): # repeat n-1 times
        swapped = False # optimalization flag
        for j in range(n- 1 - i): # going through unsorted array
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True # we mark that a change has been made
            if not swapped: # if there's been no change made, array has been already sorted
                break
arr = [5, 3, 2, 1]
bubble_sort(arr)
print("sorted: ", arr)
print("outcome")
print("test")
