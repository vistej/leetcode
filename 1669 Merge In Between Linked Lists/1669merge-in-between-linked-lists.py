# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        l2end = list2
        while l2end.next:
            l2end = l2end.next

        l1cop = list1
        while l1cop and l1cop.next:
            if i  == a - 1:
                temp = l1cop
                while temp.next:
                    temp = temp.next
                    i += 1
                    if i == b + 1:
                        l2end.next = temp
                        l1cop.next = list2
                        l1cop = temp.next
                        return list1
            l1cop = l1cop.next
            i += 1
        return list1
