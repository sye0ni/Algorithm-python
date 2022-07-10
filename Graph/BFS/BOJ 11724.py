import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for i in range(1,m+1): # 그래프 만들기 
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)
q=deque()

def bfs(s):
    visited[s]=True
    q.append(s)

    while len(q)!=0:
        curr=q.popleft()
        for i in graph[curr]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

cnt=0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt+=1
print(cnt)
