class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
         This function init all default variable for the class
        """
        self.head = None

    def isEmpty(self):
        """
        check if the LinkedList is empty. Returns a boolean value
        :return: boolean
        """
        if self.head is None:
            return True
        else:
            return False

    def addFirst(self, value):
        """
        Add an element at the head of the Linked List.
        :return: int (value at head)
        """
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        # return self.head.value

    def addLast(self, value):
        """
        Add an element to the tail of the Linked list
        :return: None
        """
        newNode = Node(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        # return self.head.value

    def addAtPosition(self, position, value):
        """
        Add an element to a given position of the linked list, The new node will be added at the position.
        :return: None
        """
        i = 1
        newNode = Node(value)
        temp = self.head
        try:
            while i < position:
                if temp is None:
                    raise ValueError
                else:
                    temp = temp.next
                i = i + 1
            newNode.next = temp.next
            temp.next = newNode
        except ValueError:
            print("Out of bounds")

    def removeAtPosition(self, position):
        """
        Remove an element from specified position
        :return: None
        """
        temp = self.head
        trav = self.head.next
        i = 0
        if position == 0:
            self.head = temp.next
            return
        while i < position-1:
            if trav.next is None:
                raise ValueError
            else:
                temp = trav
                trav = trav.next
            i = i + 1
        temp.next = trav.next
        trav.next = None

    def findValueAtPosition(self, position):
        """
        Find the value at given position in List.
        :return: int
        """
        temp = self.head
        for i in range(position):
            if temp.next is None:
                return "Out of Bound"
            else:
                temp = temp.next
        return temp.value

    def lengthOfList(self):
        """
        Gives the length of the list.
        :return: int
        """
        pass

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

## Other methods can
# Index of
# Remove from head
# remove from Tail
# clear linked list

if __name__ == "__main__":
    sol = LinkedList()
    sol.addFirst(5)
    sol.addFirst(3)
    sol.addLast(7)
    sol.addAtPosition(1, 4)
    print("Removing node at position 2")
    sol.removeAtPosition(2)
    sol.printList()
    print("Value at position")
    print(sol.findValueAtPosition(2))

