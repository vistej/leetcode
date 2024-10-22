# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level = [root]

        sum_heap = []

        while level:
            next_level = []
            s = 0
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                s += node.val
            heapq.heappush(sum_heap, -s)
            level = next_level
        if len(sum_heap) < k:
            return -1
        r = 0
        for i in range(k):
            r = heapq.heappop(sum_heap)
        
        return -r
