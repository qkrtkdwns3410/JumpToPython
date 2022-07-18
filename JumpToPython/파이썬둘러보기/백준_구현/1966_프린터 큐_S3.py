"""
 *packageName    : 
 * fileName       : 1966_프린터 큐_S3
 * author         : jihye94
 * date           : 2022-07-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-18        jihye94       최초 생성
 """

# testcase num
import sys

input = sys.stdin.readline
t = int(input())
# test start
for i in range(t):
    # 문서의 개수 n , 몇 번쨰로 인쇄되었는지 궁금한 문서가 현재 Queue의 몇번쨰 인지 m
    n, m = map(int, input().split())
    
    # n 개의 문서의 중요도
    docu_priority = list(map(int, input().split()))
    docu_priority = [(v, idx) for idx, v in enumerate(docu_priority)]
    count = 0
    
    while True:
        if max(docu_priority)[0] == docu_priority[0][0]:
            count += 1
            if docu_priority[0][1] == m:
                print(count)
                break
            
            else:
                docu_priority.pop(0)
        else:
            docu_priority.append(docu_priority.pop(0))
