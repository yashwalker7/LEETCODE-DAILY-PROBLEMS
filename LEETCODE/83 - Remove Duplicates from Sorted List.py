class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        p = head
        while p.next:
            n = p.next
            p.next = n.next
            n.next = head
            head = n

        return head