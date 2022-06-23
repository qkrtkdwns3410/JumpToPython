"""
 *packageName    : 
 * fileName       : ex1
 * author         : ipeac
 * date           : 2022-03-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-14        ipeac       최초 생성
 """
import json
import random
import requests
from pprint import pprint

SUBWAY_LIST_URL = "https://apis.zigbang.com/property/biglab/subway/all?"
ROOM_LIST_URL = "https://apis.zigbang.com/v3/items/ad/{subway_id}?deposit_s=0&detail=false&domain=zigbang&floor=1~%7Crooftop%7Csemibase&radius=1&rent_s=0&sales_type="
ROOM_INFO_URL = "https://apis.zigbang.com/v2/items/{room_id}"


# 지하철 정보 수집
def getSubwayId(subway_name):
      REQUEST_URL = SUBWAY_LIST_URL
      
      req = requests.get(SUBWAY_LIST_URL)
      if req.status_code == 200:
            data = json.loads(req.text)
            
            subway_info = [item['id'] for item in data if item['name'] == subway_name]
            
            if len(subway_info) > 0:
                  return subway_info[0]
      
      return None

# 매물 목록 수집
def getRoomList(subway_id):
      REQUEST_URL = ROOM_LIST_URL.format(subway_id=subway_id)
      
      req = requests.get(REQUEST_URL)
      if req.status_code == 200:
            data = json.loads(req.text)
            
            return [item["simple_item"]["item_id"] for item in data["list_items"] if 'ad_agent' not in item]
      
      return list()

# 매물 상세정보 수집
def getRoomInfo(room_id):
      REQUEST_URL = ROOM_INFO_URL.format(room_id=room_id)
      
      req = requests.get(REQUEST_URL)
      if req.status_code == 200:
            data = json.loads(req.text)
            
            return data
      
      return None

# 매물 상세정보를 입맞대로 파싱
def parseRoomInfo(room_info, find_text=None):
      parsed_data = {
            "url": 'https://www.zigbang.com/home/oneroom/items/{}'.format(
                  room_info["item"].get("item_id"))
            , "item_id": room_info["item"].get("item_id")
            , "제목": room_info["item"].get("title")
            , "주소": (
                  room_info["item"].get("local1"), room_info["item"].get("local2"), room_info["item"].get("local3"),
                  room_info["item"].get("local4"))
            , "정보": {
                  "사진": room_info["item"].get("images")
                  , "전세/월세": room_info["item"].get("sales_type")
                  , "방": room_info["item"].get("service_type")
                  , "층수": "{}/{}".format(room_info["item"].get("floor"), room_info["item"].get("floor_all"))
                  , "경도": random.uniform(37.48943270000667, 40.48943270000667)
                  , "위도": random.uniform(126.92405971657081, 140.92405971657081)
            }
            , "비용": {
                  "관리비": room_info["item"].get("manage_cost")
                  , "보증금액": room_info["item"].get("보증금액")
                  , "월세금액": room_info["item"].get("월세금액")
            }
            , "면적": {
                  "공급면적_m2": room_info["item"].get("공급면적_m2")
                  , "대지권면적_m2": room_info["item"].get("대지권면적_m2")
                  , "전용면적_m2": room_info["item"].get("전용면적_m2")
            }
            , "중개사": room_info["agent"].get("owner")
      }
      return parsed_data

# 지하철 정보 수집
subway_name = '신림역'
subway_id = getSubwayId(subway_name)
file_path = "./test.json"

if subway_id is not None:
      
      # 매물 목록 수집 요청
      room_list = getRoomList(subway_id)  # 수유역=96
      
      for room_id in room_list:
            # 매물 상세 정보 수집 요청
            room_info = getRoomInfo(room_id)
            
            # 매물 상세정보를 입맞대로 파싱
            parend_room_info = parseRoomInfo(room_info, '대출')
            
            if parend_room_info is not None:
                  with open(file_path, 'a+', encoding='utf-8') as file:
                        json.dump(parend_room_info, file, ensure_ascii=False)
                        json.dump(",", file, ensure_ascii=False)
      
      
      else:
            print("{}을 찾을 수 없습니다. {}".format(subway_name, subway_id))
