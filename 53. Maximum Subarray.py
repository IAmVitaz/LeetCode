from unittest import result
from typing import List

# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0: 
            return 0
        elif len(nums) == 1:
            return nums[0]     

        currentSum = nums[0]
        globalSum = nums[0]
    
        for i in range (1, len(nums)):
            currentSum = max(nums[i], nums[i] + currentSum) 
            globalSum = max(globalSum, currentSum)

        return globalSum

solution = Solution()
list = [-2,1,-3,4,-1,2,1,-5,4]
result = solution.maxSubArray(list)
print(result)