'''
    linked-list
        - is basically a data structure for storing collection of data or items

    class Box{
    int data
    Box next
    }

    head.data
        -the data - head represents the first box
    box next
    -reflects to the next box that is connected
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if self.head  is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        
        print("None")
    
    def remove_input_value(self, value):
        if self.head == None:
            return
        
        current = self.head
        position = 0
        if position == value:
            self.remove_first_node()
        else:
            while(current != None and position+1 != value):
                position = position+1
                current = current.next

            if current != None:
                current.next = current.next.next
            else:
                print("Value not present")

    def insert_input_value(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def remove_first_node(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("List is empty")


# input values
input_values = [6,3,4,2,1]

my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

my_linked_list.remove_input_value(2)
my_linked_list.insert_input_value(4,1)
my_linked_list.display()
