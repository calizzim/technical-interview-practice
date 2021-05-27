from typing import List
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
        visited = set()
        while(len(tovisit)):
            ans = self.acyclicR(graph, tovisit, visiting, visited, tovisit.pop())
            if(not ans): return 
        return True

    def acyclicR(self, graph: dict, tovisit: set, visiting: set, visited: set, current):
        if current in visited: return True
        if current in visiting: return False
        if current in tovisit: tovisit.remove(current); visiting.add(current)
        for node in graph[current]:
            ans = self.acyclicR(graph, tovisit, visiting, visited, node)
            if(not ans): return False
        visiting.remove(current); visited.add(current)
        return True
        
s = Solution()
print(s.findOrder(2,[[0,1],[1,0]]))