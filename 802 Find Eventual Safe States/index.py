class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        leads = set()
        deads = set()

        def dfs(i, visited):
            if i in visited or i in deads:
                return False
            visited.add(i)
            if not graph[i]:
                leads.add(i)
                return True
            res = True
            for j in graph[i]:
                if j not in leads:
                    res = res and dfs(j, visited)
            if res:
                leads.add(i)
            else:
                deads.add(i)
            return res
        
        for i in range(len(graph)):
            visited = set()
            if i in leads or not graph[i] or dfs(i, visited):
                res.append(i)
                leads.add(i)



        return res