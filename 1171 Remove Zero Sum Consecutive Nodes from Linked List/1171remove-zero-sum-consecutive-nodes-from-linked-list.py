# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        headcopy = head
        while headcopy.next:
            arr.append(headcopy.val)
            headcopy = headcopy.next
        arr.append(headcopy.val)
        if sum(arr) == 0:
            return headcopy.next
        for i, val in enumerate(arr):
            l = i - 1
            k = val
            while l >= 0:
                k = k + arr[l]
                # if k > 0:
                #     break
                if k == 0:
                    for c in range(l, i + 1):
                        arr[c] = 0
                    break
                l = l - 1
                
        headcopy = head
        copy = headcopy
        i = 1
        print(arr)
        fs = arr[0] == 0
        while i < len(arr):
            if arr[i] == 0:
                temp = headcopy.next
                headcopy.next = temp.next if temp else None
            else:
                headcopy = headcopy.next
            i = i + 1

        if fs:
            return head.next

        return head