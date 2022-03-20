"""
 *packageName    : 
 * fileName       : 12904_A와B_G5
 * author         : qkrtk
 * date           : 2022-03-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-20        qkrtk       최초 생성
 """


# 1<= S<=9999
# 2<=T <=1000
# S < T 길이

def Solution(s, t):
      list_s = list(s)
      list_t = list(t)
      
      switch = False
      
      while list_t:
            if list_t[-1] == 'A':
                  list_t.pop()
            elif list_t[-1] == 'B':
                  list_t.pop()
                  list_t.reverse()
            if list_t == list_s:
                  switch = True
                  break
      if switch:
            print(1)
      else:
            print(0)





a = input()
b = input()
Solution(a, b)
#
Solution("B", "ABBA")
Solution("AB", "ABB")
Solution("AAA", "AAAAAAAB")
