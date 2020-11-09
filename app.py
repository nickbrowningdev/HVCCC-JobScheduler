from userinterface import CommandLineInterface
from confighandler import ConfigHandler
import argparse
import jobhandler 
from socket import AF_INET, socket, SOCK_STREAM
import queuemanager
import job

class Hub():
    def __init__(self, config_file_path):
        self.job_handler = jobhandler.JobHandler()
        
    def get_job_types(self):
        return self.job_handler.get_job_types()
        
    def submit_simulation_job(self, seeds, scenario):
        filepath1 = r"C:\Users\nbwre\Documents\HVCCC\ewocc_demo_v48.3"
        filepath2 = r"C:\Users\nbwre\Documents\HVCCC\ewocc_demo_v48.3\Inputs" + "\\" + scenario + ".xml"

        J1 = job.SimulationJob()
        jobhandler.simulation_job_data(J1, filepath1, filepath2)
        jobhandler.set_seeds(J1,seeds)
        jobhandler.start_simulation_job(J1)

    def submit_postprocessing_job(self, seeds, scenario):
        filepath1 = r"C:\Users\nbwre\Documents\HVCCC\ewocc_demo_v48.3"
        filepath2 = r"C:\Users\nbwre\Documents\HVCCC\ewocc_demo_v48.3\Inputs" + "\\" + scenario + ".xml"
        
        J1 = job.PostprocessingJob()
        jobhandler.postprocessing_job_data(J1, filepath1, filepath2)
        jobhandler.set_seeds(J1,seeds)
        jobhandler.start_postprocessing_job(J1)

    def submit_simulation_with_postprocessing_job(self, seeds, scenario):
        filepath1 = r"C:\Users\nbwre\Documents\HVCCC\ewocc_demo_v48.3"
        filepath2 = r"C:\Users\nbwre\Documents\HVCCC\ewocc_demo_v48.3\Inputs" + "\\" + scenario + ".xml"
        
        J1 = job.SimulationWithPostprocessingJob()
        jobhandler.simulation_job_data(J1, filepath1, filepath2)
        jobhandler.set_seeds(J1,seeds)
        jobhandler.start_simulation_with_postprocessing_job(J1)

def run(config_file_path):
    queuemanager.startup_consumer()
    hub = Hub(config_file_path)
    client = CommandLineInterface(hub)
 
#entry point into program when called from terminal window  
if __name__ == "__main__":
    server_socket = socket(AF_INET, SOCK_STREAM)
    location = ("10.0.0.121", 5050)
    result_of_check = server_socket.connect_ex(location)

    if result_of_check == 0:
        print("HVCCC Server Ready")
        server_socket.close()

        parser = argparse.ArgumentParser(description='Take an input file and farm out ten reps')
        parser.add_argument('-c', '--config', required=False, default="", help="Path to config file")
        args = parser.parse_args()
        run(args.config)
    else:
        print("Error: HVCCC Server is Closed")
        server_socket.close()