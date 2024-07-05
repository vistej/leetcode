# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        d = deque()
        l = []
        i = 0
        while head:
            d.append(head.val)
            if len(d) == 3:
                if (d[1] > d[0] and d[1] > d[2]) or (d[1] < d[0] and d[1] < d[2]):
                    l.append(i)
                d.popleft()
            head = head.next
            i += 1
        r = [-1, -1]
        if len(l) > 1:
            r[1] = l[-1] - l[0]
            r[0] = l[1] - l[0]
            for k in range(2, len(l)):
                r[0] = min(r[0], l[k] - l[k - 1])
        return r