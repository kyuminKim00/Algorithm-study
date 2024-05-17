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


