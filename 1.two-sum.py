#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sol1
        # time: O(n), space O(n)

        numDict = {}
        for i in range(len(nums)):
            temp = nums[i]
            if numDict.get(target - temp) is not None:
                return [numDict[target - nums[i]], i]
            else:
                numDict[temp] = i
        

        # sol2
        # time: O(n^2), space O(1)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        return []


# @lc code=end

