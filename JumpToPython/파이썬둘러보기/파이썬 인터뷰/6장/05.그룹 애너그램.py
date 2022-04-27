"""
 *packageName    : 
 * fileName       : 05.그룹 애너그램
 * author         : ipeac
 * date           : 2022-04-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-26        ipeac       최초 생성
 """
import collections
from typing import List

class Solution:
      
      def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # 에러가 나지 않도록 항상 디폴트를 생성해주는 defaultdict()으로 선언
            anagrams = collections.defaultdict(list)
            
            for word in strs:
                  # 정렬하여 딕셔너리 추가
                  anagrams[''.join(sorted(word))].append(word)
                  print("anagrams : %s " % anagrams)
            return list(anagrams.values())
