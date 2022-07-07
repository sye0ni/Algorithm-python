from collections import deque

n=int(input())

graph=[]

for i in range(n): # 그래프 만들기 
    a=list(input())
    a=list(map(int,a))
    graph.append(a)


def bfs(): # 시작점 
    dan_cnt=[] #단지 별 집 수 저장 공간 
    dan=0  #단지 수

    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:

                q=deque()
                q.append([i,j])
                graph[i][j]=0
                cnt=1  #단지 내 집 수 ++ 

                dx=[-1,1,0,0]
                dy=[0,0,-1,1]

                while q:
                    xx,yy=q.popleft()

                    for k in range(4):
                        nx=xx+dx[k]
                        ny=yy+dy[k]

                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue 
                        
                        if graph[nx][ny]==0:
                            continue 
                        
                        if graph[nx][ny]==1:
                            q.append([nx,ny])
                            cnt+=1
                            graph[nx][ny]=0
                #큐가 모두 비워지면 
                dan+=1
                dan_cnt.append(cnt)

    print(dan)
    dan_cnt.sort()
    for i in dan_cnt:
        print(i)

bfs()
