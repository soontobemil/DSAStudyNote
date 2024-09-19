class DoublyLinkedList():
    def __init__(self, value):
        """Initilize the linked list with the first node."""
        self.head = {
            "value": value,
            "next": None,
            "before": None
        }
        self.tail = self.head
        self.length = 1

    def _traverse_to_index(self, index):
        counter = 0
        currentNode = self.head
        while counter != index and currentNode is not None:
            currentNode = currentNode["next"]
            counter +=1
        return currentNode

    def append(self, value):
        """Append a new node to the end of the list."""
        new_node = {
            "value": value,
            "next": None,
            "before": None
        }
        # Link the new node to the current tail
        new_node["before"] = self.tail
        self.tail["next"] = new_node
        self.tail = new_node
        self.length +=1

    def prepend(self, value):
        """Prepend a new node to the start of the list."""
        first_node = {
            "value": value,
            "next": None,
            "before": None
        }
        first_node["next"] = self.head
        self.head["before"] = first_node
        self.head = first_node
        self.length +=1

    def insert(self, index, value):
        """Insert a new node at a specific position in the list."""
        if index >= self.length:
            return self.append(value)

        insert_node = {
            "value": value,
            "next": None,
            "before": None
        }

        leader_node = self._traverse_to_index(index - 1)
        follower = leader_node["next"]
        leader_node["next"] = insert_node
        insert_node["before"] = leader_node
        insert_node["next"] = follower
        follower["before"] = insert_node
        self.length +=1
        return self.printList()

    def remove(self, index):
        """Remove a node at a specific index."""
        if index == 0:
            self.head = self.head["next"]
            self.length -=1
            return

        previous_node = self._traverse_to_index(index - 1)
        unwnated_node = previous_node["next"]
        next_node = unwnated_node["next"]

        previous_node["next"] = next_node
        next_node["before"] = previous_node

        self.length -= 1
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

myLinkedList = DoublyLinkedList(1)
myLinkedList.append(2)
myLinkedList.append(55555)
myLinkedList.insert(2,50)
print(myLinkedList.printList())
