def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
