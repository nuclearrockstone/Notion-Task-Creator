TOKEN = "secret_S72Il30H84e2ewcYZ8iltKmLxizTy75yJieumiBHq9o"
ID = {'CALENDERDB':'568d78248f6a4807a26b2fd7bdeeeaaf'}
URL = {'QUERYURL':'https://api.notion.com/v1/databases/{}/query','ADDURL':'https://api.notion.com/v1/pages'}
import requests
import json
import time

HEADERS = {
    "Authorization": TOKEN,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}

#Notion数据库中的“一条数据”在API中被视为一个Page

def querypage_database(id:str):
    url=URL['QUERYURL'].format(id)
    r=requests.post(url=url,headers=HEADERS)
    with open('QueryDB.json', 'w', encoding='utf8') as f:
        json.dump(r.json(), f, ensure_ascii=False, indent=4)
    return 0

querypage_database(ID['CALENDERDB'])

page={
    "parent": {
            "type": "database_id",
            "database_id": ID['CALENDERDB']
        },
    "properties": {
        "课程序号": {"rich_text": [{"text": {"content": "11111"},"annotations": {"bold": True,}}]},
        "教师": {"rich_text": [{"text": {"content": "Notion"},"annotations": {"bold": True,"color": "orange"}}]},
        "上课时间": {"date": {"start": "2024-03-03T00:00:00.000+08:00","end": "2024-03-03T04:00:00.000+08:00"}},
        "课程代码": {"rich_text": [{"text": {"content": "11111"},"annotations": {"bold": True,}}]},
        "上课地点": {"rich_text": [{"text": {"content": "22教"},"annotations": {"bold": True,}}]},
        "是否到课": {"checkbox": True},
        "学分": {"rich_text": [{"text": {"content": "1"},"annotations": {"bold": True,}}]},
        "课程名称": {"title": [{"text": {"content": "Python"},"annotations": {"bold": True,"color": "orange"}}]},
        "WeekCode": {"multi_select": [{"name": "1"},{"name": "2"}]},
        "🏢 课程列表": {"relation": [{"id": "Python-c5168e829845422fafe57a1273fefe82"}]}
            }        
}

""" r = requests.post(url=URL['ADDURL'], json=page, headers=HEADERS)

print(r.text) """