# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        previous = None
        slow = temp
        while slow:
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp
        curr = head
        while curr and previous:
            tempSlowNext = previous.next
            previous.next = curr.next
            curr.next = previous
            previous = tempSlowNext
            curr = curr.next.next
