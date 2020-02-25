# create a push, insert, append, delete or pop.
import collections
lis=collections.deque()
lis.append(2)
lis.append(3)
lis.append(4)
lis.append(5)
lis.append(6)
lis.append(2)
lis.insert(0,1)

print(lis)
lis.remove(2)
lis.pop()
lis.popleft()
print(lis)