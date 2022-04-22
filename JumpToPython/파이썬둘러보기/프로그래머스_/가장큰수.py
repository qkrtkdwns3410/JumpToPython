"""
 *packageName    : 
 * fileName       : 가장큰수
 * author         : ipeac
 * date           : 2022-04-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-21        ipeac       최초 생성
 """


def solution(numbers):
      print("==========================================")
      print("numbers : %s " % numbers)
      numbers = sorted(list(map(str, numbers)))
      
      # 왜 3을 곱하는가? 최대자릿수는 1000...  num값에 최대 네자리까지 들어갈 수 있다.
      # 그렇기에 문자열 한자리 수 ' 9 ' 를 ' 999 ' 로 변환. 3자리 모두 각 자리수를 아스키값으로 비교하여 정렬해야한다.
      numbers.sort(key=lambda x: x * 3, reverse=True)
      print("numbers : %s " % numbers)
      
      answer = str(int(''.join(numbers)))
      print("answer : %s " % answer)
      return answer




solution([6, 10, 2])
solution([3, 30, 34, 5, 9])
solution([0, 0, 0, 0])
