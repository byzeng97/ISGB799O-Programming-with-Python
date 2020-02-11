# Group Project: Yating Wang, Xuejun Shen, Bingyue Zeng, Xin Sui
import pandas as pd
import csv

Display_all = 1
Search_last_name = 2
Search_graduating_year = 3
Program_summary = 4
Add_new_student = 5
Quit = 6


def main():
    print('Welcome to Student Query Tool')
    content = pd.read_csv("Students.txt", sep="\t")  # get student data
    choice = 0
    while choice != Quit:
        choice = get_user_choice()
        if choice == Display_all:
            display_all(content)
            print("----------------------------------------------------------------")
        elif choice == Search_last_name:
            search_last_name(content)
            print("----------------------------------------------------------------")
        elif choice == Search_graduating_year:
            search_graduating_year(content)
            print("----------------------------------------------------------------")
        elif choice == Program_summary:
            program_summary(content)
            print("----------------------------------------------------------------")
        elif choice == Add_new_student:
            add_new_student(content)
            print("----------------------------------------------------------------")
        elif choice == Quit:
            print('Thank you for using our system! Bye.')


def get_user_choice():
    print('1. Display all student records')
    print('2. Display students whose last name begins with a certain string(case insensitive)')
    print('3. Display all records for students whose graduating year is a certain year')
    print('4. Display a summary report of each program for students graduating on/after a certain year')
    print('5. Add a new student record to the system')
    print('6. Quit')
    temp_choice = input('Please enter your query code： ').strip()
    is_valid = False
    choice = None
    while not is_valid:
        is_valid, error_type = validate(temp_choice)
        if is_valid:
            choice = int(temp_choice)
        else:
            if error_type == 'OUTOFBOUND':
                temp_choice = input('Unsupported query code. Please re-enter your query code: ')
            elif error_type == 'NONDIGIT':
                temp_choice = input('Unsupported query format. Please re-enter numerical query code： ')
    return choice


def validate(input):  # input is a tring which potentially represents a number
    if input.isdigit():
        if 1 <= int(input) <= 6:
            return True, 'NONE'
        else:
            return False, 'OUTOFBOUND'
    else:
        return False, 'NONDIGIT'


def display_all(InfoBook):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    print(InfoBook)


def search_last_name(InfoBook):
    lastname = input("Please enter certain beginning string of the Last name "
                     + "to start for searching for records:").strip()
    lastname = lastname.strip().capitalize()  # strip off leading and trailing spaces including tabs and capitalize and unify the user input

    if InfoBook['Last'].str.contains(lastname).any():
        print("------------------------------------------------------------------")
        print("Here is the students' records start with " + lastname + " : ")
        print(InfoBook[InfoBook['Last'].str.contains(lastname)])

    else:
        print("No Record Found")


def search_graduating_year(InfoBook):
    ylist = InfoBook['GradYear'].tolist()
    year = input("Please enter the graduate year:").strip()
    while not year.isdigit():
        year = input("Non numerical input. Please re-enter the graduate year:").strip()
    year = int(year)
    if year in ylist:
        print("--------------------------------------------------------------------")
        print(f"Here are the students' records with graduate year in {year} : ")
        print(InfoBook[InfoBook['GradYear'] == year])
    else:
        print(f"No matching records found for year： {year}")

def program_summary(InfoBook):
    gradYear = input("Which year are you expecting students to graduate on/after?: ").strip()
    while not gradYear.isdigit():
        gradYear = input("Invalid input. Please re-enter the graduation year: ").strip()
    gradYear = int(gradYear)
    option = input("Do you want to generate report for students graduating on or after this certain year?(On or After): ").strip().lower()
    while option != 'on' and option != 'after':
        option = input(
            "Unsupported option. Please answer again using On or After: ").strip().lower()
    years = InfoBook.GradYear.unique().tolist()
    years.sort()
    if option == 'on':
        if gradYear not in years:
            print(f'No matching record found for students graduating ON year： {gradYear}')
        else:
            print(f'Program report for students graduating ON year： {gradYear}')
            matching_records = InfoBook[InfoBook['GradYear'] == gradYear]
            total_num = len(matching_records['ID'].tolist())
            for program in matching_records['DegreeProgram'].unique().tolist():
                student_in_program = len(InfoBook[(InfoBook['GradYear'] == gradYear) & (InfoBook['DegreeProgram'] == program)]['ID'].tolist())
                print_student_number_and_percent(program, student_in_program, total_num)
    else:
        matching_years = list(filter(lambda yr: yr > gradYear, years))
        if len(matching_years) < 1:
            print(f'No matching record found for students graduating AFTER year: {gradYear}')
        else:
            print(f'Program report for students graduating AFTER year： {gradYear}')
            matching_records = InfoBook[InfoBook['GradYear'] > gradYear]
            total_num = len(matching_records['ID'].tolist())
            for program in matching_records['DegreeProgram'].unique().tolist():
                student_in_program = len(
                    InfoBook[(InfoBook['GradYear'] > gradYear) & (InfoBook['DegreeProgram'] == program)][
                        'ID'].tolist())
                print_student_number_and_percent(program, student_in_program, total_num)

def print_student_number_and_percent(program, studentNum, totalNum):
    print(f'There are {studentNum} students graduating in {program} and takes {studentNum/totalNum} percent of the total.')

def add_new_student(InfoBook):
    existing_ids = InfoBook['ID'].tolist()
    newid = input('Please enter ID:').strip()
    is_valid_id = False
    while not is_valid_id:
        error_type = 'NONE'
        if not newid.isdigit():
            is_valid_id = False
            error_type = 'NONDIGIT'
        elif int(newid) in existing_ids:
            is_valid_id = False
            error_type = 'DUPLICATE'
        else:
            is_valid_id = True
            error_type = 'NONE'

        if not is_valid_id:
            if error_type == 'NONDIGIT':
                newid = input('Unsupported ID format. Please re-enter numerical ID:')
            elif error_type == 'DUPLICATE':
                newid = input('This ID already exists. Please re-enter ID:')

    newFirstname = input('Please enter First Name:').strip().capitalize()
    newlastname = input('Please enter Last Name:').strip().capitalize()
    newgrad = input('Please enter Graduation Year:').strip()
    newterm = input('Please enter Graduation Term:').strip().capitalize()
    newdp = input('Please enter Degree Program:').strip()
    print('Below is the new record: ')
    print(f'Student ID: {newid}')
    print(f'First Name: {newFirstname}')
    print(f'Last Name: {newlastname}')
    print(f'Graduation Year: {newgrad}')
    print(f'Graduation Term: {newterm}')
    print(f'Degree Program: {newdp}')
    req = input('Are you sure you want to add this record to the system?(yes/no):').strip()
    if req.lower() == "no":
        print("Adding new student record operation canceled.")
        return
    newindex = str(len(InfoBook))
    InfoBook.loc[newindex] = [int(newid), newFirstname, newlastname, newgrad, newterm, newdp]
    InfoBook.to_csv("Students.txt", index=False, sep="\t", quoting=csv.QUOTE_NONE)
    req = input('Record added successfully. Do you want to see the result?(yes/no):').strip()
    if req.lower() == 'yes':
        display_all(InfoBook)


main()
