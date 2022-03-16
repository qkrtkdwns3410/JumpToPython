"""
 *packageName    : 
 * fileName       : 1343_폴리오미노
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """


def Solution(ex1):
      print("ex1 : %s " % ex1)
      ex1 = ex1.rstrip()
      polio_a = "AAAA"
      polio_b = "BB"

      if 'XXXX' in ex1:
            ex1 = ex1.replace('XXXX', polio_a)
      if 'XX' in ex1:
            ex1 = ex1.replace('XX', polio_b)

      if 'X' in ex1:
            print(-1)
      else:
            print(ex1)


a = input()
Solution(a)

Solution("XXXXXX")
print("==========================================")
Solution("XX.XX")
print("==========================================")
Solution("XXXX....XXX.....XX")
print("==========================================")
Solution('X')
print("==========================================")
Solution("XX.XXXXXXXXXX..XXXXXXXX...XXXXXX")
