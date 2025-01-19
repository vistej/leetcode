# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        headcopy = head
        while headcopy.next:
            headcopy = headcopy.next
            count = count + 1
        index = count - n
        print(index)
        if index > 0:
            headcopy = head
            ct = 0
            while headcopy.next:
                ct = ct + 1
                if ct == index:
                    if headcopy.next:
                        remove = headcopy.next
                        if remove.next:
                            headcopy.next = remove.next
                        else:
                            headcopy.next = None
                    else:
                        headcopy.next = None
                    break
                headcopy = headcopy.next
        else:
            return head.next

            
        print(headcopy)
        print(head)
        return head
        