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
        for i, j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        q = deque()
        for k, v in todo.items():
            if len(v) == 0:
                q.append(k)
        while q:
            n = q.popleft()
            for neighbor in graph[n]:
                todo[neighbor].remove(n)
                if len(todo[neighbor]) == 0:
                    q.append(neighbor)
            todo.pop(n)
        return not todo

        
# @lc code=end

