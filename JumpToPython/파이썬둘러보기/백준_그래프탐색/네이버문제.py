keyboard = [["가", "호", "저", "론", "남", "드", "부", "이", "프", "설"],
            ["알", "크", "청", "울", "키", "초", "트", "을", "배", "주"],
            ["개", "캠", "산", "대", "단", "지", "역", "구", "너", "양"],
            ["라", "로", "권", "교", "마", "쿼", "파", "송", "차", "타"],
            ["코", "불", "레", "뉴", " ", "서", "한", "산", "리", "개"],
            ["터", "강", "봄", "토", "캠", "상", "호", "론", "운", "삼"],
            ["보", "람", "이", "경", "아", "두", "프", "바", "트", "정"],
            ["스", "웨", "어", "쿼", "일", "소", "라", "가", "나", "도"],
            ["판", "자", "비", "우", "사", "거", "왕", "태", "요", "품"],
            ["안", "배", "차", "캐", "민", "광", "재", "봇", "북", "하"]]


def solution(word):
      keyboard.reverse()
      
      print("keyboard : %s " % keyboard)
      answer = []
      # 없는 글자 스위치
      switch = False
      c_int = [0, 0]
      
      list_word = list(word)
      
      for word_str in list_word:
            for key_list in keyboard:
                  if word_str in key_list:
                        print("word_str : %s " % word_str)
                        # 해당 값이 중복값 검증
                        if keyboard.count(word_str) >= 2:
                              temp = []
                              
                              for index1, i in enumerate(keyboard):
                                    for index2, j in enumerate(i):
                                          if j == word_str:
                                                temp.append(
                                                      (index1, index2, abs(index1 - c_int[0]) + abs(index2 - c_int[1])))
                                                print("temp : %s " % temp)
                                                
                                                # answer.append(abs(index1 - c_int[0]) + abs(index2 - c_int[1]))
                                                # 이전 인덱스 값 설정
                                                # c_int = [index1, index2]
                              answer.append(max(temp)[2])
                              print("answer : %s " % answer)
                              # c_int =
                        else:
                              print('else')
                              
                              for index1, i in enumerate(keyboard):
                                    for index2, j in enumerate(i):
                                          if j == word_str:
                                                answer.append(abs(index1 - c_int[0]) + abs(index2 - c_int[1]))
                                                print("answer : %s " % answer)
                                                # 이전 인덱스 값 설정
                                                c_int = [index1, index2]
                  
                  
                  # 해당 값이 키 값에 없다면 20 점 처리
                  else:
                        # 없는 글자 스위치 on
                        switch = True
                        
                        answer.append(20)
                        c_int = [0, 0]
      
      print("list_word : %s " % list_word)
      
      return answer

def bfs():
      pass


solution("부스트캠프")
print("==========================================")
# solution("부슈트캠프")
# print("==========================================")
# solution("불레뉴캠프")
# print("==========================================")
# solution("뉴$솔레어")
# print("==========================================")
# solution("뉴뉴")
# print("==========================================")
