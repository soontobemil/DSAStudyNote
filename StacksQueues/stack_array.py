class StackArray():
    def __init__(self):
        self.stack = []

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

