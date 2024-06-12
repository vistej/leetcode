class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        vis=[-1]
        op=[]
        for i,g in enumerate(groups):
            if g!=vis[-1]:
                op.append(words[i])
                vis.append(g)
        return op
                
                
                
            
            
            