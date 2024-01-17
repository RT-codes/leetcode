# 4. Median of Two Sorted Arrays
# Solved
# Hard
# Topics
# Companies

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = 0

        # combined arrays and reverse the order 
        combined_nums = sorted(nums1 + nums2, reverse=True)
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            middle_index = length // 2
            result = combined_nums[middle_index]
        else:
            middle_index_1 = length // 2 - 1
            middle_index_2 = length // 2
            val_1 = combined_nums[middle_index_1]
            val_2 = combined_nums[middle_index_2]
            result = ( val_1 + val_2 ) / 2.0
            print(val_1)
            print(val_2)
        return result

