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
    print('I have finished.')



@huey.task()
def startJobBatch(file,word,amount,wait):
    os.system((file) + " " + (word) + " " + (amount) + " " + (wait))






#Demo tasks

#  startJob('Hello', 5, 5)

#  startJobBatch('JobBatch.bat', 'Hi', '5', '10')

#  startJob('100', 2, 2, priority=100)
#  startJob('75', 2, 2, priority=75)
#  startJob('6', 2, 2, priority=6)

#  startJobBatch('JobBatch.bat', 'Batch100', '2', '2', priority=100)
#  startJobBatch('JobBatch.bat', 'Batch80', '2', '2', priority=80)
#  startJobBatch('JobBatch.bat', 'Batch5', '2', '2', priority=5)
