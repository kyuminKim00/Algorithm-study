### 다이나믹 프로그래밍 ###
# 한 번 계산된 문제는 다시 계산하지 않도록 하는 알고리즘
# 큰 문제를 작게 나누고 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘
# 컴퓨터는 메모리 공간과 연산 속도에 한계가 있어 최대한 효율적으로 구현해야하지만 
# 다이나믹 프로그래밍을 통해 약간의 메모리 공간을 더 사용하면서 연산 속도를 비약적으로 상승시킬 수 있다.

# 다이나믹 프로그래밍으로 해결할 수 있는 대표적인 문제는 피보나치 수열 문제가 있다.

# 피보나치 수열의 점화식 : An+2 = An + An+1, A1 = 1, A2 = 1

# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     else:
#         return fibo(x-1) + fibo(x-2)

# print(fibo(10))

# 피보나치 수열에는 큰 문제가 있는데 x가 커질 수록 연산 시간이 기하급수적으로 늘어난다. 
# 이유는 동일한 함수가 반복적으로 호출되기 때문이다. 시간 복잡도 O(2^n)

# fibo(10)을 계산하기 위해 f(5), f(4) 등이 반복적으로 호출된다. 이러한 문제를 다이나믹프로그래밍을 통해 해결한다.

# 다이나믹 프로그래밍은 다음 조건을 만족할 때 사용한다.
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# 메모리제이션 or 캐싱 : 한 번 구한 결과를 메모리 공간에 저장해두고 다시 호출하면서 사용하는 기법.

# d = [0] * 100 # 계산된 결과를 캐싱하기 위한 리스트

# def fibo(x):
#     if x==1 or x==2:
#         return 1
    
#     if d[x] != 0: # 이미 계산되어 있다면
#         return d[x] # 계산된 결과 반환
#     d[x] = fibo(x-1) + fibo(x-2) # 처음 계산하는 경우
#     return d[x]

# print(fibo(99))

# 이처럼 재귀함수를 이용하여 다이나믹 프로그래밍을 구현하는 방법은 Top-Down 방식이라고 한다. 
# 반면 반복문을 이용하여 구현하면 Bottom-Up 방식이라고 한다. 

# d = [0] * 100
# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3, n+1): # 반복문을 이용한 피보나치 수열
#     d[i] = d[i-1] + d[i-2]

# print(d[n])

# 전형적인 다이나믹 프로그래밍의 형태는 Bottom-uP 방식이다. 이 방식에서 사용되는 결과 저장용 리스트는 DP 테이블이라고 하고
# 메모리제이션은 Top-Down 방식을 부르는 표현이다.


### 실전문제2 : 1로 만들기 ###
# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
# 1. X가 5로 나누어떨어지면, 5로 나눈다.
# 2. X가 3으로 나누어떨어지면, 3으로 나눈다.
# 3. X가 2로 나누어떨어지면, 2로 나눈다.
# 4. X에서 1을 뺀다.

# 정수 X가 주어졌을 때 연산 4개를 적절히 사용해서 1을 만드려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# from itertools import permutations 
# x = int(input())
# arr = [5, 3, 2, 1]
# res = permutations(arr) # 순열 계산해서 모든 경우의 수 계산한 후 가장 연산 횟수가 적은 경우 출력
# res = list(res)
#                         # but 이렇게 하면 시간 초과가 발생함
# def one_calculate(arr, x):
#     for i in arr:
#         if i==1:
#             x-=1
#             return x
        
#         elif x%i==0:
#             x=x//i
#             return x
#     return x
        

# count_arr = []


# for i in res:
#     count = 0
#     x_ = x
#     while x_>1:
#         count+=1
#         x_ = one_calculate(i, x_)
    
#     count_arr.append(count)

# print(min(count_arr))

# ----------------------------------------------------------------------------------------------------- #

# Dynamic Programming 방식으로 품
# x = int(input())

# d = [0] * 30001

# for i in range(2, x+1):
#     d[i] = d[i-1] + 1 # x = x-1 인 경우

#     if i%2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     elif i%3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
#     elif i%5 == 0:
#         d[i] = min(d[i], d[i//5]+1)

# print(d[x])

## 실전문제3 : 개미 전사 ##
# N = int(input())
# arr = list(map(int, input().split()))

# d = [0] * 100
# d[0] = arr[0]
# d[1] = max(arr[0], arr[1])
# for i in range(2, N):
#     d[i] = max(d[i-1], d[i-2] + arr[i])
    
# print(d[N-1])

## 실전문제4 : 바닥 공사 ##
# 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 1X2, 2X1, 2X2의 덮개를 이용하여 바닥을 채울 때
# 발생하는 모든 경우의 수를 구하시오

# N = int(input())

# d = [0] * 1000
# d[1] = 1
# d[2] = 3
# for i in range(3, N+1):
#     d[i] = d[i-2]*2 + d[i-1]
    
# print(d[N]%796796)

## 실전문제5 : 효율적인 화폐 구성 ##
# N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용하여 그 가치의 합이 M원이 되도록한다.
# 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# N, M = map(int, input().split())
# arr = []
# for i in range(N):
#     arr.append(int(input()))

# d = [10001] * (M+1)
# d[0] = 0
# for i in range(N):
#     for j in range(arr[i], M+1):
#         d[j] = min(d[j], d[j-arr[i]]+1)

# print(d[M])

## 실전문제 31. 금광 ##

# t = int(input())
# result = []
# for i in range(t):
#     index = 0
#     n, m = map(int, input().split())
#     gold = [[0] * m for _ in range(n)]
#     arr = list(map(int, input().split()))
#     for j in range(n):
#         for k in range(m):
#             gold[j][k] = arr[index]
#             index += 1

#     dp_table = [[0]*m for _ in range(n)]
#     for i in range(n):
#         dp_table[i][0] = gold[i][0]

#     for j in range(1, m):
#         for i in range(n):
#             if i== 0:
#                 dp_table[i][j] = max(dp_table[i][j-1], dp_table[i+1][j-1]) + gold[i][j]
#             elif i == n-1:
#                 dp_table[i][j] = max(dp_table[i-1][j-1], dp_table[i][j-1]) + gold[i][j]
#             else:
#                 dp_table[i][j] = max(dp_table[i-1][j-1], dp_table[i][j-1], dp_table[i+1][j-1]) + gold[i][j]
#     max_ = 0
#     for i in range(n):
#         if dp_table[i][m-1] > max_:
#             max_ = dp_table[i][m-1]
#     result.append(max_)

# for i in result:
#     print(i)

## 실전문제 32. 정수 삼각형 ##

# n = int(input())
# arr = []
# dp_table = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#     dp_table.append([0]*len(arr[i]))
    
# for i in range(len(arr)):
#     if i == 0:
#         dp_table[i][0] = arr[i][0]
#         continue
#     for j in range(len(arr[i])):
#         if j == 0:
#             dp_table[i][j] = dp_table[i-1][j] + arr[i][j]
#         elif j == len(arr[i]) - 1:
#             dp_table[i][j] = dp_table[i-1][j-1] + arr[i][j]
#         else:
#             dp_table[i][j] = max(dp_table[i-1][j-1], dp_table[i-1][j]) + arr[i][j]

# print(max(dp_table[len(arr)-1]))

