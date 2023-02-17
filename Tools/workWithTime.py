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
