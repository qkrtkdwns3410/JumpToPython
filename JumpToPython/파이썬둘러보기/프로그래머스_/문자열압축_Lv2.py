"""
 *packageName    : 
 * fileName       : 문자열압축_Lv2
 * author         : jihye94
 * date           : 2022-04-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-24        jihye94       최초 생성
 """
import re


def solution(s):
      for i in range(1, len(s) // 2 + 1):
            re_list = re.sub('(\w{%i})' % i, '\g<l> ', s).split()
            print(re_list)



solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
