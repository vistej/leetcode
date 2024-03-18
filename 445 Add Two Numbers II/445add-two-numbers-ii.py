# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        l = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = []
        def getVal(val, carry):
            if carry:
                val = val + carry
            carry = val // 10
            val = val % 10
            return val, carry
        for i in range(l):
            val = 0
            if i >= len(a):
                val, carry = getVal(b[i], carry)
            elif i >= len(b):
                val, carry = getVal(a[i], carry)
            else:
                val, carry = getVal(a[i] + b[i], carry)
            res.append(val)
        while carry:
            val, carry = getVal(0, carry)
            res.append(val)

        res = res[::-1]
        ans = ListNode()
        tt = ans
        for r in res:
            tt.next = ListNode(r)
            tt = tt.next
        return ans.next