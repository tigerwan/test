
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

new_time = datetime.strptime(date_time, "%H:%M:%S %m/%d/%%Y")
print("new time:", new_time)


