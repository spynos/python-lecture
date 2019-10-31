#무한 루프
import time

list = ["alex", "peter", "smith"]
i = 0

while True:
    i = i%3
    print(list[i])
    i = i+1
    time.sleep(0.5)
