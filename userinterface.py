# Nick's stuff to be refactored into class and go in here

import job
import queuemanager
import jobhandler

class CommandLineInterface():

    def __init__(self, hub):
        self.hub = hub
        self.run_main_loop()
        
    def validate_user_choice(self, valid_choices, user_input):
        if user_input in valid_choices:
            return True
        else:
            print()
            print(f'{user_input} is not a valid option.')
            return False
    
    
    def get_user_input(self, user_instruction, option_ids, option_descriptions):
        """
        Displays a menu to user.
        
        Parameters
        ----------
        user_instruction : str
            This is the message to display to the user
        option_ids : iterable of strings
            A list of ids, which the user will use to identify their choice
        option_descriptions: iterable of strings
            A list of descriptions, which describe the choices
        """
        valid_choice = False
        while not valid_choice:
            print()
            print(user_instruction)
            print()
            for id, desc in zip(option_ids, option_descriptions):
                print(f'{id} : {desc}')
            print('quit : exit the application.')
            print()
            user_input = input("> ")
            valid_choice = self.validate_user_choice(list(option_ids) + ['quit'], user_input)
        if user_input == 'quit':
            return False
        return user_input

    def submit_seeds(self):
        seeds = input("Enter seeds (for example - 1,1,0): ")
        return seeds

    def submit_scenario(self):
        scenario = input("Enter scenario (for example - scenario1 or scenario2): ")
        return scenario
    
    def example_top_menu(self):
        def handle_choice_X():
            #do stuff
            print("Submitting Simulation Job")
            seeds = self.submit_seeds()
            scenario = self.submit_scenario()
            self.hub.submit_simulation_job(seeds, scenario)
            return True
            
        def handle_choice_Y():
            #do stuff
            print("Submitting Post-processing Job")
            seeds = self.submit_seeds()
            scenario = self.submit_scenario()
            self.hub.submit_postprocessing_job(seeds, scenario)
            return True

        def handle_choice_Z():
            #do stuff
            print("Submitting Simulation with Post-processing Job")
            seeds = self.submit_seeds()
            scenario = self.submit_scenario()
            self.hub.submit_simulation_with_postprocessing_job(seeds, scenario)
            return True
            
        instruction = "Please enter an option from this example menu"
        example_options = {  #using dictionary to map option ids to option descriptions
            "X": "Submit Simulation Job",
            "Y": "Submit Post-processing Job",
            "Z": "Submit Simulation with Post-processing Job",
        }
        user_input = self.get_user_input(instruction, example_options.keys(), example_options.values())
        if user_input is False:  #this is case when user wants to quit
            return False
        else:
            choice_function = {  #maps user's choice to an action, may be nested function or normal function
                "X": handle_choice_X,  
                "Y": handle_choice_Y,
                "Z": handle_choice_Z,
            }
            _continue = choice_function[user_input]() #execute chosen action
            return _continue
    
    def job_menu(self):
        job_types = self.hub.get_job_types()
        #etc
        
    def top_menu(self):
        pass
        
    def run_main_loop(self):
        _continue = True
        while _continue:
            _continue = self.example_top_menu()