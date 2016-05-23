from Node import *
'''
2.1 Remove Dups:
	Write code to remove duplicates from an unsorted linked list
	FOLLOW UP:
		How would you solve this problem if a temporary buffer is not allowed?
'''

def remove_dups(node):
	node_set = set()
	prev = None
	while node:
		if node.value in node_set:
			prev.next = node.next
		else:
			node_set.add(node.value)
			prev = node
		node = node.next
## testing
if False:
	array = [ 1, 2, 2, 1, 3, 3, 4, 5]
	head = create_singly_list(array)
	print_list(head)
	remove_dups(head)
	print_list(head)

'''
2.2 Return Kth to Last:
	Implement an algroithm to find the kth to last element of a singly linked list.
'''
def kthToLast(head, k):
	if head == None:
		return 0
	idx = kthToLast(head.next,k)+1
	if(idx == k):
		print_list(head)
	return idx
	
if False:
	array = [1, 2, 3, 4, 5]
	head = create_singly_list(array)
	print_list(head)
	kthToLast(head,3)

'''
2.3 Delete Middle Node:
	Implement an algorithm to delete a node in the middle of a singly linked list
	given only access to that node.
	EX:
	Input: the node c from the linked list a->b->c->d->e
	Output: nothing is returned but the new linked list is a->b->d->e
'''
def delete_middle_node(node):
	if node is None or node.next is None:
		return
	next = node.next
	node.value = next.value
	node.next = next.next

if False:
	array = [1, 2, 3, 4, 5]
	head = create_singly_list(array)
	node = head.next.next
	delete_middle_node(node)
	print_list(head)



'''
2.4 Partition:
	Write code to partition a linked list around a value x, such that all nodes less than x 
	come before all node greater than or equal to x. If x is contained within the list, the 
	values of x only need to be after the elements less than x
	Ex:
	Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
	Ouput: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

'''
2.5 Sum List


'''

'''
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
'''


'''
2.7 Intersection
'''

'''
2.8 Loop Detection:
'''

