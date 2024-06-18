class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [(d,p) for d,p in zip(difficulty, profit)]
        jobs.sort()
        worker.sort()
        answer = 0
        i = 0
        l = (0, 0)
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                l = jobs[i] if jobs[i][1] > l[1] else l
                i+=1
            answer += l[1]
        return answer