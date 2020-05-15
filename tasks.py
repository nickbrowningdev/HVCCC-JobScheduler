from config import huey
import time
import os


@huey.task()
def startJob(word,amount,wait):
    x = 0
    while x < amount:
        print(word)
        time.sleep(wait)
        x += 1



@huey.task()
def startJobBatch(file,word,amount,wait):
    os.system((file) + " " + (word) + " " + (amount) + " " + (wait))