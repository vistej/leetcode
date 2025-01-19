class Solution:
    def minMaxDifference(self, num: int) -> int:
        a = list(str(num))
        ma = a[0]
        mb = a[0]
        num1 = list()
        num2 = list()
        
        for i in a:
            if i != '9':
                ma = i
                break

        for i in range(len(a)):
            if a[i] == ma:
                num2.append('9')
            else:
                num2.append(a[i])
            if a[i] == mb:
                num1.append('0')
            else:
                num1.append(a[i])

        return int("".join(num2)) - int("".join(num1))