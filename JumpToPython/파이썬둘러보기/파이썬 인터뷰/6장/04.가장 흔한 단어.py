"""
 *packageName    : 
 * fileName       : 04.가장 흔한 단어
 * author         : ipeac
 * date           : 2022-04-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-26        ipeac       최초 생성
 """
import collections
import re
from typing import List

class Solution:
      
      def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
            counts = collections.Counter(words)
            # 가장 흔하게 등장하는 단어의 첫 번쨰 인덱스 리턴
            return counts.most_common(1)[0][0]
