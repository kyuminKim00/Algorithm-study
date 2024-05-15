# 그리디 알고리즘
# 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘

#예제 3.1 : 거스름돈
# 거스름돈으로 사용할 500, 100, 50, 10원 짜리 동전이 무한이 존재한다고 가정, 거슬러 줘야 할 돈이 N원일 때
# 거슬러 줘야 할 동전의 최소 개수를 구하라, N은 항상 10의 배수이다.

# n = 1260
# count = 0
# coin = [500, 100, 50, 10]

# for i in coin:
#     count += n // i
#     n %= i

# print(count)

# 실전문제 1 : 큰 수의 법칙
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
    
#  하지만 이렇게 풀면 M이 100억 이상일 때 시간 초과 판정을 받는다.
N, M, K = map(int ,input().split())
array = list(map(int, input().split()))

array = sorted(array, reverse=True)
first = array[0]
second = array[1]

count = M//(K+1)*K # 가장 큰 수가 나오는 횟수
count += M % (K+1) # (K+1)로 나누어 떨어지지 않는 경우 가장 큰 수 나오는 횟수 추가

sum = 0 
sum += count * first
sum += (M-count)*second
print(sum)
    
