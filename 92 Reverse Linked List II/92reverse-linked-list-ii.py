# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        hc = head
        ch = []
        f = None
        l = None

        i = 1

        while hc:
            
            if i >= left and i <= right:
                ch.append(hc.val)
            if i == left - 1:
                f = hc
            if i == right and hc.next:
                l = hc.next
            hc = hc.next
            i += 1
        print(ch)
        for i in range(len(ch) - 1, -1, -1):
            if not f:
                f = ListNode(ch[i])
                head = f
            else:
                f.next = ListNode(ch[i])
                f = f.next
        if f:
            f.next = l
        

        return head