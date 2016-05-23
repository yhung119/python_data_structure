'''

Class SinglyNode that only has 'next' element

create_singly_list: given an array return the first node of the singly linked list

create_doubly_list: given an array return the head and tail of the doubly linekd list in a tuple

print_list: given the head, print out the whole list


'''
class SinglyNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return str(self.value)

class DoublyNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.value)

def create_singly_list(array):
    node_array = []
    for value in array:
        node_array.append(SinglyNode(value))
    array_length = len(node_array)
    for i in range(0, array_length-1):
		node_array[i].next = node_array[i+1]
    node_array[array_length-1].next = None
	
    return node_array[0]

def create_doubly_list(array):
    node_array = []
    for value in array:
        node_array.append(DoublyNode(value))
    array_length = len(node_array)
    node_array[0].prev = None
    node_array[array_length-1].next = None
    for i in range(1, array_length):
        node_array[i-1].next = node_array[i]
        node_array[i].prev = node_array[i-1]
    return (node_array[0],node_array[array_length-1])

def print_list(head):
    node = head
    while node:
        print node,
        if node.next is None:
        	print 'End'
        node = node.next
    print

def test_doubly():
    array = [1, 2 ,3 ,4 ,5]
    (head, tail) = create_doubly_list(array)
    print_list(head)
    node = tail
    while node:
        print node,
        if node.prev is None:
            print 'End'
        node = node.prev
    print 
