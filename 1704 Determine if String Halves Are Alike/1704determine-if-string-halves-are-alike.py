class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c=0
        for i in range(len(s)):
            if i<len(s)//2:
                if s[i] in "aeiouAEIOU":
                    c-=1
            else:
                if s[i] in "aeiouAEIOU":
                    c+=1
        return c==0
 