from typing import List

# https://leetcode.com/problems/reshape-the-matrix/submissions/

# Solution by creating 1d array. Not optimal
# ------------------------------
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         m = len(mat)
#         if m == 0: return []
#         n = len(mat[0])
#         if n*m != r*c: return mat
        
#         oneDArray = []
#         resultArray = []

#         for i in range(m):
#             for j in range(n):
#                 oneDArray.append(mat[i][j])

#         for i in range(r):
#             row = []
#             for j in range(c):
#                 row.append(oneDArray[i * c + j]) 
#             resultArray.append(row)

#         return resultArray

# Solution with no in between array creation
# ------------------------------
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if row * col != r * c: return mat

        resultArray = [ [0] * c for i in range(r)]
        column_result = 0
        row_result = 0

        for i in range(row):
            for j in range(col):
                resultArray[row_result][column_result] = mat[i][j]
                column_result += 1
                if column_result == c:
                    column_result = 0
                    row_result += 1

        return resultArray

solution = Solution()
print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)) # [[1, 2, 3, 4]]
print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 4, c = 1)) # [[1], [2], [3], [4]]
print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4)) # [[1, 2], [3, 4]]
