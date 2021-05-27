from collections import deque
s = deque()
s.append(1)
s.append(2)
s.append(3)
while(len(s)):
    print(s.pop())