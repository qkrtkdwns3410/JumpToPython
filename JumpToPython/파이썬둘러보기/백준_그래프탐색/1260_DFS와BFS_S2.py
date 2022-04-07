"""
 *packageName    : 
 * fileName       : 1260_DFS와BFS_S2
 * author         : qkrtk
 * date           : 2022-04-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-05        qkrtk       최초 생성
 """


def Solution(n, m, v, node_list):
      print("==========================================")
      print("n : %s " % n)
      print("m : %s " % m)
      print("v : %s " % v)
      print("node_list : %s " % node_list)
      
      pass



Solution(4, 5, 1, [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]])
Solution(5, 5, 3, [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]])
Solution(1000, 1, 1000, [[999, 1000]])

n, m, v = map(int, input().split())
node_list = [list(map(int, input().split())) for _ in range(m)]
Solution(n, m, v, node_list)
