### 구현 ###
# 구현 : 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 구현 유형의 문제는 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

# 유형
# 1. 완전탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 2. 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 문제

## 예제 4-1 : 상하좌우 ##
# 여행가 A는 NxN 크기의 정사각형 공간에 서있다. L, R, U, D 가 입력되면 여행가를 움직임.
# 만약 정사각형 공간을 벗어난다면 무시, 도착할 지점의 좌표를 출력

# n = int(input())
# arr = list(map(str, input().split()))
# y, x = 1, 1
# ss
# for i in arr:
#     if i == 'L':
#         y -= 1
#         if x<1 or y<1 or x>n+1 or y>n+1:
#             y +=1
            
#     elif i == 'R':
#         y += 1
#         if x<1 or y<1 or x>n+1 or y>n+1:
#             y -= 1
            
#     elif i == 'U':
#         x -= 1
#         if x<1 or y<1 or x>n+1 or y>n+1:
#             x += 1
            
#     elif i == 'D':
#         x +=1
#         if x<1 or y<1 or x>n+1 or y>n+1:
#             x -=1
        
# print(x, y)

## 예제 4-2 : 시각 ##
# 정수 N이 입력되면 00시00분00초 부터 N시59분59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
# n = int(input())
# count = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if i%10 ==3 or j%10==3 or 30<=j<40 or k%10==3 or 30<=k<40:
#                 count+=1

# print(count)
# 완전탐색 문제 유형으로 검색해야할 데이터의 개수가 100만개 이하일 때 사용한다. 문제에서 미리 검사한 후 접근

## 실전문제 2 : 왕실의 나이트 ##
# 8x8 체스판
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# a1 : 1열 1행, c2 : 3열 2행

# arr = str(input())
# col = int(ord(arr[0]) - int(ord('a')) + 1)
# row = int(arr[1])

# count = 0
# move_x = [2, 2, 1, -1, -2, -2, 1, -1]
# move_y = [-1, 1, 2, 2, -1, 1, -2, -2]

# for i in range(len(move_x)):
#     x, y = col, row
#     x += move_x[i]
#     y += move_y[i]
#     if 1<=x<=8 and 1<=y<=8:
#         count += 1
# print(count)

## 실전문제 3 : 게임 개발 ##
# 맵 안에서 움직이는 게임 캐릭터 시스템 개발, 캐릭터가 있는 맵의 크기는 NxM 직사각형, 각 칸은 육지 or 바다.
# 맵의 각 칸은 (A, B)로 나타내고 A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수

# 캐릭터가 움직이는 메뉴얼
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 
#    1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
    
# 메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 개수를 출력하는 프로그램을 만드시오.

# d = 0 : 북쪽
# d = 1 : 동족
# d = 2 : 남쪽
# d = 3 : 서쪽

# n, m = map(int, input().split()) # n x m 맵 생성
# a, b, d = map(int, input().split()) # (a, b)에 d을 바라보고 있는 캐릭터 
# arr = []
# for i in range(n):
#     arr_ = list(map(int, input().split()))
#     arr.append(arr_)

# arr[a][b] = 1
# #  1 1 1 1
# #  1 0 0 1
# #  1 1 0 1
# #  1 1 1 1     
# def rotate(d):
#     if d == 0 :
#         d = 3
#     elif d == 1:
#         d = 0
#     elif d == 2:
#         d = 1
#     elif d == 3:
#         d = 2
#     return d

# def move(a, b, d, arr):
#     if d == 0:
#         a -= 1
#     elif d == 1:
#         b += 1
#     elif d == 2:
#         a += 1
#     elif d == 3:
#         b -= 1
    
#     return a, b, arr

# def check_can_go(a, b, d, arr):
#     next_d = rotate(d)
#     next_a, next_b, _ = move(a, b, next_d, arr)
#     if arr[next_a][next_b] == 1:
#         return False
#     elif arr[next_a][next_b] == 0:
#         return True

# def move_back(a, b, d):
#     if d == 0:
#         a += 1
#     elif d == 1:
#         b -= 1
#     elif d == 2:
#         a -= 1
#     elif d == 3:
#         b += 1
#     return a, b

