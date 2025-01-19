class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        check_list = {}
        res = 0
        for num in nums:
            if num in check_list:
                check_list[num].append(check_list[num][-1] + 1)
            else:
                check_list[num] = [0]
        for key,val in check_list.items():
            res += sum(val)
        return res