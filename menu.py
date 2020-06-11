import job

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
                menu_choice = int(input("Enter a choice [1 -2]: "))
                again = False

            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if menu_choice == 1:
            job.get_job_types()
            menu_loop = True
            
        elif menu_choice == 2:
            menu_loop = False
            break

        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")