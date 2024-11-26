import ultraimport

ListNode = ultraimport("__dir__/../DataStructures/linked_list.py", "ListNode")


def floyd_cycle_detection(head: ListNode) -> bool:
	"""
		Floyd's Cycle Detection Algorithm

		:param head: head of singly-linked list

		:return: True if cycle detected, else False
	"""
	if not head or not head.next:
		return False

	slow = head
	fast = head

	while slow and fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if slow == fast:
			return True

	return False
