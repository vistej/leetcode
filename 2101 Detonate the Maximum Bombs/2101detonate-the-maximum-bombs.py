class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        combs = {}
        ans = 0
        def getId(bomb, i):
            return 'x' + str(bomb[0]) + 'y' + str(bomb[1]) + str(i)
        def getDist(bomb, tomb):
            return math.sqrt((tomb[0] - bomb[0])**2 + (tomb[1] - bomb[1])**2)
        for i, bomb in enumerate(bombs):
            combs[getId(bomb, i)] = []
            for y, tomb in enumerate(bombs):
                if i != y:
                    d = getDist(bomb, tomb)
                    if d <= bomb[2]:
                        combs[getId(bomb, i)].append(getId(tomb, y))
        

        def dfs(bomb, visited, count):
            if not bomb in visited:
                visited.append(bomb)
                count += 1
                if len(combs[bomb]):
                    for comb in combs[bomb]:
                        visited, count = dfs(comb, visited, count)
            return visited, count
        
        for bomb in combs:
            visited, count = dfs(bomb, [], 0)
            ans = max(ans, count)
        return ans