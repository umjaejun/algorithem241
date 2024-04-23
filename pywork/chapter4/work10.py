def kth_smallest_sort(A, k) :
    A.sort()
    return A[k-1]

list = [4, 2, 7, 1, 9, 5]
k_value = 5

print(kth_smallest_sort(list, k_value))