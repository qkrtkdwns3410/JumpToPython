"""
 *packageName    : 
 * fileName       : 14888_연산자_끼워넣기_S1
 * author         : jihye94
 * date           : 2022-05-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-22        jihye94       최초 생성
 """
# 입력받을 숫자의 개수
n = int(input())

# 숫자 리스트
num_list = list(map(int, input().split()))
print("num_list : %s " % num_list)

# + ,  - , * , / 의 개수
dx = list(map(int, input().split()))
print("dx : %s " % dx)
minimum = int(1e9)
maximum = -int(1e9)

ans = num_list[0]

def dfs(idx):
      global ans
      global maximum
      global minimum
      
      if idx == n:
            if ans > maximum:
                  maximum = ans
            if ans < minimum:
                  minimum = ans
            return
      
      for i in range(4):
            tmp = ans
            print("i : %s " % i)
            
            if dx[i] > 0:
                  print("num_list[idx] : %s " % num_list[idx])
                  if i == 0:
                        ans += num_list[idx]
                  elif i == 1:
                        ans -= num_list[idx]
                  elif i == 2:
                        ans *= num_list[idx]
                  else:
                        if ans >= 0:
                              ans //= num_list[idx]
                        else:
                              ans = (-ans // num_list[idx]) * -1
                  dx[idx] -= 1
                  dfs(idx + 1)
                  ans = tmp
                  dx[idx] += 1

dfs(1)
print(maximum)
print(minimum)
