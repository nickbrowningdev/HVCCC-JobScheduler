from config import huey
import time
import os
from job import *


#Huey... Used to queue jobs.

@huey.task()
def queueSim(releaseFolder, inputFile, seed):
    print(releaseFolder)
    print(inputFile)
    print(seed)
    #os.system((batchFile) +" "+  (inputFile))

@huey.task()
def queuePost(releasefolderlocation, outputfolderlocation, seed):
    print(releasefolderlocation)
    print(outputfolderlocation)
    print(seed)
    #os.system("Python " + (releasefolderlocation) + " -f " + (outputfolderlocation))





def dataSimulationJob(self, releasefolderlocation, inputfilelocation):
    self.set_releasefolderlocation(releasefolderlocation)
    self.set_inputfilelocation(inputfilelocation)

def queueSimJob(self):
    releaseFolder = self.releasefolderlocation
    inputFile = self.inputfilelocation
    seedList = self.seeds
    for i in seedList:
        seed = eval(i)
        queueSim(releaseFolder,inputFile, seed)



def dataPostJob(self, releasefolderlocation, outputfolderlocation): 
    self.set_releasefolderlocation(releasefolderlocation)
    self.set_outputfolderlocation(outputfolderlocation)
    
def queuePostJob(self):
    releasefolderlocation = self.releasefolderlocation
    outputfolderloaction = self.outputfolderlocation
    seedList = self.seeds
    for i in seedList:
        seed = eval(i)
        queuePost(releasefolderlocation, outputfolderloaction, seed)




def dataSimWithPostJob(self, releasefolderlocation, inputfileloaction, outputfolderlocation): 
    self.set_releasefolderlocation(releasefolderlocation)
    self.set_inputfilelocation(inputfileloaction)
    self.set_outputfolderlocation(outputfolderlocation)

def queueSimWithPostJob(self):
    releasefolderlocation = self.releasefolderlocation
    inputFile = self.inputfilelocation
    outputfolderloaction = self.outputfolderlocation
    seedList = self.seeds
    for i in seedList:
        seed = eval(i)
        queueSim(releasefolderlocation,inputFile, seed)
        queuePost(releasefolderlocation, outputfolderloaction, seed)



def dataSeeds(self, seeds):
    r = seeds
    seeds = r.split(',')
    seedList = []
    lastSeed = eval(seeds[len(seeds)-1])
    if (len(seeds) == 4) and (lastSeed == 0):
        start = eval(seeds[0])
        stop = eval(seeds[1])
        step = eval(seeds[2])
        for x in range(start,stop+1,step):
            xList = str(x)
            seedList.append(xList)
        self.set_seeds(seedList)
    elif (len(seeds) == 3) and (lastSeed == 0):
        start = eval(seeds[0])
        stop = eval(seeds[1])
        for x in range(start,stop+1):
            xList = str(x)
            seedList.append(xList)
        self.set_seeds(seedList)
    else:
         self.set_seeds(seeds)


def printSeeds(self):
    seedList = self.seeds
    for i in seedList:
        seed = eval(i)
        print(seed)

    