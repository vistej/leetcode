class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = defaultdict(int) 

        ce = [0,0] 
        locations[tuple(ce)] += 1 

        for d in path :
            if d == 'N' :
                ce[0] += 1
            elif d == 'S' :
                ce[0] -= 1
            elif d == 'E' :
                ce[1] += 1
            elif d == 'W' :
                ce[1] -= 1 

            locations[tuple(ce)] += 1 
            if locations[tuple(ce)] > 1 :
                return True 

        return False 
