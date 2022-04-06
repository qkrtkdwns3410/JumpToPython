"""
 *packageName    : 
 * fileName       : 15904_UCPC는_무엇의_약자일까_S4
 * author         : qkrtk
 * date           : 2022-04-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-03        qkrtk       최초 생성
 """


def Solution(sentence):
      print("==========================================")
      print("sentence : %s " % sentence)
      
      result_list = ['U', 'C', 'P', 'C']
      check_it = True
      for index in range(len(result_list)):
            if result_list[index] in sentence:
                  check_it = True
                  idx = sentence.find(result_list[index])
                  sentence = sentence[idx + 1:]
            else:
                  check_it = False
                  break
      if check_it:
            print("I love UCPC")
      else:
            print("I hate UCPC")








Solution("Union of Computer Programming Contest club contest")
Solution("University Computer Programming")
Solution("University CPC")
Solution("AUCPCA")
Solution("UCPCC")
Solution("CUCPC")
Solution("UUCPC")
n = input().strip()
Solution(n)
