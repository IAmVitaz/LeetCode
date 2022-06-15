from typing import List

#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = m + n - 1

        while n > 0 and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[pointer] = nums1[m-1]
                m -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums2[n-1]
                n -= 1
                pointer -= 1
        while n > 0:
            nums1[pointer] = nums2[n-1]
            n -= 1
            pointer -= 1


        

solution = Solution()
# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

nums1 = [2,3,6,0,0,0]
m = 3
nums2 = [1,5,7]
n = 3

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

result = solution.merge(nums1, m, nums2, n)
print(nums1)

# print(Solution().merge(nums1=[1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

