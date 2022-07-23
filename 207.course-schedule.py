#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)
        for i, j in prerequisites:
            indegree[i].add(j)
            graph[j].add(i)
        q = deque()
        for k, v in indegree.items():
            if len(v) == 0:
                q.append(k)
        while q:
            node = q.popleft()
            for n in graph[node]:
                indegree[n].remove(node)
                if len(indegree[n]) == 0:
                    q.append(n)
            indegree.pop(node)
        return not indegree

        
# @lc code=end

