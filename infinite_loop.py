#무한 루프
import time

list = ["alex", "peter", "smith"]
i = 0

while True:
    print(list[i])
    i = (i+1)%3
    time.sleep(0.5)
