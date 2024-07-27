from typing import List
from math import inf

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            graph[i][i] = 0
        
        for o, c, cost in zip(original, changed, cost):
            x, y = ord(o) - ord('a'), ord(c) - ord('a')
            graph[x][y] = min(graph[x][y], cost)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                cost = graph[ord(s) - ord('a')][ord(t) - ord('a')]
                if cost == inf:
                    return -1
                total_cost += cost
        
        return total_cost