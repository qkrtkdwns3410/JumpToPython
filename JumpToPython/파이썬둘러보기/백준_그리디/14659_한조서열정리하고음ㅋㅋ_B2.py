"""
 *packageName    : 
 * fileName       : 14659_한조서열정리하고음ㅋㅋ_B2
 * author         : qkrtk
 * date           : 2022-03-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-28        qkrtk       최초 생성
 """


def Solution(n, mountain_list):
      max_cnt_list = []
      max_cnt = 0
      
      index = 0
      
      while n:
            for in_index in range(index + 1, n):
                  if mountain_list[index] >= mountain_list[in_index]:
                        max_cnt += 1
            max_cnt_list.append(max_cnt)
            index += 1
            n -= 1
            max_cnt = 0
      
      max_cnt_list.sort(reverse=True)
      print(max_cnt_list[0])


n = int(input())
listlist = list(map(int, input().split()))
Solution(n, listlist)

# Solution(7, [6, 4, 10, 2, 5, 7, 11])
