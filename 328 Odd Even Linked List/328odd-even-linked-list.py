# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        o = []
        e = []
        while head:
            o.append(head.val)
            head = head.next
            if head:
                e.append(head.val)
                head = head.next
        head = ListNode(o[0])
        c = head
        for i in range(1, len(o)):
                c.next = ListNode(o[i])
                c = c.next
        for v in e:
            c.next = ListNode(v)
            c = c.next
        return head