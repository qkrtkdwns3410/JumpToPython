"""
 *packageName    : 
 * fileName       : 03.로그 파일 재정렬
 * author         : ipeac
 * date           : 2022-04-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-26        ipeac       최초 생성
 """
from typing import List


class Solution:
      
      def reorderLogFiles(self, logs: List[str]) -> List[str]:
            letters, digits = [], []
            for log in logs:
                  if log.split()[1].isdigit():
                        digits.append(log)
                  else:
                        letters.append(log)
            
            # 2개의 키를 람다 표현식으로 정렬
            letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
            return letters + digits
