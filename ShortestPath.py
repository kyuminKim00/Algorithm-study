### 최단 경로 ###
# 최단 경로 알고리즘 유형에는 다양한 종류가 있는데 상황에 맞는 효율적인 알고리즘이 이미 정립되어 있다.
# 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 경우, 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우 등
# 최단 거리 알고리즘
# 1. 다익스트라 알고리즘 
# 2. 플로이드 워셜 알고리즘

## 다익스트라 알고리즘 ##
# 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘

# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 5. 3, 4 과정 반복

# 다익스트라 알고리즘은 최단 경로를 구하는 과정에서 '각 노드에 대한 현재까지의 최단 거리'의 정보를 항상 1차원 리스트에 저장하고 갱신함
# 이 리스트를 최단 거리 테이블이라고 함.

## 간단한 다익스트라 알고리즘 구현 ##
# O(V^2) 시간복잡도, 
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차탐색)한다.

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
# start = int(input()) # 시작 노드 입력 받기
# graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트(간선의 정보)
# visited = [False] * (n+1) # 방문한 적이 있는지 체크하는 목적의 리스트
# distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# for _ in range(m): # 간선 정보 입력받기
#     a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append((b, c))
    
# # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호 반환    
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     # 시작 노드 초기화
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
        
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n-1):
#         now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드
#         visited[now] = True # 방문 처리
        
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]: # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
#                 distance[j[0]] = cost

# dijkstra(start)

# # 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

# 위의 구현은 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야하고 현재 노드와 연결된 노드를 일일히 확인해야 하기 때문에
# 시간 복잡도가 O(V^2)이다. 노드의 개수가 5000개 이하라면 괜찮지만 넘어가면 시간 초과가 나올 가능성 높다.
# 따라서 개선된 다익스트라 알고리즘을 이용해야한다.

## 개선된 다익스트라 알고리즘 ##
# 시간복잡도 O(ElogV), E : 간선의 개수, V : 노드의 개수
# 개선된 다익스트라 알고리즘은 힙 자료구조를 사용, 힙을 이용하면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.
# 힙 자료구조 중 최소 힙은 값이 가장 낮은 원소를 먼저 추출하는데 단순히 힙을 이용해 만든 우선순위 큐를 이용해
# 시작 노드로부터 거리가 짧은 노드 순서대로 큐에서 나올 수 있도록 다익스트라 알고리즘을 작성한다.

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
# start = int(input()) # 시작 노드 번호
# graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# distance = [INF] * (n+1) # 최단 거리 테이블 초기화

# for _ in range(m): # 간선 정보(비용) 입력
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
    
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start)) # 거리 0, 시작 노드, 우선순위 큐에 삽입
#     distance[start] = 0 # 시작 노드의 거리는 0
#     while q: # 큐가 비어 있지 않다면 계속 실행
#         dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드 꺼내기
#         if distance[now] < dist: # 현재꺼낸 노드가 이미 처리된 적이 있는 노드라면 무시
#             continue
#         for i in graph[now]: # 현재 노드에 연결된 노드 확인
#             cost = dist + i[1]
#             if cost < distance[i[0]]: # 현재노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

        
# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

# 위의 개선된 다익스트라 알고리즘 구현은 간단한 다익스트라 알고리즘에 비해 시간복잡도가 O(ElogV)로 빠름.


### 플로이드 워셜 알고리즘 ###
# 다익스트라는 '한 지점'에서 다른 지점까지의 최단 경로를 구할 때 사용하는 알고리즘이라면
# 플로이드 워셜은 '모든 지점'에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용하는 알고리즘.
# 플로이드 워셜 알고리즘의 시간 복잡도 O(N^3)
# 다익스트라에서는 출발 노드가 1개이므로 최단 거리를 저장하기 위해 1차원 리스트를 사용하지만
# 플로이드 워셜에서는 2차원 리스트에 최단 거리 정보를 저장.
# 다익스트라는 그리디 알고리즘이지만 플로이드 워셜은 다이나믹 프로그래밍이다.

# 점화식 : Dab = min(Dab, Dak + Dkb)
# A에서 B로 가는 최소 비용과 A에서 K를 거쳐 B로 가는 비용을 비교하여 더 작은 값으로 갱신

# INF = int(1e9)
# n = int(input()) # 노드 개수
# m = int(input()) # 간선 개수
# graph = [[INF] * (n+1) for _ in range(n+1)] # 노드끼리의 거리를 담는 2차원 리스트, 이어져있지 않으면 INF

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0 # 자기 자신에서 자기 자신으로 가는 비용은 0

# for _ in range(m): # 각 간선에 대한 정보 입력, 초기화
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
    
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # 점화식에 따라 구현
            
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if graph[a][b] == INF:
#             print("INF")
#         else:
#             print(graph[a][b], end = " ")
#     print()


## 실전문제2 : 미래도시 ##
# 플로이드 워셜 알고리즘 문제 #

# n, m = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
            
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
    
# x, k = map(int,input().split())

# for m in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             cost = graph[i][j]
#             d_cost = graph[i][m] + graph[m][j]
#             if d_cost < cost:
#                 graph[i][j] = d_cost



# k_cost = graph[1][k]
# x_cost = graph[k][x]
# cost = k_cost + x_cost
# if cost >= INF:
#     print(-1)
# else:
#     print(cost)

## 실전문제3 : 전보 ##
# 다익스트라 알고리즘 문제#

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m, start = map(int,input().split())

# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int,input().split())
#     graph[a].append((b, c))
    
# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start))
    
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
        
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
                
# dijkstra(start)
# count = 0
# max_distance = 0
# for d in distance:
#     if d < INF:
#         count += 1
#         max_distance = max(max_distance, d)
        
# print(count-1, max_distance)
    
        


