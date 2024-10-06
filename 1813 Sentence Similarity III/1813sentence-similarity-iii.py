class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        ls, ss = sentence1.split(' '), sentence2.split(' ')
        if len(ls) == len(ss):
            return sentence1 == sentence2

        if len(ls) < len(ss):
            ls,ss = ss,ls


        if ls[0] == ss[0]:
            if ls[-1] == ss[-1]:
                i = 0
                j = -1
                while i < len(ss) + j:
                    c = 0
                    if ls[i] == ss[i]:
                        i += 1
                        c = 1
                    if ls[j] == ss[j]:
                        j -= 1
                        c = 1
                    if not c:
                        break
                return i >= len(ss) + j
            else:
                return ''.join(ls[:len(ss)]) == ''.join(ss)
        elif ls[-1] == ss[-1]:
            return ''.join(ls[len(ls)-len(ss):]) == ''.join(ss)

        return False

