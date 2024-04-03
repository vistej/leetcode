class Solution:
    def  findWord(self, board, word, checked, i, j, x):
        if board[i][j] == word[x] and (i, j) not in checked:
            cc = dict(checked)
            cc[(i, j)] = True
            if (x == len(word) - 1) or (i - 1 >= 0 and self.findWord(board, word, cc, i - 1, j, x + 1)) or (j - 1 >= 0 and self.findWord(board, word, cc, i, j - 1, x + 1)) or (i + 1 < len(board) and self.findWord(board, word, cc, i + 1, j , x + 1)) or (j + 1 < len(board[0]) and self.findWord(board, word, cc, i, j + 1, x + 1)):
                return True
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    checked = {}
                    if self.findWord(board, word, checked, i, j , 0):
                        return True
        return False