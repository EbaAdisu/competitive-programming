class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        row = matrix[l]
        l = 0 
        r = len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        