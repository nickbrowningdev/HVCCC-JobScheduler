from huey.signals import SIGNAL_COMPLETE, SIGNAL_ERROR
import os
from huey import SqliteHuey

huey = SqliteHuey('main')



##startup_consumer():
##shutdown_consumer():
##force_shutdown_consumer():

##How to pass/set a task name for each individual task rather than a common name

##Also check create_rep_folder_and_files in jobreader for questions on railUtilisation




#Methods in this file are used to access the huey queue.
@huey.signal(SIGNAL_COMPLETE)
def task_completed(signal, task):
    print('%s - %s - %s' % (signal, task.name, task))
    print('task was completed.')
    

@huey.signal(SIGNAL_ERROR)
def task_error(signal, task, exc=None):
    print('%s - %s' % (signal, task.name))
    print('task error.')


    
    


@huey.task(name='Simulation Job')
def queue_simulation_job(releaseFolderLocation, subfolder, folder, seedList):
        for i in seedList:
            seed = eval(i)
            run_simulation_job(releaseFolderLocation, subfolder, folder, seed)


@huey.task(name='Postprocessing Job')
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


def show_jobs_in_queue():
    jobs = huey.pending()
    for i in jobs:
        print(i)
        print('Priority= ' + str(i.priority))



    



   

