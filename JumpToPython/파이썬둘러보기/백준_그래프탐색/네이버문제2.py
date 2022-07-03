"""
 *packageName    : 
 * fileName       : 문제2
 * author         : jihye94
 * date           : 2022-06-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-27        jihye94       최초 생성
 """

def solution(n, m, survey):
    # n : 상품의 개수 , m : 등급 라인 , survey : 등급 부여
    print("n,m,survey : %s " % n, m, survey)
    answer = []
    
    grade_list = [[] for _ in range(m)]
    per_item_grade_list = {}
    
    for item in survey:
        prod, grade = item.split(" ")
        print("나누기 : %s " % prod, grade)
        
        print("ord(grade) : %s " % ord(grade))
        grade_list[ord(grade) - 65].append(prod)
    print("grade_list : %s " % grade_list)
    
    for grade_cnt in grade_list:
        print("grade_cnt : %s " % grade_cnt)
    
    return answer


solution(5, 4,
         ["apple A", "apple A", "ball B", "apple C", "ball C", "ball B", "ball C", "apple A", "cat B", "cat C", "cat C",
          "cat D", "dog A", "dog A", "dog C", "dog C", "dog C", "dog D", "elephant B", "elephant B", "elephant C",
          "elephant C", "elephant C", "elephant C"])
print("==========================================")
# solution(3, 3, ["bbccc A", "bbccc A", "bbccc B", "bbccc B", "aazz A", "aazz A", "aazz B", "aazz B", "aazz B", "aazz C",
#                 "bbccc B", "bbccc C", "aaabb A", "aaabb A", "aaabb B", "aaabb B", "aaabb B", "aaabb C"])
# print("==========================================")
# solution(2, 4, ["aaa A", "aaa A", "aaa C", "aaa D", "aaa D", "aaa D", "bbbb A", "bbbb A", "bbbb D", "bbbb D", "bbbb D",
#                 "bbbb D"])
