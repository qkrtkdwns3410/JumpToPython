# 입력받을 숫자의 개수
n = int(input())

# 숫자 리스트
num_list = list(map(int, input().split()))

# + ,  - , * , / 의 개수
dx = list(map(int, input().split()))
minimum = int(1e9)
maximum = -int(1e9)

ans = num_list[0]

def dfs(idx):
      global ans
      global maximum, minimum
      
      if idx == n:
            if ans > maximum:
                  maximum = ans
            if ans < minimum:
                  minimum = ans
            return
      
      for i in range(4):
            tmp = ans
            
            if dx[i] > 0:
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
                  
                  dx[i] -= 1
                  dfs(idx + 1)
                  ans = tmp
                  dx[i] += 1

dfs(1)
print(maximum)
print(minimum)
