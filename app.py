from userinterface import CommandLineInterface
from confighandler import ConfigHandler
import argparse
import jobhandler 



class Hub():

    def __init__(self, config_file_path):
        
        self.job_handler = jobhandler.JobHandler()
        
    def get_job_types(self):
        return self.job_handler.get_job_types()
        
 
def run(config_file_path):
    hub = Hub(config_file_path)
    client = CommandLineInterface(hub)

 
#entry point into program when called from terminal window  
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take an input file and farm out ten reps')
    parser.add_argument('-c', '--config', required=False, default="", help="Path to config file")
    args = parser.parse_args()
    run(args.config)
    
