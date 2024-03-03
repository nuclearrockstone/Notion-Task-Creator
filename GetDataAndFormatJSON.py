#处理输入的课程数据并形成格式化数据
#定义如下参数
#course为课程
#lesson指单节课程

import json
from collections import defaultdict
import datetime
#导入单节课程信息
lessonfile = open('LessonData.json', 'r', encoding='utf8')
lessons=json.loads(lessonfile.read())["activities"]
lessonsalphadata=[]
#把所有课程的信息导入，以小节（45分钟）的形式导入JSON
for i in range(0,len(lessons)):
    lesson=lessons[i]
    if lesson!=[]:
        for q in range(0,len(lesson)):
            lessondic={}
            lessondic['CourseName']=lesson[q]['courseName']
            lessondic['TeacherName']=lesson[q]['teacherName']
            lessondic['ClassRoom']=lesson[q]['roomName']
            lessondic['CourseCode']=lesson[q]['courseId']
            lessondic['VaildWeek']=lesson[q]['vaildWeeks']
            lessondic['WeekCode']=(i+1)//12+1
            lessondic['DayCode']=(i+1)%12
            lessonsalphadata.append(lessondic)
            print(lesson[q]['courseName'])

with open('lessonsalphadata.json', 'w', encoding='utf8') as f:
    json.dump(lessonsalphadata, f, ensure_ascii=False, indent=4)

#将单节课程合并为大课
grouped_data = defaultdict(list)

for lesson in lessonsalphadata:
    # 使用(name, item)元组作为键
    key = (lesson["CourseName"], lesson["TeacherName"], lesson["ClassRoom"], lesson["CourseCode"], lesson["VaildWeek"], lesson["WeekCode"])
    grouped_data[key].append(lesson["DayCode"])

lessonbetadata=[{"CourseName":a,"TeacherName":b,"ClassRoom":c,"CourseCode":d,"VaildWeek":e,"WeekCode":f,"DayCode":g} for (a,b,c,d,e,f),g in grouped_data.items()]

with open('lessonbetadata.json', 'w', encoding='utf8') as f:
    json.dump(lessonbetadata, f, ensure_ascii=False, indent=4)