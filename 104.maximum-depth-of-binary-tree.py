#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive
        # time: O(n)
        # space: O(n) worest case, average O(logn)
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        #iterative BFS
        # if not root:
        #     return 0
        # maxDepth = 0
        # q = deque()
        # q.append((root, 1))
        # while q:
        #     ptr, depth = q.popleft()
        #     maxDepth = max(maxDepth, depth)
        #     if ptr.left:
        #         q.append((ptr.left, depth + 1))
        #     if ptr.right:
        #         q.append((ptr.right, depth + 1))

        # return maxDepth
        
        #iterative DFS
        maxDepth = 0
        if not root:
            return maxDepth
        stack = [(root, 1)]
        while stack:
            ptr, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if ptr.left:
                stack.append((ptr.left, depth + 1))
            if ptr.right:
                stack.append((ptr.right, depth + 1))
            
        return maxDepth
        
# @lc code=end

