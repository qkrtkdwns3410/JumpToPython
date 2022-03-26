"""
 *packageName    : 
 * fileName       : 1543_문서_검색_S4
 * author         : qkrtk
 * date           : 2022-03-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-25        qkrtk       최초 생성
 """


def Solution(str_old, find_str):
      print("==========================================")
      print("str_old : %s " % str_old)
      print("find_str : %s " % find_str)
      cnt = 0
      while True:
            if str_old.find(find_str) == -1:
                  break
            str_old = str_old.replace(find_str, ' ', 1)
            cnt += 1
      
      print(cnt)


old = input().strip()
find = input().strip()
Solution(old, find)

Solution("ababababa", "aba")
Solution("aaa aaa", "a")
Solution("a a a a a", "a a")
Solution("ababababa", "ababa")
Solution("aaaaaaa", "aa")
