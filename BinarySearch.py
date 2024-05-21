### 이진 탐색 ###
# 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘
# 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다. 
# 이진 탐색에서는 위치를 나타내는 3개의 변수를 사용한다.(시작점, 끝점, 중간점)
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하면서 원하는 데이터를 찾는 과정
# 이진 탐색은 찾으려는 데이터를 반씩 줄여가며 탐색하므로 시간복잡도는 O(logN)이다.

# 1. 시작점과 끝점을 확인하고 중간점을 정한다.(중간점이 실수일 때는 소수점은 버린다)
# 2. 중간점의 데이터와 찾으려는 데이터를 비교한다.
# 3. 비교하여 찾으려는 데이터가 더 크다면 시작점을 중간점으로 옮긴다. 반대로 더 작다면 끝점을 중간점으로 옮긴다.
# 4. 1-3 과정을 찾으려는 데이터와 중간점의 데이터가 같을 때까지 반복한다.

# def binary_search(array, target, start, end): # 재귀적으로 구현한 이진 탐색
#     if start > end:
#         return None
    
#     mid = (end + start)//2 # 중간점
    
#     if array[mid] == target:
#         return mid
    
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
    
#     else:
#         return binary_search(array, target, mid + 1, end)

# def binary_search(array, target, start, end): # 반복적으로 구현한 이진 탐색
#     while start<=end:
#         mid = (start+end)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
            
# n, target = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# result = binary_search(arr, target, 0, n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

## 실전문제2 : 부품 찾기 ##

# n = int(input())
# arr = list(map(int, input().split()))

# m = int(input())
# customer = list(map(int, input().split()))

# arr = sorted(arr) # 이진 탐색하기 전 정렬

# def binary_search(array, target, start, end): ## 재귀적으로 구현한 이진 탐색
#     if start>end:
#         return None

#     mid = (start + end)//2

#     if array[mid] == target:
#         return mid
    
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
    
#     else:
#         return binary_search(array, target, mid+1, end)
    

# for i in customer:
#     if binary_search(arr, i, 0, len(arr)-1) != None :
#         print("yes", end = ' ')
#     else:
#         print("no", end=' ')


## 실전문제3 : 떡볶이 떡 만들기 ##

# import sys
# n, m = map(int, sys.stdin.readline().rstrip().split())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# H = max(arr)
# customer = []

# while True: # 단순히 자르는 길이를 1씩 감소시켜가면서 풀기, 이렇게하면 시간 복잡도 측면에서 오답이 나올 가능성이 높다.
#     if H == 0:
#         break
#     count = 0
#     for i in arr:
#         length = i - H
#         if length >=0:
#             count+=length
#     customer.append([count, H])
#     H-=1

# print(customer)

# final = [i for i in customer if i[0]>=6]
# print(final)
# print(final[0][1])


# import sys
# n, m = map(int, sys.stdin.readline().rstrip().split())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))

# start = 0 
# end = max(arr)

# while True: # binary serach로 구현
#     if start>end:
#         break

#     mid = (start + end) // 2
#     all_length = 0
#     for i in arr:
#         one_length = i - mid
#         if one_length >= 0:
#             all_length+=one_length
#         else:
#             pass

#     if all_length>=m:
#         start = mid+1
#         result = mid

#     elif all_length<m:
#         end = mid-1

# print(result)
