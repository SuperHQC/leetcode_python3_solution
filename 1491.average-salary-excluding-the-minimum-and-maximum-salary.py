#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        mins = 10**7
        maxs = 0
        total = 0
        for i in salary:
            mins = min(mins, i)
            maxs = max(maxs, i)
            total += i
        # print(total)
        # print(mins)
        # print(maxs)
        # print(total - mins - maxs)
        # print(len(salary)-2)
        return (total - mins - maxs) / (len(salary)-2)
# @lc code=end

