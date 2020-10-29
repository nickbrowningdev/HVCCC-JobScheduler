from lxml import etree
import subprocess
import argparse
import shutil
import datetime
import copy
import os
import sys
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import job
import queuemanager


#J1 = SimulationWithPostprocessingJob()
#simulation_job_data(J1, r"C:\Users\enjib\Desktop\ewocc_demo_v48.3", r"C:\Users\enjib\Desktop\ewocc_demo_v48.3\Inputs\scenario1.xml")
#set_seeds(J1,'1,1,0')
#start_simulation_with_postprocessing_job(J1)


class JobHandler():

    def __init__(self):
        pass
    
    def get_job_types(self):
        return job.get_job_types()




#The following functions are used to set data for specific tasks.

def simulation_job_data(task, releaseFolderLocation, inputFileLocation): 
    #Used to set nessasary params for a Simulation job to be completed.
    #Simulation jobs may also have singluar params set via the set_'param' methods.
    task.set_releasefolderlocation(releaseFolderLocation)
    task.set_inputfilelocation(inputFileLocation)


def postprocessing_job_data(task, releaseFolderLocation, outputFolderLocation): 
    #Used to set nessasary params for a Postprocessing job to be completed.
    #Postprocessing jobs may also have singluar params set via the set_'param' methods.
    task.set_releasefolderlocation(releaseFolderLocation)
    task.set_outputfolderlocation(outputFolderLocation)


def set_seeds(task, seeds): 
    #Sets seeds list, input should be a string. Inputs can be as follows:
    #('First seed, Last seed, 0')  0 as last seed creates a loop from first to last.
    #('First seed, Last seed, Step, 0')   0 as last seed creates a loop from first to last. Stepping through by step seed amount.
    #('First seed, Second seed, Third seed, .....')  Can enter as many seeds as you like.

    seeds = seeds.split(',')
    seedList = []
    lastSeed = eval(seeds[len(seeds)-1])
    if (len(seeds) == 4) and (lastSeed == 0):
        start = eval(seeds[0])
        stop = eval(seeds[1])
        step = eval(seeds[2])
        for x in range(start,stop+1,step):
            xList = str(x)
            seedList.append(xList)
        task.set_seeds(seedList)
    elif (len(seeds) == 3) and (lastSeed == 0):
        start = eval(seeds[0])
        stop = eval(seeds[1])
        for x in range(start,stop+1):
            xList = str(x)
            seedList.append(xList)
        task.set_seeds(seedList)
    else:
         task.set_seeds(seeds)




#The following functions are used to send tasks to the queueing functions with the right params.


def start_simulation_job(task):
    #Queues up just the Simulation jobs to be completed using the jobs paramameters.
    releaseFolderLocation = task.releasefolderlocation
    seedList = task.seeds
    p = get_priority(task)
    subfolder = create_rep_folder_and_files(task)
    pathName, folderName = os.path.split(subfolder)
    queuemanager.queue_simulation_job(releaseFolderLocation, subfolder, folderName, seedList, priority=p)



def start_postprocessing_job(task):
    #Queues up just the Postproccesing jobs to be completed using the jobs paramameters.
    releaseFolderLocation = task.releasefolderlocation
    outputFolderLocation = task.outputfolderlocation
    seedList = task.seeds
    p = get_priority(task)
    queuemanager.queue_postprocessing_job(releaseFolderLocation, outputFolderLocation, seedList, priority=p)



def start_simulation_with_postprocessing_job(task):
    releaseFolderLocation = task.releasefolderlocation
    inputFile = task.inputfilelocation
    seedList = task.seeds
    allSimsFirst = task.allsimsfirst
    p = get_priority(task)
    subfolder = create_rep_folder_and_files(task)
    pathName, folderName = os.path.split(subfolder)
    scenarioName = get_output_folder(inputFile) 
    if task.outputfolderlocation == None:
        scenarioName = get_output_folder(inputFile) 
        outputFolderLocation = os.path.join(releaseFolderLocation, 'Outputs', scenarioName)
    else:
        outputFolderLocation = task.outputfolderlocation
    queuemanager.queue_simulation_with_postprocessing_job(releaseFolderLocation, subfolder, folderName, outputFolderLocation, allSimsFirst, seedList, priority=p)
     







#The following functions are used to create output folders and input files for number of seeds.

def create_output_folders(task, seed):
    outputLocation = task.outputfolderlocation
    folderSeed = str(seed)
    subfolder = os.path.join(outputLocation, folderSeed)
    if os.path.isdir(subfolder):
        shutil.rmtree(subfolder)
    os.mkdir(subfolder)



def create_rep_folder_and_files(task):
    #Used to create temp folder for input files.
    inputFile = task.inputfilelocation
    seedList = task.seeds
    folder, fileName = os.path.split(inputFile)
    subfolderName = os.path.splitext(fileName)[0]
    subfolder = os.path.join(folder,  subfolderName)
    if os.path.isdir(subfolder):
        shutil.rmtree(subfolder)
    
    os.mkdir(subfolder)
    for i in seedList:
        #Used to create input file for each of the starting seeds.
        seed = eval(i)
        create_rep_files(subfolder, subfolderName, inputFile, seed)
    
    return subfolder



def create_rep_files(folder, fileName, originalFile, num_rep):
    #Used to create input file for each of the starting seeds.
    try:
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(originalFile, parser)
        root = tree.getroot()


        for rep in range(num_rep, num_rep + 1):
            for par in root.find("runParameters").findall("runParameter"):
                parName = par.attrib["name"]
                if parName == "replications":
                    par.set("value", "1")
                elif parName == "startingSeed":
                    par.set("value", str(rep))

            outFileName = os.path.join(folder, fileName + "_" + str(rep) + ".xml")

            with open(outFileName, 'w') as fl:
                tree.write(outFileName, pretty_print=True, xml_declaration=True,   encoding="utf-8")

    except IOError:
        print("Error found when trying to read file",originalFile," ....\n")
        print("*** Ending script, no outputs generated ***\n")
        sys.exit(1)








#The following functions are used to get specific params.


def get_output_folder(originalFile):

    try:
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(originalFile, parser)
        root = tree.getroot()

        for par in root.find("runParameters").findall("runParameter"):
            parName = par.attrib["name"]
            if parName == "scenarioID":
                scenarioName = par.get("value")
                return scenarioName

    
    except IOError:
        print("Error found when trying to read file",originalFile," ....\n")
        print("*** Ending script, no outputs generated ***\n")
        sys.exit(1)




def get_priority(task): 
    if task.priority == None:
        p=0
    else:
        p=task.priority
    return p



def print_seeds(task): 
    #Used to test seed list input.

    seedList = task.seeds
    for i in seedList:
        seed = eval(i)
        print(seed)