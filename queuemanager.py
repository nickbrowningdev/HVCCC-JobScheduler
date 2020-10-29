from huey.signals import SIGNAL_COMPLETE, SIGNAL_ERROR
import os
from huey import SqliteHuey
import subprocess




huey = SqliteHuey('main')



#The following functions are used to startup/shutdown the Huey consumer console.

def startup_consumer():
    p = subprocess.Popen("huey_consumer queuemanager.huey", creationflags=subprocess.CREATE_NEW_CONSOLE)


##shutdown_consumer():
##force_shutdown_consumer():








#The following functions are used to give feedback on tasks in the queue.

@huey.signal(SIGNAL_COMPLETE)
def task_completed(signal, task):
    print('%s - %s - %s' % (signal, task.name, task))
    print('task was completed.')
    

@huey.signal(SIGNAL_ERROR)
def task_error(signal, task, exc=None):
    print('%s - %s' % (signal, task.name))
    print('task error.')


def show_jobs_in_queue():
    jobs = huey.pending()
    for i in jobs:
        print(i)
        print('Priority= ' + str(i.priority))

    




#The following functions are called by tasks in jobhandler and are used to put tasks in the queue.

@huey.task(name='Simulation Job') #Queue Simulation Jobs in the huey queue.
def queue_simulation_job(releaseFolderLocation, subfolder, folder, seedList):
        for i in seedList:
            seed = eval(i)
            run_simulation_job(releaseFolderLocation, subfolder, folder, seed)


@huey.task(name='Postprocessing Job')#Queue Postproccesing Jobs in the huey queue.
def queue_postprocessing_job(releaseFolderLocation, outputFolderLocation, seedList):
        for i in seedList:
            seed = eval(i)
            run_postprocessing_job(releaseFolderLocation, outputFolderLocation, seed)


@huey.task(name='Simulation with Postprocessing Job')#Queue Simulation/Postproccesing Jobs in the huey queue.
def queue_simulation_with_postprocessing_job(releaseFolderLocation, subfolder, folder, outputFolderLocation, allSimsFirst, seedList):
    if allSimsFirst == True:
        for i in seedList:
            seed = eval(i)
            run_simulation_job(releaseFolderLocation, subfolder, folder, seed)    
        for i in seedList:
            seed = eval(i)
            run_postprocessing_job(releaseFolderLocation, outputFolderLocation, seed)
    else:
        for i in seedList:
            seed = eval(i)
            run_simulation_job(releaseFolderLocation, subfolder, folder, seed) 
            run_postprocessing_job(releaseFolderLocation, outputFolderLocation, seed)

 

def run_simulation_job(releaseFolderLocation, subfolder, folder, seed):
    os.system((releaseFolderLocation + r"\Code\HVVCC\HVVCC_windows.bat") +" "+ (subfolder) + '\\' + (folder) + '_' + str(seed) + '.xml')

def run_postprocessing_job(releaseFolderLocation, outputFolderLocation, seed):
    os.system("Python " + (releaseFolderLocation + r"\LogReaders\processlogs_release.py") + " -f " + (outputFolderLocation) + '\\' + str(seed))






    



   

