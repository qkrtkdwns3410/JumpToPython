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
      cost = road_length_list[0] * station_price_per_liter[0]
      min_value = station_price_per_liter[0]
      
      dist = 0
      
      for i in range(1, n - 1):
            if station_price_per_liter[i] < min_value:
                  cost += min_value * dist
                  dist = road_length_list[i]
                  min_value = station_price_per_liter[i]
            
            else:
                  dist += road_length_list[i]
            
            if i == n - 2:
                  cost += min_value * dist
      print(cost)



n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

Solution(n, list_a, list_b)

#
# Solution(4, [2, 3, 1], [5, 2, 4, 1])
# Solution(4, [3, 3, 4], [1, 1, 1, 1])
