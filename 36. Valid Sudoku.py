import collections
from typing import List

# https://leetcode.com/problems/valid-sudoku/

# Complexity O(9^2^3) since we iterate through the matrix 3 times:
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # check sudoku horisontally:
#         for i in range(9):
#             results = set()
#             for j in range(9):
#                 item = board[i][j]
#                 if item != "." and item in results:
#                     return False
#                 else: 
#                     results.add(item)

#         # check sudoku vertically:
#         for i in range(9):
#             results = set()
#             for j in range(9):
#                 item = board[j][i]
#                 if item != "." and item in results:
#                     return False
#                 else: 
#                     results.add(item)

#         # check sudoku box:
#         for box in range(9):
#             horisontalShift = (box % 3) * 3
#             verticalShift = (int(box / 3)) * 3

#             results = set()
#             for i in range(3):
#                 for j in range(3):
#                     item = board[i + verticalShift][j + horisontalShift]
#                     if item != "." and item in results:
#                         return False
#                     else: 
#                         results.add(item)

#         return True

# Complexity O(9^2). Iterate through matrix only once:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        # check sudoku horisontally:
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                square =  int(i / 3) * 3 + int(j / 3)
                squareCol = int(j / 3)
                if (item in rows[i] or 
                    item in cols[j] or 
                    item in squares[square]):
                    return False
            
                rows[i].add(item)
                cols[j].add(item)
                squares[square].add(item)

        return True


solution = Solution()
print(solution.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)) # true

print(solution.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)) # false

print(solution.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6","3",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)) # false

print(solution.isValidSudoku(board = 
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]
)) # false

print(solution.isValidSudoku(board = 
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","1"]
,[".",".",".",".",".","3",".",".","."]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]
)) # false