# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        currNum = 1
        curr = head
        previous = None
        while currNum <= (length-n) and currNum <= length:
            previous = curr
            curr = curr.next
            currNum += 1
        if previous:
            previous.next = curr.next
        else:
            return curr.next
        return head
