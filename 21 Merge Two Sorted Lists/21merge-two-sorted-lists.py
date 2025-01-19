# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        end = head

        while list1 or list2:
            print('hello')
            if list1 and  (not list2 or list1.val <= list2.val):
                end.next = ListNode(list1.val)
                list1 = list1.next
            elif list2 and  (not list1 or list2.val <= list1.val):
                end.next = ListNode(list2.val)
                list2 = list2.next
            end = end.next
        
        return head.next
