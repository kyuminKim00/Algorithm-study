### 자료구조 ###
## stack ##
# LIFO(Last In Fisrt Out)
# 파이썬에서 stack을 사용할 때는 별도의 라이브러리를 사용할 필요 없다. append(), pop() 사용

# stack = []
# stack.append(5) 
# stack.append(3)
# stack.append(1)
# print(stack)
# stack.pop() # 가장 마지막에 있는 원소 pop
# print(stack) # 최하단 원소부터 출력
# print(stack[::-1]) # 최상단 원소부터 출력

## queue ##
# FIFO(First In First Out)
# queue는 deque 라이브러리통해 사용한다.

# from collections import deque
# queue = deque()
# queue.append(5)
# queue.append(3)
# queue.append(1)
# queue.popleft() # 가장 나중에 들어온 원소를 pop
# queue.popleft()
# queue.append(2)
# print(queue)
# queue.reverse()
# print(queue)

## 그래프 ##
# 노드(Node), 간선(Edge)로 표현, 두 노드가 간선으로 연결되어있다면 두 노드는 인접(adjacent)라고 표현
# 그래프를 표현하는데는 두 가지 방식이 있다.

# 1. 인접 행렬(Adjacent Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식, 인접하지 않은 노드끼리는 무한의 비용이라고 작성.

# INF = 999999999999 # 무한의 비용
# graph = [
#     [0, 7, 5],
#     [7, 0 ,INF],
#     [5, INF, 0]
# ]

# 2. 인접 리스트(Adjacent List) : 리스트로 그래프의 연결 관계를 표현하는 방식, 노드에 연결ㄹ된 노드에 대한 정보를 차례대로 연결하여 저장
#    인접 리스트는 '연결리스트' 자료구조를 사용해 구횬하는데, 파이썬은 기본 자료형이 append() 메소드를 제공하므로 단순히 2차원 리스트를 이용하면 인접리스트 구현 가능
   
# graph = [[] for _ in range(3)] # 3행 2차원 스트
# graph[0].append((1, 7)) # 노드 0에 연결된 노드 저장, (노드, 거리), 노드 0에 노드 1이 거리 7로 연결되어 있다.
# graph[0].append((2, 5))
# graph[1].append((0, 7)) # 노드 1에 노드 0이 거리 7로 연결되어 있다.
# graph[2].append((0, 5))

# print(graph)

## 두 방식의 차이 ##
# 1. 메모리 측면
# 인접 행렬 방식은 노드 간의 모든 관계를 저장하므로 노드가 많아지면 메모리 낭비가 커짐. 
# 반면 인접 리스트 방식은 연결된 정보만을 저장하므로 메모리를 효율적으로 사용.

# 2. 속도 측면
# 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림.(인접 리스트에서는 연결된 데이터를 하나씩 확인해야 하므로)
# ex) 노드 1과 노드 7이 연결되어 있는 상황에서 인접행렬 방식에서는 graph[1][7] 만 확인하면 Edge를 알 수 있지만 인접 리스트 방식에서는 graph[1]에 대한 모든 인접리스트를
# 앞에서부터 확인해야한다.


### 재귀 함수 ###
# 재귀 함수 : 자기 자신을 다시 호출하는 함수
# 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용함. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을
# 끝내야 그 앞의 함수 호출이 종료되기 때문
# 재귀함수 구현에는 꼭 재귀함수 탈출 조건을 명시하여야 함.
# 재귀함수는 수학의 점화식을 그대로 소스코드로 옮김
# 점화식 : 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것

# def factorial_iterative(n): # 반복문으로 구현한 팩토리얼
#     result = 1
#     for i in range(1, n+1):
#         result*=i
        
#     return result

# def factorial_recursive(n): # 재귀적으로 구현한 팩토리얼
#     if n<=1:
#         return 1
#     return n * factorial_recursive(n-1)

# print("반복:", factorial_iterative(5))
# print("재귀:", factorial_iterative(5))


