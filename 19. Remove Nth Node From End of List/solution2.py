# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        end = head
        previous = None
        for i in range(n):
            end = end.next
        while end:
            previous = start
            end = end.next
            start = start.next
        if previous:
            previous.next = start.next
            return head
        else:
            return start.next
