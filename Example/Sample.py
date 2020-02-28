# def last2(str):
#     # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     print(last2)
#     count = 0
#
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#
#     return count
#
# a = last2("hixxhi")
# print(a)

# stud = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41],
#         ['Harsh', 39]]
# l1 = []
# l2 = []
# for i, j in sorted(stud):
#     # l1.append(i)
#     l2.append(j)
#
# for k in l2:
#     print(k)

# def func():
#     # a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
#     #    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#     #    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
#     #    59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
#     #     79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
#     #    98, 99]
#     a = [7, 3, 2, 1, 4, 6, 8, 9, 10, 11, 0]
#
#     k = 9
#     sum = len(a)
#     s = set()
#
#     for i in range(0,sum):
#         temp = k - a[i]
#         if temp in s:
#             print("pair is"+str(sum)+"is (" + str(a[i]) + " ," + str(temp)+")")
#         s.add(a[i])
#
#
#
#     # for i in range(len(a)-1):
#     #     for j in range(i+1,len(a)-1):
#     #         if a[i] + a[j] == k:
#     #             print(a[i], a[j])
#     #             j += 1
#
# import time
# # start_time = time.clock()
# func()
# # print (time.clock() - start_time, "seconds")

# str = [1, 2, 3, 4, 5, 6]
# result = 0
# for i in range():
#     print(i)
#     # result = result + str[:i+1]

# a = "Hello"
# b = "xyz"
#
# print(a[2:])

# if len(a) < len(b):
#     print(a+b+a)
# else:
#     print(b+a+b)

# short = min(len(a),len(b))
# count = 0
# for i in range(short - 1):
#     sub_a = a[i:i+2]
#     sub_b = b[i:i+2]
#     if sub_a == sub_b:
#         count += 1
# print(count)


# print(a[0:len(a)//2])

# print(a[1:-2])


class A:
    def class_a(self):
        print("In Class A")


class B:
    def class_b(self):
        print("In Class B")


class C(A,B):
    print("in class C")



c1 = C()
c1.class_a()

def A():
#     list1 = [1, 2, 3, 1]
#
#     if list1[0] == list1[len(list1) - 1]:
#         return True
#     return False
#
# print(A())

    l = [1, 1]
    if len(l) == 0:
        return 0
    elif len(l) <= 2:
        return l[0] + l[1]
    elif len(l) > 2:
        return l[0] + l[1]

print(A())






# print(l[1:] + l[:1])
# print(l[::-1])
# l1 = []
# for i in l:
#     l1.insert(0,i)
# print(l1)





