import json

""" coursefile = open('CourseData.json', 'r', encoding='utf8')
courses=json.loads(coursefile.read())
for course in courses:
    print(course['教师']) """

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

""" def get_course_meta(id:str):
    url=URL['QUERYURL'].format(id)
    r=requests.post(url=url,headers=HEADERS)
    courses=r.json()["results"]
    data={}
    for course in courses:
        data[course["properties"]["课程名称"]["title"][0]["text"]["content"]]={
            'id':course['id'],
            'CourseSN':course["properties"]["课程序号"]["rich_text"][0]["text"]["content"],
            'CourseCode':course["properties"]["课程代码"]["rich_text"][0]["text"]["content"]
        }
    return data

d=get_course_meta(ID['COURSEDB'])

with open('CourseDB.json', 'w', encoding='utf8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4) """

timetablefile = open('TimeTable.json', 'r', encoding='utf8')
timetable=json.loads(timetablefile.read())

    