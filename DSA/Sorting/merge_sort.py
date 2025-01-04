import ultraimport

ListNode = ultraimport("__dir__/../DataStructures/linked_list.py", "ListNode")


# ----- List Merge Sort -----

def list_merge(left: list[int], right: list[int]):
	"""
		Merges two sublists

		:param left: left sublist
		:param right: right sublist

		:return: joined list
	"""
	res = []

	while left and right:
		if left[0] < right[0]:
			res.append(left[0])
			left.pop(0)
		else:
			res.append(right[0])
			right.pop(0)

	# append any remaining elements
	while left:
		res.append(left[0])
		left.pop(0)
	while right:
		res.append(right[0])
		right.pop(0)

	return res

def list_merge_sort(nums: list[int]):
	"""
		Recursively splits list into sublists
		until sublist size is 1, then rebuilds
		list from sorted sublists

		:param nums: list to be sorted

		:return: sorted list
	"""
	n = len(nums)

	# if list is trivially sorted...
	if n <= 1:
		return nums

	# divide into sublists
	left, right = [], []
	for i, num in enumerate(nums):
		if i < n // 2:
			left.append(num)
		else:
			right.append(num)

	# recursively sort sublists
	left = list_merge_sort(left)
	right = list_merge_sort(right)

	return list_merge(left, right)


# ----- Linked List Merge Sort -----

def find_middle(head: ListNode):
	"""
		Returns middle node of a linked list

		:param head: head of linked list

		:return: ListNode at center of linked list
	"""
    slow = head
    fast = head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow

def linked_list_merge(left: ListNode, right: ListNode):
	"""
		Merges two sublists

		:param left: head of left linked sublist
		:param right: head of right linked sublist

		:return: joined linked list
	"""
    l = left
    r = right
    dummy = ListNode(-1)
    curr = dummy

    while l and r:
        if l.val < r.val:
            curr.next = l
            curr = l
            l = l.next
        else:
            curr.next = r
            curr = r
            r = r.next
        
    curr.next = l if l else r

    return dummy.next

def linked_list_merge_sort(head: ListNode):
	"""
		Recursively splits linked list into sublists
		until sublist size is 1, then rebuilds
		list from sorted sublists

		:param head: head node of linked list
					 to be sorted

		:return: sorted linked list
	"""
    if not head or not head.next:
        return head

    middle = find_middle(head)
    left_head = head
    right_head = middle.next
    middle.next = None

    left = linked_list_merge_sort(left_head)
    right = linked_list_merge_sort(right_head)

    return linked_list_merge(left, right)

return linked_list_merge_sort(head)
