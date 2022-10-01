# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        start=head
        end=head.next
        while start is not None and end is not None and end.next is not None:
            if start==end:
                return True
            start=start.next
            end=end.next.next
        return False