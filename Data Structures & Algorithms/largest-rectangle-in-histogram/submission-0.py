class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftmax = [0]*len(heights)
        rightmax = [len(heights)-1]*len(heights)
        stack = [0]
        curmin = 0
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                popped_i = stack.pop()
                rightmax[popped_i] = (i-1)
            stack.append(i)
        stack=[len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                popped_i = stack.pop()
                leftmax[popped_i] = (i+1)
            stack.append(i)

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i]*(rightmax[i]-leftmax[i]+1))
        return max_area