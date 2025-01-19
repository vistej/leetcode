class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        def dfs(node, parent):
            c = 0
            for n, d in graph[node]:
                if n != parent:
                    c += d
                    c += dfs(n, node)
            return c

        return dfs(0, -1)