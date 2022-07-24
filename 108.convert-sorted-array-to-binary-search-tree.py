#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(0, len(nums), nums)

    def helper(self, start, end, nums):
        if start == end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(start, mid, nums)
        node.right = self.helper(mid + 1, end, nums)
        return node

        
# @lc code=end

