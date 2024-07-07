### 그리디 알고리즘 ###
# 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘

# 예제 3.1 : 거스름돈
# 거스름돈으로 사용할 500, 100, 50, 10원 짜리 동전이 무한이 존재한다고 가정, 거슬러 줘야 할 돈이 N원일 때
# 거슬러 줘야 할 동전의 최소 개수를 구하라, N은 항상 10의 배수이다.

# n = 1260
# count = 0
# coin = [500, 100, 50, 10]

# for i in coin:
#     count += n // i
#     n %= i

# print(count)

## 실전문제 1 : 큰 수의 법칙 ##
# 다양한 수로 이루어진 배열(배열의 크기 N)이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없다.

# N, M, K = map(int, input().split())
# array = list(map(int, input().split()))
# array = sorted(array, reverse=True) # 오름차순 정렬
# sum = 0 
# count = 0
# first = array[0] # 큰 수의 법칙 문제를 풀기 위해 가장 큰 값, 두번째로 큰 값만 있으면 풀수 있음
# second = array[1] # 가장 큰 값을 K번 더하고 두번째로 큰 값 한번 더하는 것을 반복
# while True:
    
#     for i in range(K):
#         if count == M:
#             break
#         sum += first
#         count+=1
#     if count == M:
#         break  
#     sum+=second
#     count+=1

# print(sum)

######################################################################################################
######################################################################################################

# 하지만 이렇게 풀면 M이 100억 이상일 때 시간 초과 판정을 받는다.
# 아래와 같이 가장 큰 수가 나오는 횟수를 미리 계산하는 것으로 접근해야 시간 초과 판정을 받지 않는다.
# N, M, K = map(int ,input().split())
# array = list(map(int, input().split()))

# array = sorted(array, reverse=True)
# first = array[0]
# second = array[1]

# count = M//(K+1)*K # 가장 큰 수가 나오는 횟수
# count += M % (K+1) # (K+1)로 나누어 떨어지지 않는 경우 가장 큰 수 나오는 횟수 추가

# sum = 0 
# sum += count * first
# sum += (M-count)*second
# print(sum)

######################################################################################################
######################################################################################################

## 실전문제 2 : 숫자 카드 게임 ##
# 1. 숫자가 쓰인 카드들이 NxM 형태
# 2. 뽑고자 하는 카드가 포함되어 있는 행 선택
# 3. 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑아야 함.
# 4. 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야함.

# 카드들이 NxM 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     arr_ = list(map(int, input().split()))
#     arr.append(arr_)
    
# arr_min = []
# for i in arr:
#     arr_min.append(min(i)) # 한 행에서 최소 값을 찾고

# print(max(arr_min)) # 그 중에서 최대 값을 찾으면 됨

######################################################################################################
######################################################################################################

## 실전문제 3 : 1이 될 때까지 ##
# 어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단 두번째 연산은 N이
# K로 나누어떨어질 때만 선택할 수 있다.

# 1.N에서 1을 뺀다.
# 2.N을 K로 나눈다.

# N과 K가 주어질 때 N이 1 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

# n, k = map(int, input().split())
# count = 0
# while n >1:
#     if n%k == 0: # 최대한 많이 나눌 수 있게 하는 것이 해답임
#         n = n//k
#         count += 1
#     else:
#         n = n-1
#         count += 1
# print(count)

## 기출문제 1. 모험가 길드 ##

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# arr.reverse()
# group=[]
# num = 0
# for i in arr:
#     if len(group)==0:
#         first = i
#     group.append(i)
#     if len(group) == first:
#         num+=1
#         group=[]

# print(num)      

## 기출문제 2. 곱하기 혹은 더하기 ##

# arr = input()
# s = []
# for i in arr:
#     s.append(int(i))

# a = [0, 1]

# for i in range(1, len(s)):
#     now = s[i]
#     if i == 1:
#         prev = s[i-1]
#     if (now in a) or (prev in a):
#         prev = now + prev
#     else:
#         prev = now * prev

# print(prev)

## 기출문제 3. 문자열 뒤집기 ##

# arr = input()
# num = 1
# for i in range(1, len(arr)):
#     if arr[i] == arr[i-1]:
#         pass
#     else:
#         num+=1

# print(num//2)

## 기출문제 4. 만들 수 없는 금액 ##

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()

# target = 1
# for i in arr:
#     if target < i:
#         break
#     target += i
    
# print(target)

## 기출문제 5. 볼링공 고르기 ##

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# num = 0

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i == j:
#             continue

#         if arr[i] != arr[j]:
#             num+=1

# print(num//2)

## 기출문제 6. 무지의 먹방 라이브 ##

def solution(food_times, k):
    for i in range(k-1):

        if sum(food_times) == 0:
            return -1
        
        index = i%len(food_times)        
        if food_times[index] != 0:
            food_times[index] -= 1
        
        else:
            index +=1
            index = index%len(food_times)
            while True:
                if food_times[index] != 0:
                    food_times[index] -=1
                    break
                else:
                    index +=1
                    index = index%len(food_times)
        answer = index+1

    return answer



print(solution([3, 1, 2], 2))