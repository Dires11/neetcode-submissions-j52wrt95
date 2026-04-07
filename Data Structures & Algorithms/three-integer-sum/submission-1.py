class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for target in range(len(nums)):
            if target > 0 and nums[target] == nums[target-1]:
                continue
            i, j = target + 1, len(nums) - 1
            while i < j:
                total = nums[target] + nums[i] + nums[j]
                if total == 0:
                    out.append([nums[target], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]: i += 1
                    while i < j and nums[j] == nums[j-1]: j -= 1
                    i += 1
                    j -= 1
                elif total > 0:
                    j -= 1
                else:
                    i+=1
        return out