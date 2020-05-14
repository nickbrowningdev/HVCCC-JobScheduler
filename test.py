from huey import SqliteHuey
import time


huey = SqliteHuey(filename='huey.db')




@huey.task()
def startjob(word,amount,wait):
    x = 0
    while x < amount:
        print(word)
        time.sleep(wait)
        x += 1


#@huey.task()
#def startJobBatch(word,amount,wait):

    