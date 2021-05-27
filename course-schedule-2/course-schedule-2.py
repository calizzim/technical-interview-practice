from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # make graph - use hash table
        graph = dict()
        for index in range(numCourses):
            graph[index] = []
        for pr in prerequisites:
            graph[pr[1]].append(pr[0])
        # check that the graph is acyclic - if not return []
        tovisit = set(range(numCourses))
        visiting = set()
        visited = deque()
        while(len(tovisit)):
            if not self.acyclicR(graph, tovisit, visiting, visited, tovisit.pop()): return []
        #determine order
        ans = []
        while(len(visited)):
            ans.append(visited.pop())
        return ans

    def acyclicR(self, graph: dict, tovisit: set, visiting: set, visited: set, current):
        if current in visited: return True
        if current in visiting: return False
        if(current in tovisit): tovisit.remove(current)
        visiting.add(current)
        for node in graph[current]:
            if not self.acyclicR(graph, tovisit, visiting, visited, node): return False
        visiting.remove(current)
        visited.append(current)
        return True
        
s = Solution()
print(s.findOrder(2,[[0,1],[1,0]]))