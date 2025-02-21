# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = set()
        def loop(node, val, i):
            if not node:
                return
            if node.val == -1:
                node.val = 2 * val + i
                self.vals.add(node.val)
            
            loop(node.left, node.val, 1)
            loop(node.right, node.val, 2)
        loop(root, 0, 0)
        self.root = root
        

    def find(self, target: int) -> bool:
        return target in self.vals;
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)