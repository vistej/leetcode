class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        arr = [1 if x[0] in vowels and x[-1] in vowels else 0 for x in words]
        res = []
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]


        for i, j in queries:
            y = arr[i - 1] if i > 0 else 0
            x = arr[j]
            re = x - y
            res.append(re if re > 0 else 0)

        return res