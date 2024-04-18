def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [7, 4, 9, 6, 3, 8, 7, 5]
selection_sort(arr)
print("정렬된 리스트:", arr)