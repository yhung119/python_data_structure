from node import *

'''
reverse_list1: reverse the linked list using recursion

reverse_list2: reverse the linked list with node pointers

'''

def reverse_list1(node):
	if(node is None or node.next is None):
		return node
	retval = reverse_list1(node.next)
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

##array to be reverse
array = [1, 2, 3, 4 ,5]
## create the singly linked list
node1 = create_singly_list(array)
node2 = create_singly_list(array)
print "Original list: \n"
print_list(node1)

print "Reverse_list 1: \n"
reverse = reverse_list1(node1)
print_list(reverse)

print "Reverse_list 2:\n"
reverse = reverse_list2(node2)
print_list(reverse)
