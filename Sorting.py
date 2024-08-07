### 정렬 ###
# 데이터를 특정한 기준에 따라 순서대로 나열
# 파이썬은 reverse 메소드를 지원하므로 오름차순 정렬 이후에 reverse 메소드를 사용하여 내림차순 정렬 한 것으로 바꿀 수 있다.

## 선택 정렬 ##
# 가장 원시적인 정렬 방법
# 데이터가 무작위로 있을 때 이중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해
# 앞에서 두 번째 데이터와 바꾸는 과정을 반복.
# 매번 가장 작은 것을 선택한다는 의미에서 선택 정렬(Selection sort) 알고리즘이라고 함.

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i] # 파이썬에서는 이렇게 swap할 수 있음
#                                                             # 다른 언어에서는 임시 저장용 변수를 통해 swap 해야함
 
# print(array)

## 선택 정렬의 시간 복잡도 ##
# N개의 데이터를 정렬할 때 선택 정렬은 N-1 번의 최소 값 찾는 연산을 수행해야함.
# 또한 최소 값을 찾는 연산을 찾기 위해서 N, N-1, N-2 , ... , 2 번의 비교 연산이 필요함.
# 따라서 근사치로 N x (N+1) / 2 번의 연산이 필요하고 빅오 표기법에 따라 O(N^2)으로 표현 가능.
# 기본적인 for문이 두 개 중첩되어 있으므로 O(N^2) 이라고 생각해도 좋음.

# 선택 정렬은 다른 정렬에 비해 시간 복잡도가 높음, 데이터가 10000개 이상일 때는 15초 이상 시간 소요

##################################################################################################################
##################################################################################################################

### 삽입 정렬 ###
# 특정한 데이터를 적절한 위치에 삽입한다는 의미에서 삽입 정렬(Insertion Sort)라고 함. 
# 특정한 데이터가 적잘한 위치에 삽입되기 이전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
# 삽입 정렬은 두 번째 데이터부터 시작한다. 첫번째 데이터는 이미 정렬되어있다고 판단하기 때문이다. 
# 두번째 데이터가 첫번째 데이터보다 큰지 작은지에 따라서 왼쪽, 오른쪽에 들어가는 두 경우가 존재하고, 경우에 따라 삽입한다.
# 세번째 데이터는 첫번째, 두번째 데이터의 관계에서 첫번째 데이터의 왼쪽, 두 데이터의 사이, 두번째 데이터의 오른쪽으로
# 들어가는 세 경우가 존재하고, 경우에 따라 삽입한다. 
# 이 과정을 마지막까지 반복하면 정렬이 완료된다.

# 삽입 정렬에서 정렬이 이루어진 원소는 항상 오름차순을 유지하고 있기 때문에 특정한 데이터를 삽입할 위치를 찾는 과정에서
# 그 데이터보다 작은 데이터를 찾으면 그 자리에 삽입하면 된다. 

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(array)): # 첫번째 원소는 이미 정렬되어 있다고 가정
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]: # 자기보다 큰 데이터를 만나면 자리를 바꾸면서 왼쪽으로 이동
#             array[j], array[j-1] = array[j-1], array[j]
#         else: 
#             break # 자기보다 작은 데이터를 만나면 그 자리에서 멈춤

# print(array)

## 삽입 정렬의 시간 복잡도 ##
# 삽입 정렬의 시간 복잡도는 O(N^2)이다. 배열이 거의 정렬되어 있지 않았을 때는 선택 정렬과 비슷한 시간이 소요되는데
# 현재 배열이 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다. 최선의 경우 O(N)의 시간 복잡도.
# 퀵정렬과 비교했을 때 보통의 경우는 삽입 정렬이 비효율적이지만 배열이 거의 정렬되어 있는 상황에서는 삽입 정렬이 더 빠르다.

##################################################################################################################
##################################################################################################################

### 퀵 정렬 ###
# 가장 많이 사용되는 알고리즘.
# 기준 데이터(피벗)을 설정하고 피벗보다 큰 데이터와 작은 데이터의 위치를 바꾸면서 정렬
# 피벗을 설정한 다음 큰 데이터와 작은 데이터를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다. 
# 피벗을 설정하는 방식으로 책에서는 가장 대표적인 방식인 호어 분할 방식을 기준으로 설명한다.

