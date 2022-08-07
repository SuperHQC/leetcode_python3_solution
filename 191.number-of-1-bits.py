#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        # return self.helper(n, 0)

    def helper(self, n, count = 0):
        if n == 0:
            return count
        else:
            return self.helper(n & (n-1), count + 1)
        
# @lc code=end

