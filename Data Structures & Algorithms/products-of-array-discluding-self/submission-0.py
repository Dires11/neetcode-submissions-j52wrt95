class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProd = []
        suffixProd = []
        prefix = 1
        suffix = 1
        
        for i in range(len(nums)):
            prefixProd.append(prefix)
            prefix *= nums[i]
            suffixProd.append(suffix)
            suffix *= nums[len(nums)-i-1]


        suffixProd = suffixProd[::-1]
        out = []
        for i in range(len(nums)):
            out.append(prefixProd[i]*suffixProd[i])
        return out