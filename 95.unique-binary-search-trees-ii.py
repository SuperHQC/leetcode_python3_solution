#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.subTree(1, n)
    
    def subTree(self, min, max):
        if min > max:
            return [None]
        res = []
        for i in range(min, max+1):
            leftA = self.subTree(min, i-1) 
            rightA = self.subTree(i+1, max)
            for nl in leftA:
                for nr in rightA:
                    node = TreeNode(i)
                    node.left = nl
                    node.right = nr
                    res.append(node)
        return res

    
        
# @lc code=end

