class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:

        def loop(node, i):
            if i == len(word):
                return node.end
            if word[i] == '.':
                ch = False
                for n in node.children.keys():
                    ch = ch or loop(node.children[n], i + 1)
                return ch
            elif word[i] not in node.children:
                return False
            return loop(node.children[word[i]], i + 1)

        node = self.root
        return loop(node, 0)            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)