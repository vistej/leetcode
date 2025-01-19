# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ha = head
        arr = []
        while ha:
            arr.append(ha.val)
            ha = ha.next
        he = head
        i = 1
        j = len(arr) - 1
        while i < j:
            he.next = ListNode(arr[j])
            j -= 1
            he = he.next
            he.next = ListNode(arr[i])
            i += 1
            he = he.next
        if i == j:
            he.next = ListNode(arr[i])
        