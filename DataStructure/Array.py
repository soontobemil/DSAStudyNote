# strings = ['a','b']

# strings.append('e') # O(1) Operation, we are not looping through anything.
# strings.pop() # O(1)
# strings.insert(0, 'start') # O(n)

# print(strings)

class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def get_method(self, index):
        return self.data.get(index, None)

    def push_method(self, item):
        self.data[self.length] = item
        self.length +=1
        return self.length

    def pop_method(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -=1
        return last_item

    def delete_method(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -=1

newArray = MyArray()
newArray.push_method('Hi')
newArray.push_method('Hi, Again')
newArray.push_method('Pop this huh')
newArray.delete_method(2)

print(f"Length is {newArray.length}, {newArray.data}")
