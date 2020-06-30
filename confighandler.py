# I must confess I have no idea what config parameters we need yet - probably stuff related to client server architecture, as a start

class ConfigHandler():

    def __init__(self):
        #maybe ConfigHandler instance will need Hub instance passed in as parameter, so it can call functions on it.
        self.set_default_parameters()
        pass
        
    def set_default_parameters(self):
        #self.parameter_A = default_value etc
        pass
            
    def read_config(self, config_file_path):
        #read config file
        #set parameters accordingly
        pass
        
    def get_parameter_A(self):
        #return self.parameter_A
        pass