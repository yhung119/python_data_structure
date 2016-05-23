from Node import *

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
	
array = [1, 2, 3, 4 ,5]
node = create_list(array)
print_list(node)
reverse = reverse_list2(node)
print_list(reverse)
