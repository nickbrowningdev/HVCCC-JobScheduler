from abc import ABC, abstractmethod
from collections import namedtuple
import uuid
from queuemanager import *
from tasks import *

Param = namedtuple('param', ["type", "setter"])

class JobParams():
    
    def __init__(self):
        self.params = {}
        
    def add_param(self, name, param):
        self.params[name] = param
        
    def remove_param(self, name):
        del self.params[name]
        
    def get_params(self):
        return self.params
    
    def __iter__(self):
        for key,val in self.params.items():
            yield key, val
        

class Job(ABC):
 
    def __init__(self):
        if not hasattr(self, 'params'):
            self.params = JobParams()
            self.id = self.create_id()
        self.timestamp_submit = None
        self.priority = None
        self.creator = None
        super().__init__()
        self.add_param("Priority", Param(type=int, setter=self.set_priority))
    
    def create_id(self):
        id = uuid.uuid1()
        return id   #Added...
        
    def add_param(self, name, param):
        self.params.add_param(name, param)
    
    def remove_param(self, name):
        self.params.remove_param(name)
        
    def get_params(self):
        return self.params

    def set_priority(self, priority):
        self.priority = priority
  
 

class SimulationJob(Job):
    
    name = "Simulation Job"

    def __init__(self):
        self.releasefolderlocation = None
        self.inputfilelocation = None
        self.seeds = None
        self.job_name = "Ben"
        self.queue_task = huey.task()(queue_job)
        #self.queue_task = huey._registry.create_task(name=self.job_name)(queue_job)
        #self.queue_job = self.make_queue_job()
        super().__init__()
        self.add_param("Release folder location", Param(type=str, setter=self.set_releasefolderlocation))
        self.add_param("Input file location", Param(type=str, setter=self.set_inputfilelocation))
        self.add_param("Seeds", Param(type=str, setter=self.set_seeds))
        
    def set_releasefolderlocation(self, folderlocation):
        self.releasefolderlocation = folderlocation
        
    def set_inputfilelocation(self, filelocation):
        self.inputfilelocation = filelocation
    
    def set_seeds(self, seeds):
        self.seeds = seeds

    #@huey.task(name=self.name)
    #def queue_job(self):
       # print("Completing Job")


    #def make_queue_job(self):
        #@huey.task(name=self.name)
        #def queue_job(self):
        #return queue_job



class PythonScriptJob(Job):
    
    name = "Python Script Job"

    def __init__(self):
        self.scriptlocation = None
        self.scriptparamstring = None
        super().__init__()
        self.add_param("Script location", Param(type=str, setter=self.set_scriptlocation))
        self.add_param("Script parameters (as string)", Param(type=str, setter=self.set_scriptparamstring))

    def set_scriptlocation(self, scriptlocation):
        self.scriptlocation = scriptlocation

    def set_scriptparamstring(self, scriptparamstring):
        self.scriptparamstring = scriptparamstring
        

class PostprocessingJob(Job):

    name = "Postprocessing Job"

    def __init__(self):
        self.releasefolderlocation = None
        self.outputfolderlocation = None
        self.seeds = None
        self.activateraillog = False
        self.warmup = None
        super().__init__()
        self.add_param("Release folder location", Param(type=str, setter=self.set_releasefolderlocation))
        self.add_param("Output folder location", Param(type=str, setter=self.set_outputfolderlocation))
        self.add_param("Seeds", Param(type=str, setter=self.set_seeds))
        self.add_param("Activate Rail Log", Param(type=str, setter=self.set_activateraillog))
        self.add_param("Warmup value", Param(type=int, setter=self.set_warmup))
        
    def set_releasefolderlocation(self, folderlocation):
        self.releasefolderlocation = folderlocation
        
    def set_outputfolderlocation(self, folderlocation):
        self.outputfolderlocation = folderlocation
        
    def set_seeds(self, seeds):
        self.seeds = seeds
        
    def set_activateraillog(self, activateraillog):
        self.activateraillog = activateraillog
        
    def set_warmup(self, warmup):
        self.warmup = warmup

        
class SimulationWithPostprocessingJob(SimulationJob, PostprocessingJob):

    name = "Simulation with Postprocessing Job"

    def __init__(self):
        SimulationJob.__init__(self)
        PostprocessingJob.__init__(self)
        self.allsimsfirst = False
        self.add_param("All sims first", Param(type=bool, setter=self.set_allsimsfirst))
        #self.remove_param('Output folder location')
        
    def set_allsimsfirst(self, allsimsfirst):
        self.allsimsfirst = allsimsfirst

        
def get_job_types():
    return [SimulationJob, PostprocessingJob, SimulationWithPostprocessingJob]



