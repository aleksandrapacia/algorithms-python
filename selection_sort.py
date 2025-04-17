def selection_sort(arr):
    n = len(arr)
    for i  in range(n-1):
        min_idx = i  # we assume that the first eleemnt is the smallest
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i] # swapping

lista = [64,5,25,12,22,11]
selection_sort(lista)
print(lista)