# count = 0
# count_move = 0
# while True:
#     if check_can_go(a, b, d, arr):
#         d = rotate(d)
#         a, b, arr = move(a, b, d, arr)
#         arr[a][b] = 1
#         count_move += 1
#         count = 0
#     else:
#         d = rotate(d)
#         count+=1
#         if count == 4:
#             a, b = move_back(a, b, d)
#             if arr[a][b] == 1:
#                 break
#             else:
#                 arr[a][b] = 1
#                 count_move += 1
#                 count = 0

# print(count_move+1)

## 실전문제 7. 럭키 스트레이트 ##

# n = str(input())

# left = n[0:len(n)//2]
# right = n[len(n)//2: ]

# left_sum = 0
# for i in left:
#     left_sum += int(i)

# right_sum = 0
# for i in right:
#     right_sum += int(i)

# if left_sum == right_sum:
#     print("LUCKY")
# else:
#     print("READY")


## 실전문제 8. 문자열 재정렬 ##

# s = input()

# str_arr = []
# int_arr = []
# for i in s:
#     if ord(i) >= 65:
#         str_arr.append(i)
#     else:
#         int_arr.append(i)

# str_arr.sort()

# sum = 0
# for i in int_arr:
#     sum += int(i)
# for i in str_arr:
#     print(i, end="")
# print(sum)

## 실전문제 9. 문자열 압축 ##

# def solution(s):
#     bank = []
#     for i in range(1, len(s)+1):
#         compressed = ""
#         count=1
#         for j in range(0, len(s), i):
#             now = s[j:j+i]
#             next = s[j+i:j+2*i]
#             if now == next:
#                 count+=1
#             else:
#                 if count>1:
#                     compressed += str(count) + now
#                     count=1
#                 else:
#                     compressed += now
#                     count=1
#         length = len(compressed)
#         bank.append(length)
#     answer = min(bank)
#     return answer

## 실전문제 10. 자물쇠와 열쇠 ##

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# def turn(k): # 2차원리스트 90도로 돌리는 함수
#     n = len(k)
#     m = len(k[0])
#     result = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = k[i][j]
#     return result

# def check(new_lock):
#     lock_lenght = len(new_lock) // 3
#     for i in range(lock_lenght, lock_lenght * 2):
#         for j in range(lock_lenght, lock_lenght * 2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     new_lock = [[0] * (n*3) for _ in range(n*3)]

#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]
    
#     for k in range(4):
#         key = turn(key)
#         for x in range(n*2):
#             for y in range(n*2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 if check(new_lock) == True:
#                     return True
                    
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False

## 실전문제 11. 뱀 ##  -> 아직 못 품
n = int(input())
map = [[0] * n for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j = map(int, input().split())
    map[i][j] = 1

snake = []
l = int(input())
for _ in range(l):
    time, direction = input().split()
    snake.append((int(time), direction))

def move(dir, x, y):
    if dir == 'right':
        return x+1, y
    if dir == 'down':
        return x, y +1
    if dir == 'up':
        return x, y-1
    if dir == 'left':
        return x-1, y

def rotate(now_dir, inst):
    if inst =='right':
        if now_dir =='right':
            return 'down'
        if now_dir =='left':
            return 'up'
        if now_dir =='up':
            return 'right'
        if now_dir == 'down':
            return 'left'
    if inst == 'left':
        if now_dir =='right':
            return 'up'
        if now_dir =='left':
            return 'down'
        if now_dir =='up':
            return 'left'
        if now_dir == 'down':
            return 'right'
        
def check(x, y, map):
    if x ==0 or x == len(map[0]):
        return False
    if y ==0 or y == len(map[0]):
        return False
    return True

flag = 1
count = 0
x, y = 1, 1
direction = 'right'
for i in snake:
        for j in i[0]:
            if flag:
                x, y = move(direction, x, y)
                if check(x, y, map):
                    count+=1
                else:
                    flag = 0
                    break
                direction = rotate(direction, i[1])


