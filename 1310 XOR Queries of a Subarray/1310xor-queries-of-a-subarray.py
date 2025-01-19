class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
        print(arr)
        
        r = [arr[x[1]] ^ arr[x[0] - 1] if x[0] > 0 else arr[x[1]] for x in queries]

        return r