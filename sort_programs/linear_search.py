def linear_search(A, x):
    for i in range(0,len(A)):
        if x == A[i]:
            return i
    return -1


result = linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 170)
if result == -1:
    print("element not found")

else:
    print("element found at index",result)
