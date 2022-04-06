"""
 *packageName    : 
 * fileName       : n뒤집기_level1
 * author         : ipeac
 * date           : 2022-04-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-04        ipeac       최초 생성
 """


def solution(n):
      n_str = ""
      while True:
            n_str += str(n % 3)
            if n < 3:
                  break
            n //= 3
      
      answer = 0
      answer = int(n_str, 3)
      return answer


solution(45)
solution(125)
