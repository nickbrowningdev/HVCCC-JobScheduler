import job

def load_job_menu():
    print("What job would you like?")
    print("1. Simulation Job")
    print("2. Post-processing Job")
    print("3. Simulation with Post-processing Job")
    print("4. Return")

# returns job type
def return_job_type():
    job_menu_loop = True

    while job_menu_loop:

        # job type
        job_types = job.get_job_types()

        # displays job menu
        load_job_menu()

        # input catching
        # makes sure the menu choice is only an int
        again = True

        while again:
            try:
                # user makes a choice
                menu_choice = int(input("Enter a choice [1 - 4]: "))
                again = False

            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

            if menu_choice == 1:
                # gets a job type
                x = job_types[0]()

                params = x.get_params().get_params()

                params['Seeds'].setter([1, 2, 3])

                x.seeds

                for name, param in x.get_params():
                    print(name)
                    print(param)

                print(x.get_params())

                job_menu_loop = True
            
            elif menu_choice == 2:
                # gets a job type
                x = job_types[1]()
                
                params = x.get_params().get_params()

                params['Seeds'].setter([1, 2, 3])

                x.seeds

                for name, param in x.get_params():
                    print(name)
                    print(param)

                print(x.get_params())

                job_menu_loop = True

            elif menu_choice == 3:
                # gets a job type
                x = job_types[2]()
                
                params = x.get_params().get_params()

                params['Seeds'].setter([1, 2, 3])

                x.seeds

                for name, param in x.get_params():
                    print(name)
                    print(param)

                print(x.get_params())

                job_menu_loop = True

            elif menu_choice == 4:
                job_menu_loop = False
                break

            else:
                # any other input will print an error message
                print("Oops, Something went wrong!")
                print("Please Try Again!")

# displays menu
def load_menu():
    print(30 * "-" , "HVCCC" , 30 * "-")
    print("1. Create Job")
    print("2. Exit")
    print(67 * "-")

# gets menu choice
def display_menu():
    menu_loop = True

    while menu_loop:
        # displays menu
        load_menu()

        # input catching
        # makes sure the menu choice is only an int
        again = True

        while again:
            try:
                # user makes a choice
                menu_choice = int(input("Enter a choice [1 - 2]: "))
                again = False

            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if menu_choice == 1:
            # gets a job type
            return_job_type()          

            menu_loop = True
            
        elif menu_choice == 2:
            menu_loop = False
            break

        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

# for testing purposes
# display_menu()