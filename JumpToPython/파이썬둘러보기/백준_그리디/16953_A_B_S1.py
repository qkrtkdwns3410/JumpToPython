def Solution(input_str):
      a, b = map(int, input_str.split())
      cnt = 1

      if b != a:
            while b >= a:
                  if b % 10 == 1:
                        b //= 10
                        cnt += 1
                  elif b % 10 != 1:
                        if b % 2 == 0:
                              b //= 2
                              cnt += 1
                        else:
                              print(-1)
                              return
                  if b < a:
                        print(-1)
                        return
                  elif b == a:
                        print(cnt)
                        return

      else:
            print(cnt)
            return




# def Solution(ex1):
#       print("==========================================")
#       try:
#             cnt = 0
#
#             a, b = map(int, ex1.split())
#
#             if a == b:
#                   print(1)
#                   return
#
#             if b % 2 != 0:
#                   b_last_str = str(b)[-1::]
#                   while str(b)[-1::] == '1':
#                         if b_last_str != '1':
#                               print(-1)
#                               return
#                         b = int(str(b)[:-1:])
#                         cnt += 1
#
#             while b % 2 == 0:
#                   if b == a:
#                         print(cnt + 1)
#                         return
#                   b //= 2
#                   cnt += 1
#
#                   if b == a:
#                         print(cnt + 1)
#                         return
#
#                   if b % 2 != 0:
#                         b_last_str = str(b)[-1::]
#                         while str(b)[-1::] == '1':
#
#                               if b_last_str != '1':
#                                     print(-1)
#                                     return
#                               b = str(b)
#                               b = int(b[:-1:])
#                               cnt += 1
#             if a == b:
#                   print(cnt + 1)
#                   return
#             elif b < a:
#                   print(-1)
#                   return
#             elif b % 2 != 0:
#                   print(-1)
#                   return
#       except Exception as e:
#             print(-1)
#             return


# c = input()
# Solution(c)
# Solution("2 162")
# Solution("2 31")
# Solution("2 81")
# Solution("1 31")
Solution("2 1611")
print("==========================================")
# Solution("4 42")
# print("==========================================")
# Solution("100 40021")
# print("==========================================")
