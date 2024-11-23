
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [[box[j][i] for j in range(m - 1, -1, -1)] for i in range(n)]


        for j in range(m):
            stones = deque()
            for i in range(n):
                if res[i][j] == "#":
                    stones.append(i)
                elif res[i][j] == "." and stones:
                    fi = stones.popleft()
                    res[fi][j] = "."
                    res[i][j] = "#"
                    stones.append(i)
                else:
                    stones = deque()


        return res