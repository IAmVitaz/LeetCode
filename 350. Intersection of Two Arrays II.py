from typing import List

# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = dict()
        result = []
        for num in nums1:
            if num in hashMap:
                occurence = hashMap[num]
                hashMap[num] = occurence + 1
            else:
                hashMap[num] = 1

        for num in nums2:
            if num in hashMap and hashMap[num] > 0:
                result.append(num)
                occurence = hashMap[num]
                hashMap[num] = occurence - 1
                
        return(result)

solution = Solution()
list1 = [1,2,2,1]
list2 = [2,2]
result = solution.intersect(list1, list2)
print(result)