class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        num_col = len(matrix[0])

        while l <= r:
            mid = (r+l)//2
            row = mid//num_col
            col = mid%num_col
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid +1
            else:
                r = mid-1
        return False