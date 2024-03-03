from datetime import datetime, timedelta

STARTDAY="2024-03-04"
Delta=3*7+1
Dday=(datetime.strptime(STARTDAY, '%Y-%m-%d') + timedelta(days=Delta)).strftime('%Y-%m-%d')

print(Dday)