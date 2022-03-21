"""
 *packageName    : 
 * fileName       : 11047_동전_0_S4
 * author         : qkrtk
 * date           : 2022-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-21        qkrtk       최초 생성
 """


def Solution(coin_count, object_coin_value, coin_value_list):
      coin_value_list = sorted(coin_value_list, reverse=True)
      init_coin_value = 0
      cnt = 0
      
      while 1:
            if init_coin_value == object_coin_value:
                  print(cnt)
                  return
            for num in coin_value_list:
                  while num <= object_coin_value - init_coin_value:
                        init_coin_value += num
                        cnt += 1
                        
                        if init_coin_value == object_coin_value:
                              print(cnt)
                              return








a, b = map(int, input().split())
aaa = []
for _ in range(a):
      aaa.extend(map(int, input().split()))

Solution(a, b, aaa)
