import csv


def register_user(filename):
    """
    Registers a user for an after-school club.
    It asks inputs for First Name, Last Name, Gender, Form
    and stores in a csv file (append mode will create the file if it doesn't exist)
    :param filename: The full path and name of the file to save the user registration
    :return:
    """
    # Ask the user for their details (all inputs are mandatory)
    first_name = mandatory_input("First Name")
    last_name = mandatory_input("Last Name")
    gender = mandatory_input("Gender (M/F)")
    form = mandatory_input("Form")

    # Open a file to store the user's details in CSV format (append mode)
    with open(filename, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([first_name, last_name, gender, form])

    # Print a success message
    print(f"Thank you {first_name} {last_name}. You have successfully registered for the after-school club")


def mandatory_input(input_key):
    """
    Keeps asking for the input until provided (i.e. not an empty string)
    :param input_key: The name of the value being requested, i.e. Last Name
    :return: The inputted value
    """
    while True:
        input_value = input(f"Enter your {input_key}: ")
        if input_value != "":
            return input_value
        else:
            print(f"Please enter your {input_key}.")


register_user("club_register.csv")
