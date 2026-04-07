class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        length = 1
        max_len = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue

            if nums[i+1] - nums[i] != 1:
                max_len = max(max_len, length)
                length = 0
            length += 1

        return max(max_len, length)