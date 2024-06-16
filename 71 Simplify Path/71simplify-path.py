class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path.split('/'))
        s = []
        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            if p == '..':
                if s:
                    s.pop()
            else:
                s.append('/' + p)
            
        

        return ''.join(s) if s else '/'