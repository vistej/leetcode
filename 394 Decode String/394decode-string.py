class Solution:
    def decodeString(self, s: str) -> str:
        a = []
        for c in s:
            if c == "]":
                v = a.pop()
                i = ""
                while a and not str(v).isnumeric():
                    i = v + i if v != "[" else i
                    v = a.pop()

                number = v
                while a and str(a[-1]).isnumeric():
                    number = a.pop() + number
                print(number, i)
                [a.append(i) for _ in range(int(number))]
            else:
                a.append(c)
        
        return "".join(a)
            

