from typing import List

# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        currentRow = 1
        result = []
        
        while currentRow <= numRows:
            newRow = []
            for i in range(currentRow):
                if i == 0 or i == currentRow - 1:
                    newRow.append(1)
                else:
                    newItem = result[currentRow - 2][i-1] + result[currentRow - 2][i]
                    newRow.append(newItem)
            result.append(newRow)
            currentRow += 1
        
        return result
                
solution = Solution()
print(solution.generate(numRows = 5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(solution.generate(numRows = 1)) # [[1]]
print(solution.generate(numRows = 0)) # []
