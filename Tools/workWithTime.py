import time
from datetime import datetime, timedelta
import time

# returns current date time as time stamp
# print(time.time())


def send_email():
    for i in range(10000):
        pass


START_TIME = time.time()
send_email()
END_TIME = time.time()
DURATION = END_TIME - START_TIME
print(DURATION)


# Date Time
CUSTOM_DATETIME = datetime(2018, 1, 1)
CURRENT_DATETIME = datetime.now()

# Format to specific format
TIME_TO_FORMAT = "2018/01/01"
datetime.strptime(TIME_TO_FORMAT, "%Y/%m/%d")
print(TIME_TO_FORMAT)

# -- Convert string to DateTime obj --

# Convert from TimeStamp
DATETIME_OBJ = datetime.fromtimestamp(time.time())
print(DATETIME_OBJ)
print(f"formatted year: {DATETIME_OBJ.year}")
print(f"formatted month: {DATETIME_OBJ.month}")

# Convert DateTime to string
DATETIME_STRING = DATETIME_OBJ.strftime("%Y/%m")
print(DATETIME_STRING)


# -- timedelta represents duration --

DT1 = datetime(2018, 1, 1)
DT2 = datetime.now()
DURATION = DT2 - DT1
print(DURATION)
print(DURATION.days)
print(DURATION.seconds)
