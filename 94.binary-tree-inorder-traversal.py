#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorder(root, [])
    
    def inorder(self, node: Optional[TreeNode], res: List[int]):
        if node.left:
            self.inorder(node.left, res)
        res.append(node.val)
        if node.right:
            self.inorder(node.right, res)
        return res

# @lc code=end

