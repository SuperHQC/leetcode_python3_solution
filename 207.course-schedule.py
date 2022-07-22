#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)
        q = deque()
        for i, j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        for k, v in todo.items():
            if len(v) == 0:
                q.append(k)
        while q:
            n = q.popleft()
            for i in graph[n]:
                todo[i].remove(n)
                if len(todo[i]) == 0:
                    q.append(i)
            todo.pop(n)
        return not todo

        
# @lc code=end

