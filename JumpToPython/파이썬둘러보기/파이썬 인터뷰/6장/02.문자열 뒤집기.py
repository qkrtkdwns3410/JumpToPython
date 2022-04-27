"""
 *packageName    : 
 * fileName       : 02.문자열 뒤집기
 * author         : ipeac
 * date           : 2022-04-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-26        ipeac       최초 생성
 """

# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며. 리턴 없이 리스트 내부를
from typing import List


class Solution:
      
      def reverseString(self, s: List[str]) -> None:
            s.reverse()
