class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n:
            temp = []
            i = 0
            j = 0
            while i < m or j < n:
                if i == m:
                    temp += nums2[j:]
                    break
                if j == n:
                    temp += nums1[i:m]
                    break
                if nums1[i] < nums2[j]:
                    temp.append(nums1[i])
                    i += 1
                else:
                    temp.append(nums2[j])
                    j += 1
            for i in range(len(temp)):
                nums1[i] = temp[i]

        