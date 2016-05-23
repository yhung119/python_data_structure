class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

## return head of the list
def create_list(array):
	node_array = []
	for value in array:
		node_array.append(Node(value))
	node = node_array[0]
	for i in range(0, len(node_array)-1):
		node_array[i].next = node_array[i+1]
	node_array[len(node_array)-1].next = None
	return node 

def print_list(node):
    while node:
        print node,
        if node.next is None:
        	print None
        node = node.next
    print