# 向课程数据库添加课程信息
TOKEN = "secret_S72Il30H84e2ewcYZ8iltKmLxizTy75yJieumiBHq9o"
ID = {'CALENDERDB':'568d78248f6a4807a26b2fd7bdeeeaaf','COURSEDB':'0727681c69a74efa966b424e254c9bef'}
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

""" querypage_database(ID['CALENDERDB']) """

coursefile = open('CourseData.json', 'r', encoding='utf8')
courses=json.loads(coursefile.read())
for course in courses:
    page={
    "parent": {
            "type": "database_id",
            "database_id": ID['COURSEDB']
        },
    "properties": {
        "课程序号": {"rich_text": [{"text": {"content": course["课程序号"]}}]},
        "教师名称": {"rich_text": [{"text": {"content": course["教师"]}}]},
        "课程代码": {"rich_text": [{"text": {"content": course["课程代码"]}}]},
        "上课地点": {"rich_text": [{"text": {"content": course["上课地点"]}}]},
        "学分": {"rich_text": [{"text": {"content": course["学分"]}}]},
        "课程名称": {"title": [{"text": {"content": course["课程名称"]},"annotations": {"bold": True,"color": "orange"}}]},
            }        
}
    print(course['课程名称'])
    
    r = requests.post(url=URL['ADDURL'], json=page, headers=HEADERS)
    print(r.status_code)
    print(course["课程名称"])