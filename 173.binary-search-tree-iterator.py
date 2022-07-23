#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        self.stack.append(node)
        while node.left:
            self.stack.append(node.left)
            node = node.left
        

    def next(self) -> int:
        res = None
        if self.hasNext():
            node = res = self.stack.pop()
            if node.right:
                self.stack.append(node.right)
                node = node.right
                while node.left:
                    self.stack.append(node.left)
                    node = node.left
        return res.val

    def hasNext(self) -> bool:
        if self.stack:
            node = self.stack[-1]
            return node
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

