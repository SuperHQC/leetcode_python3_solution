#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        A = sorted(nums)
        for i in range(len(A)-1, 1, -1):

            if A[i-1] + A[i-2] > A[i]:
                return A[i-1] + A[i-2] + A[i]
        return 0 
        
# @lc code=end

