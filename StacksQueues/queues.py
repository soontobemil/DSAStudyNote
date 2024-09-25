class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self

    def dequeue(self):
        if self.first is None:
            return None

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1
        return

    def print_stack(self):
        current = self.first
        items = []
        while current:
            items.append(current.value)
            current = current.next
        print(f"Stack: {items}, Length: {self.length}, Top: {self.first.value if self.first else None}, Bottom: {self.last.value if self.last else None}")

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(6)
myQueue.enqueue(7)
myQueue.enqueue(11)
print(myQueue.peek())
myQueue.dequeue()
myQueue.print_stack()


class MyQueue:

    def __init__(self, value):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
            self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2: # If there is nothing in stack2 array
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2: # If there is nothing in stack2 array
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return max(len(self.stack1), len(self.stack2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
