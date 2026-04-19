class Solution:
    #Looked up solution. Need to come back. 
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
        
        total = (len(a)+len(b))
        half = (len(a)+len(b))//2
        l = 0
        r = len(a)-1
        while True:
            a_index = (l+r)//2
            b_index = half-a_index -2
            
            lefta = a[a_index] if a_index >= 0 else float("-inf")
            righta = a[a_index+1] if a_index+1 < len(a) else float("inf")

            leftb = b[b_index] if b_index >=0 else float("-inf")
            rightb= b[b_index+1] if b_index+1 < len(b) else float("inf")
            
            if lefta <= rightb and leftb <= righta:
                if total % 2 == 1:
                    return min(righta, rightb)
                return (min(righta, rightb) + max(lefta, leftb))/2
            elif lefta > rightb:
                r = a_index-1
            else:
                l = a_index+1
