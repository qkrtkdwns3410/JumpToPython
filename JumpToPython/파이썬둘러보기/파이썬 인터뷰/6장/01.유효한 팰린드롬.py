"""
 *packageName    : 
 * fileName       : 01.유효한 팰린드롬
 * author         : ipeac
 * date           : 2022-04-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-26        ipeac       최초 생성
 """
import collections
import math
import re
import time
from typing import Deque

start = time.time()
math.factorial(100000)


def isPalindrome(s: str) -> bool:
      s = s.lower()
      # 정규식으로 불필요한 문자 필터링
      s = re.sub('[^a-z0-9]', '', s)
      
      return s == s[::-1]



# 주어진 문자열이 팰린드롬인지 확인하라! 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
s = "A man, a plan, a canal: Panama"
print("s : %s " % s)

print(isPalindrome(s))
end = time.time()

print(f"{end - start:.5f} sec")
