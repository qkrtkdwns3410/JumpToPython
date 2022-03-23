"""
 *packageName    : 
 * fileName       : 1744_수_묶기_G4
 * author         : qkrtk
 * date           : 2022-03-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-23        qkrtk       최초 생성
 """


def Solution(n, num_list):
      result = 0
      negative_list = []
      positive_list = []
      
      for num in num_list:
            if num <= 0:
                  negative_list.append(num)
            else:
                  positive_list.append(num)
      
      positive_list.sort(reverse=True)
      print("positive_list : %s " % positive_list)
      
      temp = 0
      for index, num in enumerate(positive_list):
            if temp != 0:
                  gop_num = temp * num
                  if temp + num > gop_num:
                        result += temp + num
                  else:
                        result += temp * num
                  
                  temp = 0
            else:
                  temp = num
                  if len(positive_list) - 1 == index:
                        result += temp
      
      negative_list.sort()
      
      print("negative_list : %s " % negative_list)
      
      temp2 = 1
      switch = False
      for index, num in enumerate(negative_list):
            
            if switch:
                  result += num * temp2
                  switch = False
                  continue
            
            if num == 0:
                  continue
            elif not switch:
                  temp2 = num
                  switch = True
                  if len(negative_list) - 1 == index:
                        result += temp2
      
      print(result)


n = int(input())
list_a = []
for _ in range(n):
      list_a.append(int(input()))
print("list_a : %s " % list_a)

Solution(n, list_a)

Solution(5, [-3, -2, -1, 1, 2])
Solution(2, [1, 2])
Solution(3, [-6, -5, -1])
Solution(5, [1, 1, 1, 1, 1])
Solution(13, [-10, -9, -8, -7, -6, -5, 1, 2, 3, 4, 5, 6, 7])
Solution(10, [-5, -4, -3, 0, 1, 2, 3, 4, 5, 6])
Solution(10, [-10, -9, -8, -7, -6, 0, 1, 2, 3, 4])

Solution(5, [-3, -2, -1, 1, 2])
Solution(5, [-3, -2, -1, 1, 2])
Solution(5, [-3, -2, -1, 1, 2])
# Solution(4, [-1, 2, 1, 3])
# Solution(6, [0, 1, 2, 4, 3, 5])
# Solution(1, [-1])
# Solution(3, [-1, 0, 1])
# Solution(2, [1, 1])
