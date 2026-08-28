# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            stat = visited.get(head, False)
            if stat:
                return True
            visited[head] = True
            head = head.next
        return False
            