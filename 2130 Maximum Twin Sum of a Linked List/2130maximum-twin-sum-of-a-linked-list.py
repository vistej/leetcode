# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        store = {}
        msum = 0
        inx = 0
        while head:
            store[inx] = head.val
            inx += 1
            head = head.next
        hin = 0
        while hin <= inx//2:
            ns = store[hin] + store[inx - 1 - hin]
            if ns > msum:
                msum = ns
            hin += 1
        return msum
