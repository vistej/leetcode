class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        c = 0
        while money:
            money -= 8
            children -= 1
            if (not children and money) or money < children or (money == 4 and children == 1):
                return c
            c += 1

        return c