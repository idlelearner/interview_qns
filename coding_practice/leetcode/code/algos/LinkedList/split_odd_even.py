# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        odd, cur_odd = head, head
        even, even_head = head.next, head.next
        while even!=None and even.next!=None:
            odd.next = odd.next.next
            odd = odd.next
            if odd!=None:
                cur_odd = odd
            even.next = even.next.next
            even = even.next
        cur_odd.next = even_head
        return head
