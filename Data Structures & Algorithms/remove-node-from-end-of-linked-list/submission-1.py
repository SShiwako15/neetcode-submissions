# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
             return None
        n1 = 0
        temp = head
        while temp:
            n1 += 1
            temp = temp.next
        n2 = n1 - n
        if n2 == 0:
                head = head.next
                return head
        count = 1
        curr = head
        while curr:
            if not curr.next.next:
                curr.next = None
                return head
            if count == n2:
                curr.next = curr.next.next
                return head
            curr = curr.next
            count += 1
        return head
