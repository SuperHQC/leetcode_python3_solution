#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = high - low + 1
        odds = count // 2
        if low % 2 != 0 and high % 2 != 0:
            odds += 1
        return odds
        
# @lc code=end

