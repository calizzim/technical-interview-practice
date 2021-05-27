from typing import List
from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        tovisit = set()
        visiting  = set()
        visited = deque()
        #setup graph
        graph = dict()
        for word in words:
            for letter in word:
                if letter not in graph: graph[letter] = []; tovisit.add(letter)

        
        #add rules to the graph
        for index, word in enumerate(words[0:len(words)-1]):
            nextWord = words[index+1]
            for letterIndex, letter in enumerate(word[0:int(min(len(word),len(nextWord)))]):
                nextWordLetter = nextWord[letterIndex]
                if letter != nextWordLetter:
                    graph[letter].append(nextWordLetter)
                    break

        #cycle detection and lexigraphical sorting
        while(len(tovisit)):
            if not self.dfsR(graph, tovisit, visiting, visited, tovisit.pop()): return ''
        
        #get order
        ans = ''
        while(len(visited)):
            ans = ans+visited.pop()
        return ans
        
    def dfsR(self, graph, tovisit, visiting, visited, current):
        if current in visited: return True
        if current in visiting: return False
        if current in tovisit: tovisit.remove(current)
        visiting.add(current)
        for node in graph[current]:
            if not self.dfsR(graph, tovisit, visiting, visited, node): return False
        visiting.remove(current), visited.append(current)
        return True

s = Solution()
print(s.alienOrder(['abc','ab']))