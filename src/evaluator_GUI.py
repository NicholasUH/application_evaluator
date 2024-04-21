from fetch_criteria import fetch_criteria
from fetch_criterion import fetch_criterion
from application import Application
from evaluate_application import process_application
from status import Status
from dataclasses import fields

def list_available_criteria(path):
    print("Available criteria: ")
    for index, criteria in enumerate(fetch_criteria(path), start=1):
        print(index, " - ", criteria)

def get_criteria(user_criteria):
    criteria_list = fetch_criteria('src/criteria')
    return [criteria_list[i-1] for i in user_criteria if i >= 1 and i <= len(criteria_list)]

def validate_user_critiera_input(chosen_numbers):
    return not any(number < 1 or number > len(fetch_criteria('src/criteria')) for number in chosen_numbers)

def get_user_criteria_input():
    while True:
        try:
            user_input = input(("Enter the numbers of the criteria you want to use separated by spaces: ")).strip()
            chosen_numbers = list(map(int, user_input.split(' ')))
            
            if not validate_user_critiera_input(chosen_numbers):
                print("Please enter numbers between 1 and ", len(fetch_criteria('src/criteria')))
                continue

            return chosen_numbers
        
        except ValueError:
            print("Please enter only integers")

def validate_applicantion_info(prompt):
    while True:
        try:
            user_input = input(f'{prompt}: ').lower().strip()
            if user_input in ['true', 'false']:
                return user_input == 'true'
            
            raise ValueError
        except ValueError:
            print("Please enter only true or false")
    
def get_applicantion_info(chosen_critiera):
    print("Provide application details:")
    print("Enter 'true' or 'false' for each of the following: ")
    application_info = {}
    
    for field in fields(Application):
        application_info[field.name] = validate_applicantion_info(field.name)

    return application_info

def create_application(chosen_criteria):
    return Application(**get_applicantion_info(chosen_criteria))

def format_output(application):
    status, message = application
    print("Applicant passes. " + message) if status == Status.PASS else print("Applicant does not pass. " + message)

def continue_adding_applications():
    while True:
        try:
            user_input = input("Would you like to process another application? Please enter Yes or No: ").lower().strip()
            if user_input == 'yes':
                return True
            elif user_input == 'no':
                return False
            raise ValueError
        except ValueError:
            print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    list_available_criteria('src/criteria')
    chosen_criteria = get_criteria(get_user_criteria_input())
    chosen_criteria_functions = [fetch_criterion(criterion, 'criteria') for criterion in chosen_criteria]

    continue_getting_applications = True
    while continue_getting_applications:
        new_application = create_application(chosen_criteria)
        application_result = process_application(new_application, *chosen_criteria_functions)
        format_output(application_result)

        continue_getting_applications = continue_adding_applications()
