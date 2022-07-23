#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        nodeCopy = Node(node.val)
        q = deque()
        nodeMap = {node: nodeCopy}
        q.append(node)
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in nodeMap:
                    neighborCopy = Node(neighbor.val)
                    q.append(neighbor)
                    nodeMap[n].neighbors.append(neighborCopy)
                    nodeMap[neighbor] = neighborCopy
                else:
                    nodeMap[n].neighbors.append(nodeMap[neighbor])
        return nodeCopy


        
# @lc code=end

