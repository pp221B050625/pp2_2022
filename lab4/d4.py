from datetime import datetime,timedelta
date1 = datetime.now()
date2 = datetime(2022,5, 10, 10, 0,0)
diff = date2 - date1
sec = diff.total_seconds()
print(sec)