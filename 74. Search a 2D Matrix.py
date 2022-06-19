from typing import List

# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) #3
        col = len(matrix[0]) #2
        
        pointer_start = 0
        pointer_end = row * col - 1

        while pointer_end >= pointer_start:
            pointer_mid = int((pointer_end + pointer_start) / 2)
            mid_row = int(pointer_mid / col)
            mid_col = int(pointer_mid % col)
            if matrix[mid_row][mid_col] < target:
                pointer_start = pointer_mid + 1
            elif matrix[mid_row][mid_col] > target:
                pointer_end = pointer_mid - 1
            else: return True

        return False

solution = Solution()
print(solution.searchMatrix(matrix = [[1,2],[3,4],[5,6]], target = 5)) # true
# print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 30)) # true
# print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false
# print(solution.searchMatrix(matrix = [[1]], target = 1)) # true
# print(solution.searchMatrix(matrix = [[1,1]], target = 1)) # true


