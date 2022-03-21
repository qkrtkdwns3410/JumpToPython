"""
 *packageName    : 
 * fileName       : 13305_주유소_S4
 * author         : qkrtk
 * date           : 2022-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-21        qkrtk       최초 생성
 """


# 도시의 개수 N , 인접한 두 도시를 연결하는 도로의 길이...N-1 개의 배열 , 주유소의 리터당 가격 N개의 자연수로
def Solution(n, road_length_list, station_price_per_liter):
      station_price_per_liter = station_price_per_liter[:-1]
      now_fuel = 0
      cost = 0
      min_value = min(station_price_per_liter)
      
      for index, num in enumerate(road_length_list):
            if min_value == station_price_per_liter[index]:
                  for index_in in range(index, len(road_length_list)):
                        cost += road_length_list[index_in] * station_price_per_liter[index]
                  
                  continue
            
            if index == 0:
                  cost += station_price_per_liter[index] * num
                  now_fuel += station_price_per_liter[index] * num
            else:
                  now_fuel -= road_length_list[index - 1]
                  
                  if station_price_per_liter[index] > station_price_per_liter[index - 1] and now_fuel < num:
                        cost += station_price_per_liter[index - 1] * num
                        now_fuel += station_price_per_liter[index - 1] * num
                  elif station_price_per_liter[index] <= station_price_per_liter[index - 1] and now_fuel < num:
                        cost += station_price_per_liter[index] * num
                        now_fuel += station_price_per_liter[index] * num
      print(cost)


# a=  int(input())
#
#
# Solution(4, [2, 3, 1], [5, 2, 4, 1])
Solution(4, [3, 3, 4], [1, 1, 1, 1])
