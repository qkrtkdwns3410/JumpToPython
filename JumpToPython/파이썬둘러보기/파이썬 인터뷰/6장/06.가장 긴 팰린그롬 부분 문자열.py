"""
 *packageName    : 
 * fileName       : 06.가장 긴 팰린그롬 부분 문자열
 * author         : ipeac
 * date           : 2022-04-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-27        ipeac       최초 생성
 """

class Solution:
      
      def longestPalindrome(self, s: str) -> str:
            print("str : %s " % str)
            
            # 팰린드롬 판별 및 투 포인터 확장
            def expand(left: int, right: int) -> str:
                  while left >= 0 and right < len(s) and s[left] == s[right]:
                        left -= 1
                        right += 1
                  return s[left + 1:right]
