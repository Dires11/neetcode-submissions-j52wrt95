class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_nums = set()
        for num in nums:
            if num in prev_nums: 
                return True
            else:
                prev_nums.add(num)
        return False;