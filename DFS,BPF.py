### DFS/BFS ###
# 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

## DFS ##
# Depth-First Search, 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘, ##스택## 자료구조를 이용

# 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
# 방문처리 : 스택에 한 번 삽이되어 처리된 노드가 다시 삽입되지 않게 체크하는 것.

# def dfs(graph, v, visited):
#     visited[v] = True # 현재 노드를 방문 처리
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# graph = [ # 인접리스트로 그래프 표현
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9 # 노드가 방문된 정보를 1차원 리스트로 표현

# dfs(graph, 1, visited)


## BFS ##
# Breadth First Search, 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
# BFS 구현은 ##큐## 자료구조를 이용한다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 구현하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다.

# 동작 과정
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

# BFS는 O(N)의 시간이 소요되고 일반적으로 DFS보다 수행 시간이 짧다.

# from collections import deque

# def bfs(graph, start, visited): 
#     queue = deque([start]) # deque 객체를 만들고 start 노드 넣기 
#     visited[start] = True
#     while queue:
#         v = queue.popleft() # 가장 먼저 들어온 노드 pop
#         print(v, end=' ')
#         for i in graph[v]: # 노드에 인접한 노드 순회
#             if not visited[i]: 
#                 queue.append(i) # 아직 방문하지 않은 노드면 큐에 append
#                 visited[i] = True

# graph = [ # 인접리스트로 그래프 표현
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9
# bfs(graph, 1, visited)

## 실전문제3 : 음료수 얼려 먹기 ##
# NxM 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

# n, m = map(int, input().split())

# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input())))
    
# visited = [[False for j in range(m)] for i in range(n)]

# def DFS(graph, i, j, visited):
#     visited[i][j] = True
    
#     if 0<=i+1<n and 0<=j<m:
#         if not visited[i+1][j] and not arr[i+1][j]:
#             DFS(graph, i+1, j, visited)
#     if 0<=i-1<n and 0<=j<m:
#         if not visited[i-1][j] and not arr[i-1][j]:
#             DFS(graph, i-1, j, visited)
#     if 0<=i<n and 0<=j+1<m:
#         if not visited[i][j+1] and not arr[i][j+1]:
#             DFS(graph, i, j+1, visited)
#     if 0<=i<n and 0<=j-1<m:
#         if not visited[i][j-1] and not arr[i][j-1]:
#             DFS(graph, i, j-1, visited)

# count = 0

# for i in range(n):
#     for j in range(m):
#         if not visited[i][j] and not arr[i][j]:
#             DFS(arr, i, j, visited)
#             count+=1
# print(count)

## 풀이 ##
# 1. 특정한 지점의 주변 상하좌우를 살펴본 뒤 주변 지점에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 방문
# 2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하면 연결된 모든 지점 방문 가능
# 3. DFS를 시작했으면 아이스크림의 개수 1 더하기(DFS를 시작한다는 것은 하나의 집단을 센 것)
# 4. (0, 0) 에서 (n, m)까지 반복


## 실전문제4 : 미로 탈출 ##
# NxM 의 크기 직사각형 형태의 미로에 갇혀있다. 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재한다.
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시하고 한번에 한 칸씩 이동할 수 있다.
# 이때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오.

# from collections import deque

# queue = deque()
# arr = []
# n, m = map(int, input().split())
# number = [[0 for j in range(m)] for i in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def BFS(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue: # 큐가 빌 때까지 반복
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
            
#             if arr[nx][ny] == 0:
#                 continue
            
#             if arr[nx][ny] == 1:
#                 arr[nx][ny] = arr[x][y] + 1
#                 queue.append((nx, ny))
#     return arr[n-1][m-1]

# print(BFS(0, 0))
        
# graph = [ # 인접리스트로 그래프 표현
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * len(graph)

# def dfs(visited, graph, v):
#     visited[v] = True
#     print(v)
#     for i in graph[v]:
#         if visited[i] == False:
#             visited[i] = True
#             dfs(visited, graph, i)

# from collections import deque

# def bfs(graph, start,visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v)
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

## 실전 문제 15. 특정 거리의 도시 찾기 ##

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = [False] * (n+1)

# from collections import deque

# def bfs(graph, visited, start):
#     length = []
#     num = 0
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         num+=1
#         for i in graph[node]:
#             if not visited[i]:
#                 queue.append(i)
#                 length.append((i, num))
#                 visited[i] = True
#     return length

# length = bfs(graph, visited, 1)
# answer = []
# for i in length:
#     if i[1] == k:
#         answer.append(i[0])

# if len(answer) == 0:
#     print(-1)
# else:

#     answer.sort()
#     for i in answer:
#         print(i, end="\n")
