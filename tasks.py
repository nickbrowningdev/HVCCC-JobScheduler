from config import huey
import time


@huey.task()
def startjob(word,amount,wait):
    x = 0
    while x < amount:
        print(word)
        time.sleep(wait)
        x += 1


