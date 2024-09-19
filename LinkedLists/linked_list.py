# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.next = None

class LinkedList():
    # Instantiate linkedlist class
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def linkedList_append(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        self.tail["next"] = new_node
        self.tail = new_node
        self.length +=1

    def linkedList_prepend(self, value):
        first_node = {
            "value": value,
            "next": None
        }
        first_node["next"] = self.head # When using class, the next attribute is a propery of the node, not a directionary key.
        self.head = first_node
        self.length +=1

    def linkedList_insert(self, index, value):
        if index >= self.length:
            return self.linkedList_append(value)

        insert_node = {
            "value": value,
            "next": None
        }

        def traverseToIndex(value):
            counter = 0
            currentNode = self.head
            while counter != index and currentNode is not None:
                currentNode = currentNode["next"]
                counter +=1
            return currentNode

        leader_node = traverseToIndex(index - 1)
        hold_pointer = leader_node["next"]
        leader_node["next"] = insert_node
        insert_node["next"] = hold_pointer
        self.length +=1
        return self.printList()


    def printList(self):
        array = []
        currentNode = self.head
        while currentNode != None:
            array.append(currentNode["value"])
            currentNode = currentNode["next"]
        return array

    def __str__(self):
        return f"LinkedList: (head={self.head}, tail={self.tail}, length={self.length})"

myLinkedList = LinkedList(10)
myLinkedList.linkedList_append(20)
myLinkedList.linkedList_append(550)
myLinkedList.linkedList_prepend(77)
myLinkedList.linkedList_insert(1, 667777)
print(myLinkedList.printList())
