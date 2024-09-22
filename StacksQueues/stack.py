class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1
        return self


    def pop (self):
        if self.top is None:
            return None

        if self.top == self.bottom:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1
        return


    def isEmpty():
        return 1

    def print_stack(self):
        current = self.top
        items = []
        while current:
            items.append(current.value)
            current = current.next
        print(f"Stack: {items}, Length: {self.length}, Top: {self.top.value if self.top else None}, Bottom: {self.bottom.value if self.bottom else None}")


myStack = Stack()
myStack.push("Google")
myStack.push("Udemy")
myStack.pop()
myStack.pop()
myStack.print_stack()
