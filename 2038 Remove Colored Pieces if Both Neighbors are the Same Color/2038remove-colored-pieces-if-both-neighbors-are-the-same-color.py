class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count = 0
        b_count = 0
        alice = 0
        bob = 0
        for c in colors:
            if c == 'A':
                a_count += 1
                b_count = 0
            else:
                b_count += 1
                a_count = 0
            if a_count > 2:
                alice += 1
            if b_count > 2:
                bob += 1
        return alice > bob