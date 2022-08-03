# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = deque(lists)
        while len(lists) > 1:
            lists.append(self.sortTwoList(lists.popleft(), lists.popleft()))
        return lists[0] if len(lists) > 0 else None

    def sortTwoList(slef, list1, list2):
        head = ListNode()
        curr = head
        while list1 and list2:
            newNode = ListNode()
            if list1.val <= list2.val:
                newNode.val = list1.val
                list1 = list1.next
            else:
                newNode.val = list2.val
                list2 = list2.next
            curr.next = newNode
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head.next
