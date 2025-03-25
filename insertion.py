def insertion_sort(arr):
    for i in range(1, len(arr)): # start from the second element in array
        key = arr[i] # element to insert
        j = i -1 # previous element

        # inserting elements bigger than key to the right
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j] # element arr[j] to the right (o
            # ne step)
            j -=1 # reduction of index

        arr[j+1] = key  # putting key element at right plac
arr = [7, 3, 5, 2, 8]
insertion_sort(arr)
print("sorted:", arr)