# 1. 리스트의 첫번째 데이터를 피벗으로 설정한다.
# 2. 왼쪽부터 피벗보다 큰 데이터를 찾고, 오른쪽부터 피벗보다 작은 데이터를 찾는다.
# 3. 두 데이터의 위치를 서로 변경한다.
# 4. 2, 3의 과정을 반복하다가 두 데이터의 위치가 엇갈리면(피벗보다 큰 데이터가 피벗보다 작은 데이터보다 오른쪽에 있는 경우)
#    피벗과 작은 데이터의 위치를 변경한다.
# 5. 4의 과정을 수행하면 피벗인 데이터보다 작은 데이터들은 왼쪽에, 큰 데이터들은 오른쪽에 존재하게 된다(분할됨).
# 6. 분할된 리스트의 첫번째 데이터를 피벗으로 설명하고 1-5 과정을 반복하여 정렬한다.

# 퀵 정렬은 재귀 함수 형태로 작성하는데 이때 퀵 정렬이 끝나는 조건을 명시해야한다.
# 퀵 정렬이 끝나는 조건은 현재 리스트의 데이터의 개수가 1개인 경우이다. 

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# def quick_sort(array, start, end):
#     if start >= end: # 재귀함수 종료조건, 원소가 1개인 경우 종료
#         return
    
#     pivot = start # 피벗은 첫번째 원소
#     left = start + 1
#     right = end
    
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1 # 왼쪽에서부터 피벗보다 큰 데이터 찾기
#         while right > start and array[right] >= array[pivot]:
#             right -= 1 # 오른쪽에서부터 피벗보다 작은 데이터 찾기
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right] # 엇갈렸다면 피벗과 작은 데이터 교체
#         else:
#             array[left], array[right] = array[right], array[left] # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
    
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
    
# quick_sort(array, 0, len(array)-1)
# print(array)

# def quick_sort_python(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0] # 피벗은 첫번째 원소
#     tail = array[1:] # 피벗을 제외한 리스트
    
#     left_side = [x for x in tail if x <= pivot] # 피벗보다 작은 데이터 리스트
#     right_side = [x for x in tail if x > pivot] # 피벗보다 큰 데이터 리스트
    
#     return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환

# print(quick_sort_python(array))

## 퀵 정렬의 시간 복잡도 ##
# 퀵 정렬의 시간 복잡도는 평균 O(NlogN)이다. 
# 최악의 경우 O(N^2), 퀵 정렬은 데이터가 정렬되어 있는 경우에는 매우 느리게 동작한다.(삽입 정렬과 반대)

##################################################################################################################
##################################################################################################################

### 계수 정렬 ###
# 계수 정렬은 특정한 조건이 부합할 때만 사용할 수 있는 매우 빠른 알고리즘.
# 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능하다. 
# 데이터가 무한한 범위를 가질 수 있는 실수형 데이터가 주어지는 경우 계수 정렬을 사용할 수 없다. 

# 이러한 제약이 발생하는 이유는 계수 정렬을 이용할 때 모든 범위를 담을 수 있는 크기의 리스트를 선언해야하기 때문이다.
# 예를 들어 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000이라면 1,000,001개의 데이터가 들어갈 수 있는 리스트를 선언해야한다.

# 계수 정렬은 앞의 3개의 정렬 방식처럼 데이터를 비교하고 자리를 변경하는 방식의 정렬이 아니다.

# 1. 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있는 리스트를 선언한다. 
# 2. 데이터를 하나씩 확인하며 1에서 선언한 리스트에서 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가한다.
# 3. 리스트에는 각 데이터가 몇 번 등장했는지 횟수가 기록되는데 이것이 정렬된 형태 그 자체이다.
# 4. 리스트의 첫 번째 데이터부터 하나씩 값만큼 인덱스를 출력하면 정렬된 형태가 보인다.

# array = [7, 5, 9, 0, 3, 1, 2, 2, 5, 0, 9 , 4, 2]
# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ') 
# print(count)
        
## 계수 정렬의 시간 복잡도 ##
# 데이터의 개수가 N, 데이터 중 최대값의 크기를 K라고 할 때 시간 복잡도는 O(N+K)이다.
# 범위가 제한되어 있는 상황에서 현존하는 정렬 알고리즘 중에서 가장 빠르다.

## 계수 정렬의 공간 복잡도 ##
# O(N+K)
# 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다. 
# 데이터가 0과 999999 두 개만 존재할 때 리스트의 크기는 1000000이 되어야하지만 단 두 값만 사용한다.
# 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다. 

##################################################################################################################
##################################################################################################################

### 파이썬의 정렬 라이브러리 ###
# 파이썬은 기본 정렬 라이브러리인 sorted() 함수를 제공한다. 이 함수는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을
# 기반으로 만들어져 시간 복잡도 O(NlogN)을 보장한다.

