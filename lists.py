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
        #paul is here. 
    print

def reverse_list1(node):
	if(node is None or node.next is None):
		return node
	retval = reverse_list(node.next)
	node.next.next = node
	node.next = None
	return retval

def reverse_list2(node):
	cur = node.next
	prev = node
	prev.next = None
	while cur:
		nex = cur.next
		cur.next = prev
		prev = cur
		cur = nex
	return prev
## o hi yo~
array = [1, 2, 3, 4 ,5]
node = create_list(array)
print_list(node)
reverse = reverse_list2(node)
print_list(reverse)
