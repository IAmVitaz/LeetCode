from typing import List, Set

#https://leetcode.com/problems/two-sum/

# O(n) solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersDict = dict()

        for i in range(len(nums)):
            firstValue = nums[i]
            secondValue = target - firstValue
            if secondValue in numbersDict:
                return [numbersDict[secondValue], i]
            else:
                numbersDict[firstValue] = i

solution = Solution()
list = [2,7,11,15]
target = 9
result = solution.twoSum(list, target)
print(result)