# array = [7, 1, 5, 2, 7, 8, 9, 3, 5]
# array_sorted = sorted(array)
# array.sort()
# print(array_sorted)
# print(array)

## 정렬 라이브러리의 시간 복잡도 ##
# 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다. 정렬 라이브러리는 이미 잘 작성된 함수이므로 퀵 정렬을 직접 구현하는 것보다
# sorted() 함수를 사용하는 것이 더 효과적이다.
# 문제에서 별도의 요구가 없이 단순히 정렬해야 하는 상황에서는 sorted() 함수를 사용하고 데이터의 범위가 한정되어 있으며
# 더 빨리 동작해야할 때는 계수 정렬을 사용하면 된다.

# 1. 정렬 라이브러리로 풀 수 있는 문제 : sorted() 함수 사용
# 2. 정렬 알고리즘의 원리에 대해 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제 풀 수 있음.
# 3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 방법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 알아야 풀 수 있다.

##################################################################################################################
##################################################################################################################

## 실전문제2 : 위에서 아래로 ##
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
    
# arr = sorted(arr, reverse=True)
# for i in arr:
#     print(i, end=' ')

## 실전문제3 : 성적이 낮은 순서로 학생 출력하기 ##
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오

# n = int(input())
# arr = []
# for i in range(n):
#     data = input().split()
#     arr.append([data[0], data[1]])

# arr = sorted(arr, key = lambda data : data[1]) # lammda 매개변수 : 매개변수 표현식 -> 함수 람다 정의 방법

# for i in arr:
#     print(i[0], end=' ')

## 실전문제4 : 두 배열의 원소 교체 ##
# 두 개의 배열 A, B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며 배열의 원소는 모두 자연수이다.
# 최대 K번의 바꿔치기 연산을 수행할 수 있는데 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열  B에 있는 원소 하나를 골라 두 원소를 서로 바꾸는 것이다.
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다. N, K, 배열 A, B에 대한 정보가 주어졌을 때 최대 K번의 바꿔치기 연산을 수행하여
# 만들 수 있는 배열 A의 모든 원소의 합의 최대값을 출력하는 프로그램을 작성하시오.

# n, k = map(int, input().split())
# A = map(int, input().split())
# B = map(int, input().split())

# A = sorted(A)
# B = sorted(B, reverse=True)

# for i in range(k):
#     if A[i]<B[i]:
#         A[i], B[i] = B[i], A[i]
#     else:
#         break

# print(sum(A))
    

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     tail = array[1:]
#     left = [x for x in tail if x<=pivot]
#     right = [x for x in tail if x>pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(array))

## 실전문제 23. 국영수 ##

# n = int(input())
# db = []
# for i in range(n):
#     db.append(input().split())

# db = sorted(db, key= lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# for i in range(len(db)):
#     print(db[i][0])

## 실전문제 24. 안테나 ##

# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()

# if len(arr) % 2 == 0:
#     median_1 = arr[len(arr)//2]
#     sum_1 = 0
#     for i in arr:
#         sum_1 += abs(i - median_1)
#     median_2 = arr[(len(arr)//2)-1]
#     sum_2 = 0
#     for i in arr:
#         sum_2 += abs(i-median_2)
#     if sum_1 >= sum_2:
#         print(median_2)
#     else:
#         print(median_1)
# else:
#     median = arr[len(arr)//2]
#     print(median)

# ## 실전문제 25. 실패율 ##

# def solution(N, stages):
#     num_people = len(stages)
#     arr = []
#     db = [0] * (N+2)
#     for i in stages:
#         db[i]+=1  
#     for i in range(len(db)-1):
#         if num_people==0:
#             ratio = 0
#         else:
#             ratio = db[i]/num_people
#         num_people -= db[i]
#         arr.append((i, ratio))

#     arr = sorted(arr, key = lambda x:x[1], reverse=True)

#     new_arr = []
#     for i in arr:
#         if i[0]!=0:
#             new_arr.append(i[0])

#     answer = new_arr
#     return answer

## 실전문제 26. 카드 정렬하기 ##

# n = int(input())
# card = []

# import heapq
# q = []
# for i in range(n):
#     heapq.heappush(q, int(input()))
# cost=0
# while len(q) > 1:
#     first = heapq.heappop(q)
#     second = heapq.heappop(q)
#     merge = first + second
#     cost += merge
#     heapq.heappush(q, merge)

# print(cost)