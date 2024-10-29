class Solution:
    def numTrees(self, n: int) -> int:
        trees = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += trees[root - 1] * trees[nodes - root]
            trees[nodes] = total
        
        return trees[n]