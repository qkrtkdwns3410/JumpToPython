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
import collections


def solution(number, k):
      print("==========================================")
      print("number : %s " % number)
      print("k : %s " % k)
      res = []
      cnt = 0
      max_value = 0
      
      for i, v in enumerate(number):
            print("cnt : %s " % cnt)
            if cnt == k:
                  print("append 수행")
                  res.append(v)
                  
                  continue
            print("i : %s " % i)
            print("v : %s " % v)
            if i == 0:
                  print("첫번째")
                  res.append(v)
                  max_value = v
                  
                  print("res : %s " % res)
            
            elif i != 0 and res[-1] < v:
                  if max_value < v:
                        max_value = v
                  
                  for num in res:
                        res.remove(num)
                  
                  print("pop수행")
                  res.pop()
                  cnt += 1
                  
                  res.append(v)
                  print("res : %s " % res)
            else:
                  res.append(v)
      
      print("res : %s " % res)
      
      return res



# solution("1924", 2)
# solution("1231234", 3)
solution("4177252841", 4)
