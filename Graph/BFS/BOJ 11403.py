import sys
from collections import deque

n=int(input())
graph=[[-1]*n for _ in range(n)]
visited=[False]*n

def bfs(s):
    global visited
    q=deque()
    q.append(s)
    while q:
        curr=q.popleft()
        for i in graph[curr]:
            if not visited[i] and i!=-1:
                q.append(i)
                visited[i]=True

for i in range(n): # 그래프 생성
    line=list(map(int,sys.stdin.readline().split()))

    for j in range(n):
        if line[j]==1:
            graph[i][j]=j


for i in range(n):
    visited=[False]*n
    bfs(i)
    for j in range(n):
        if visited[j]:
            print("1",end=' ')
            continue
        else:
            print("0",end=' ')
    print()
