from collections import deque

n,m=map(int,input().split())

graph=[]

for i in range(n): # 그래프 만들기
    a=list(input())
    a=list(map(int,a))
    graph.append(a)

def bfs(x,y): # 시작점 
    cnt=[[0]*m for _ in range(n)]
    q=deque()
    q.append([x,y])
    cnt[x][y]=1

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]


    while q:
        xx,yy=q.popleft()
        
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue 

            if graph[nx][ny]==0:
                continue 

            if graph[nx][ny]==1:
                q.append([nx,ny])
                graph[nx][ny]=graph[xx][yy]+1

    print(graph[n-1][m-1])

bfs(0,0)
