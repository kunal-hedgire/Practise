
def bubble(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

print(bubble([5, 1, 4, 2, 8]))
