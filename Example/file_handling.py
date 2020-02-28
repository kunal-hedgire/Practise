# import time
#
# def file_handle():
#     with open("D:/practise file csv/50000 Sales Records.csv") as file:
#         for read in file.readlines():
#             time.sleep(2)
#             yield read
#
#
# count = 0
# p = file_handle()
# for i in p:
#     # count += 1
#     print(i,"\n")
# print(count)

#  Number palindrome
# num = int(input("Enter the number:"))
# temp = num
# rev = 0
# while num > 0:
#     dig = num % 10
#     print("dig",dig)
#     rev = rev * 10 + dig
#     print("rev",rev)
#     print("before num", num)
#     num = num // 10
#     print("num",num)
#
# if temp == rev:
#     print("palindrome")
# else:
#     print("not palindrome")


# String Palindrome
# s = input("Enter the string:")
# w = ""
# for i in s:
#     w = i + w
#     print(w)
# if s == w:
#     print("true")
# else:
#     print("Flase")

# s1 = s[::-1]
# if s == s1:
#     print("palindrome")
# else:
#     print("not palindrome")



# Fabonacci number

# import math
#
# def perfect_sqrt(x):
#     s = int(math.sqrt(x))
#     return s*s == x
#
#
# def fab(n):
#     return perfect_sqrt(5*n*n+4) or perfect_sqrt(5*n*n-4)
#
#
# if fab(4) == True:
#     print("True")
# else:
#     print("False")

# Fabonacci series

# def fab_series(x):
#     n1, n2 = 0, 1
#     count = 0
#
#     if x < 0:
#         print("Wrong input..!")
#
#     elif x == 0:
#         return 0
#
#     elif x == 1:
#         return 1
#
#     else:
#         # return fab_series(x-1) + fab_series(x-2)
#         while count < x:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count +=1
#
#
# # print(fab_series(9))
# fab_series(9)





















