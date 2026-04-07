class Solution:
    def trap(self, height: List[int]) -> int:
        largest_left = []
        largest_right = [0]*len(height)
        l = 0
        r = 0
        for i in range(len(height)):
            l= max(height[i], l)
            largest_left.append(l)
            r = max(height[len(height)-i-1], r)
            largest_right[len(height)-i-1]=r
        water = 0
        for i in range(len(height)):
            water += min(largest_left[i], largest_right[i])-height[i]
        return water
       