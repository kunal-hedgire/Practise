def missing_char(str, n):
    front = str[:n]
    print(front)
    end = str[n+1:]
    print(end)
    return front + end


a = missing_char("kunal", 2)
print(a)



