"""
 *packageName    : 
 * fileName       : 1202_보석_도둑_G2
 * author         : ipeac
 * date           : 2022-03-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-27        ipeac       최초 생성
 """


def Solution(n, bag_count, jew_list, max_weight_list):
      print("==========================================")
      print("n : %s " % n)
      print("bag_count : %s " % bag_count)
      print("jew_list : %s " % jew_list)
      print("max_weight_list : %s " % max_weight_list)
      
      sorted(jew_list, key=lambda x: x[0])
      print("jew_list : %s " % jew_list)





Solution(2, 1, [[5, 10], [100, 100]], [11])
Solution(3, 2, [[1, 65], [5, 23], [2, 99]], [10, 2])

n, k = map(int, input().split())
jew_list = []
for _ in range(n):
      jew_list.append(list(map(int, input().split())))

print("jew_list : %s " % jew_list)
max_weight_list = []
for _ in range(k):
      max_weight_list.append(int(input()))
print("max_weight_list : %s " % max_weight_list)
