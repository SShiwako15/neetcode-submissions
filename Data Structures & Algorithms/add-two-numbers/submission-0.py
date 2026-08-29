# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        head = ListNode()
        
        nums1, n = 0, 0
        while l1:
            nums1 += l1.val * (10 ** n)
            n += 1
            l1 = l1.next
        
        nums2, n = 0,0
        l1 = l2
        while l2:
            nums2 += l2.val * (10 ** n)
            n += 1
            l2 = l2.next

        num = nums1 + nums2
        temp = head
        while num:
            temp.val = num % 10
            num = num // 10
            if num:
                temp.next = ListNode()
                temp = temp.next

        return head