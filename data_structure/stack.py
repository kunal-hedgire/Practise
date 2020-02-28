class Stack:

    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1
        self.input()

    def input(self):
        print("the stack operation are:\n"
              "1.add item to stack\n"
              "2.remove item from stack\n"
              "3.top position\n"
              "4.exit\n")
        inp = int(input("Enter your choice: "))
        if inp == 1:
            self.push_item()

        elif inp == 2:
            self.pop_item()

        elif inp == 3:
            self.peek()

        elif inp == 4:
            print("closing...")
            exit(0)

        else:
            print("wrong input!!!!! please try again!!!\n\n")
            self.input()

    def push_item(self):
        num = int(input("Enter the number: "))
        for _ in range(self.size):
            if self.is_full():
                print("can't push item to stack is overflow")
            else:
                self.stack.append(num)
                self.top += 1
            self.input()

    def pop_item(self):
        if self.is_empty():
            print("Can't pop the element stack is empty")

        else:
            print("\n element is pop:", self.stack.pop())
            self.top -= 1
        self.input()

    def peek(self):
        if self.top == -1:
            print(self.top)
        else:
            print(self.stack[self.top])

    def is_full(self):
        # return true if stack is full
        if self.top == self.size-1:
            return True

    def is_empty(self):
        # return True if stack is empty
        if self.top == -1:
            return True


size = int(input("Enter the stack size: "))
s = Stack(size)
