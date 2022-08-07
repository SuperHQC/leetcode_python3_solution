#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dt = []
        for a, b in points:
            dt.append(abs(a- x) + abs(b - y))
        mp = map(int, dt)
        return reduce(operator.argmin, mp)
        
# @lc code=end

