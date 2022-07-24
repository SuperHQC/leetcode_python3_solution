#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        todo = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)
        q = deque()
        for i, j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        for k, v in todo.items():
            if len(v) == 0:
                q.append(k)
        res = []
        while q:
            n = q.popleft()
            for child in graph[n]:
                todo[child].remove(n)
                if len(todo[child]) == 0:
                    q.append(child)
            todo.pop(n)
            res.append(n)
        return res if not todo else []
                
# @lc code=end

