class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = defaultdict(int)
        color_ball = defaultdict(set)

        res = [0] * len(queries)

        for i, [ball, color] in enumerate(queries):
            if not color_ball[color]:
                res[i] = res[i - 1] + 1 if i > 0 else 1
            else:
                res[i] = res[i - 1]
            color_ball[color].add(ball)
            if ball_color[ball] and ball_color[ball] != color:
                prev_color = ball_color[ball]
                color_ball[prev_color].remove(ball)
                if  not color_ball[prev_color]:
                    res[i] -= 1
            ball_color[ball] = color
        
        return res