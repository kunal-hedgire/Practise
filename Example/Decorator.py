def hash1(func):
    def inner(*args, **kwargs):
        print("in hash")
        print("#"*30)
        func(*args, **kwargs)
        print("#"*30)
    return inner


def percentage(func):
    def inner(*args, **kwargs):
        print("In percentage")
        print("%"*30)
        func(*args, **kwargs)
        print("%"*30)
    return inner



@percentage
@hash1
def message(msg):
    print(msg)


message("Hello")
