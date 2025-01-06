class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(map(int, boxes))
        n = len(boxes)
        l = boxes[0]
        r = sum(boxes) - boxes[0]
        lsum = 0
        rsum = sum([i * boxes[i] for i in range(n)])
        res = [rsum]

        for i in range(1, n):
            rsum -= r
            lsum += l
            res.append(lsum + rsum)
            r -= boxes[i]
            l += boxes[i]
        
        return res

                