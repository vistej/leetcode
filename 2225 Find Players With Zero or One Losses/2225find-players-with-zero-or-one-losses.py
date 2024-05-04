class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners , losers = set(),[]
        for match in matches:
            winners.add(match[0])
            losers.append(match[1])
        one_losers = Counter(losers)
        winners = winners-one_losers.keys()
        one_losers = {k:v for k,v in one_losers.items() if v ==1 }
        return [sorted(winners),sorted(one_losers.keys())]