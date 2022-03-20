"""
 *packageName    : 
 * fileName       : 11000_강의실_배정_G5
 * author         : ipeac
 * date           : 2022-03-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-20        ipeac       최초 생성
 """
import heapq
import sys

heap = []
n = int(sys.stdin.readline())
arr = []

for i in range(n):
      a, b = map(int, sys.stdin.readline().split())
      arr.append([a, b])

arr.sort(key=lambda x: x[0])
print("arr : %s " % arr)

# 첫 번째 강의가 끝나는 시간 추가
heapq.heappush(heap, arr[0][1])
print("heap : %s " % heap)

for i in range(1, n):
      if heap[0] > arr[i][0]:
            heapq.heappush(heap, arr[i][1])
            print("heap : %s " % heap)
      else:
            heapq.heappop(heap)
            print("heap : %s " % heap)
            
            heapq.heappush(heap, arr[i][1])
            print("heap : %s " % heap)

print(len(heap))










#
