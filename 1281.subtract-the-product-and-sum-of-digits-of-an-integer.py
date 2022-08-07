#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(map(int, str(n)))
        return reduce(operator.mul, l) - sum(l)
        
# @lc code=end

