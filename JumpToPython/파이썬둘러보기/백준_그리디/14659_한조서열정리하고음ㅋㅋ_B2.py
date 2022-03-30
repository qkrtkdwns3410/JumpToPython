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
      max_cnt = 0
      height = 0
      max_cnt_ans = 0
      
      for mountain in mountain_list:
            if mountain > height:
                  height = mountain
                  max_cnt = 0
            else:
                  max_cnt += 1
            max_cnt_ans = max(max_cnt_ans, max_cnt)
      print(max_cnt_ans)







Solution(5, [2, 1, 5, 4, 3])
Solution(7, [6, 1, 2, 9, 3, 4, 5])
Solution(3, [11, 1, 10])
Solution(7, [6, 4, 10, 2, 5, 7, 11])
n = int(input())
listlist = list(map(int, input().split()))
Solution(n, listlist)
