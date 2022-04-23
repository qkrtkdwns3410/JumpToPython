"""
 *packageName    :
 * fileName       : 큰수만들기_Lv2
 * author         : jihye94
 * date           : 2022-04-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-23        jihye94       최초 생성
 """


def solution(number, k):
      print("==========================================")
      print("number : %s " % number)
      print("k : %s " % k)
      
      number = list(number)
      result = [number.pop(0)]
      for n in number:
            if result[-1] < n:
                  while result and result[-1] < n and k > 0:
                        result.pop()
                        k -= 1
                  result.append(n)
            elif k == 0 or result[-1] >= n:
                  result.append(n)
      if k:
            result = result[:-k]
      answer = ''.join(result)
      return answer






solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)
