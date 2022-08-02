# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = head
        previous = head
        while(list1 != None and list2 != None):
            if list1.val <= list2.val:
                curr = ListNode(list1.val)
                if previous:
                    previous.next = curr
                else:
                    head = curr
                previous = curr
                list1 = list1.next
            else:
                curr = ListNode(list2.val)
                if previous:
                    previous.next = curr
                else:
                    head = curr
                previous = curr
                list2 = list2.next
        if list1:
            if curr:
                curr.next = list1
            else:
                return list1
        elif list2:
            if curr:
                curr.next = list2
            else:
                return list2

        return head
