TOKEN = "secret_S72Il30H84e2ewcYZ8iltKmLxizTy75yJieumiBHq9o"
ID = {'CALENDERDB':'568d78248f6a4807a26b2fd7bdeeeaaf','COURSEDB':'0727681c69a74efa966b424e254c9bef'}
URL = {'QUERYURL':'https://api.notion.com/v1/databases/{}/query','ADDURL':'https://api.notion.com/v1/pages'}
import requests
import json
from datetime import datetime, timedelta

STARTDAY="2024-03-04"

HEADERS = {
    "Authorization": TOKEN,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}

#Notion数据库中的“一条数据”在API中被视为一个Page

def get_course_meta(id:str):
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

courses=get_course_meta(ID['COURSEDB'])

#导入课程日历
lessonfile = open('lessonbetadata.json', 'r', encoding='utf8')
lessons=json.loads(lessonfile.read())
#导入作息表
timetablefile = open('TimeTable.json', 'r', encoding='utf8')
timetable=json.loads(timetablefile.read())

for lesson in lessons:
    vaildweek=[char for char in lesson['VaildWeek']]
    for i in range(0,len(vaildweek)):
        
        if vaildweek[i]=='1':
            Delta=lesson['WeekCode']-1+i*7-7
            date=(datetime.strptime(STARTDAY, '%Y-%m-%d') + timedelta(days=Delta)).strftime('%Y-%m-%d')
            start=date+"T"+timetable[min(lesson['DayCode'])-1]['Start']+':00.000+08:00'
            end=date+"T"+timetable[max(lesson['DayCode'])-1]['End']+':00.000+08:00'
            daystring=",".join([str(num) for num in lesson["DayCode"]])
            page={
    "parent": {
            "type": "database_id",
            "database_id": ID['CALENDERDB']
        },
    "properties": {
        "课程序号": {"rich_text": [{"text": {"content": courses[lesson["CourseName"]]['CourseSN']}}]},
        "教师": {"rich_text": [{"text": {"content": lesson['TeacherName']}}]},
        "上课时间": {"date": {"start": start,"end": end}},
        "课程代码": {"rich_text": [{"text": {"content": courses[lesson["CourseName"]]['CourseCode']}}]},
        "上课地点": {"rich_text": [{"text": {"content": lesson['ClassRoom']}}]},
        "是否到课": {"checkbox": False},
        "学分": {"rich_text": [{"text": {"content": "1"}}]},
        "课程名称": {"title": [{"text": {"content": lesson["CourseName"]}}]},
        "WeekCode": {"rich_text": [{"text": {"content": str(lesson["WeekCode"])}}]},
        "DayCode": {"rich_text": [{"text": {"content":daystring }}]},
        "🏢 课程列表": {"relation": [{"id": courses[lesson["CourseName"]]['id']}]}
            }        
            
}
            r = requests.post(url=URL['ADDURL'], json=page, headers=HEADERS)
            print(r)
            print(lesson["CourseName"])