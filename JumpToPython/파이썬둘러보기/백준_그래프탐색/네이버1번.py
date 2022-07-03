# n : 앱의 개수 , recent : 최근 일자 기준 정수 ,
# recently_use, total_use : 삭제할 시간 기준을 나타내는 정수
#  records : 앱 이용 기록을 담은 2차원 정수 배열
def solution(n, recent, recently_use, total_use, records):
    print("==========================================")
    print("n : %s " % n)
    print("recent : %s " % recent)
    print("recently_use : %s " % recently_use)
    print("total_use : %s " % total_use)
    print("recent : %s " % recent)
    print("records : %s " % records)
    print("==========================================")
    
    answer = []
    total_time_per_app = {}
    recent_five_day_per_app = {}
    
    for record in records:
        print("==========================================")
        # 이용일자 및 최근 3일 , 전체 기간 합계
        use_day, app_num, use_time = map(int, record)
        
        if use_day <= recent:
            recent_five_day_per_app[app_num] = recent_five_day_per_app.get(app_num, 0)
            recent_use_time = recent_five_day_per_app[app_num]
            
            recent_five_day_per_app[app_num] = recent_use_time + use_time
        
        print("use_day, app_num, use_time : %s " % use_day, app_num, use_time)
        
        # 전체 기간 기산 값이 없는 경우 0 으로 세팅
        total_time_per_app[app_num] = total_time_per_app.get(app_num, 0)
        now_use_time = total_time_per_app[app_num]
        
        print("값 투입")
        print("앱 번호 : %s " % app_num)
        print("now_use_time : %s " % now_use_time)
        
        total_time_per_app[app_num] = now_use_time + use_time
        print("total_time_per_app : %s " % total_time_per_app)
        print("recent_five_day_per_app : %s " % recent_five_day_per_app)
        print("==========================================")
    
    for key, value in total_time_per_app.items():
        if value < total_use:
            for key2, value2 in recent_five_day_per_app.items():
                if key == key2 and value2 <= recently_use:
                    answer.append(key2)
    
    print(set(answer))
    return answer



solution(4, 5, 5, 10,
         [[1, 1, 2], [1, 2, 3], [2, 4, 3], [3, 1, 4], [5, 3, 3], [5, 2, 2], [7, 4, 4], [8, 3, 3], [10, 4, 3]])
solution(3, 3, 10, 30,
         [[1, 2, 7], [2, 1, 3], [3, 1, 5], [4, 2, 15], [5, 2, 10]])
