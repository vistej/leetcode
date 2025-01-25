class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        temp = sorted(nums)
        groups = [deque([temp[0]])]
        indexes = {temp[0]: 0}

        for i in range(1, len(nums)):
            if temp[i] - temp[i - 1] <= limit:
                groups[-1].append(temp[i])
            else:
                groups.append(deque([temp[i]]))
            indexes[temp[i]] = len(groups) - 1

        
        for i in range(len(nums)):
            group = groups[indexes[nums[i]]]
            nums[i] = group.popleft()

        
        return nums