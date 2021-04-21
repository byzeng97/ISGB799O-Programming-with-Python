# Python Project 2019 Fall Fordham University 
A team project in Python course (ISGB7990 taught by Prof. Han)

SUMMARY

The overall goal of your SQT program is to read student records from a file, and let the user enter queries in order to see a detail or summary report. The project will need many of the topics covered in class.

PROGRAM INPUTS

The student input file has the following fields: Student ID #
Last name
First name
Graduating year (e.g, 2019)
Graduating term (Fall, Spring, Summer)
Degree program (e.g., MSBA, MBA, etc.)
This input file has a header record (a first line describing the fields in the file). Each field is separated by a tab. Example files to use (e.g, students.txt) will be posted on Blackboard.

PROGRAM PROCESSING

Your program should read each record of the file once into a data structure (e.g., list, dictionary). The program should keep the instance of the data in memory for the duration of the program, i.e., it should not re-read the data from the file for each user query.
Your program should allow queries to be entered, regarding the student list. Types of queries include: Display all student records
Display students whose last name begins with a certain string (case insensitive) Display all records for students whose graduating year is a certain year
Display a summary report of number and percent of students in each program, for students graduating on/after a certain year
The exact way to get user input and display the results will be decided by the group. The user interface should be via the console (screen and keyboard).
The program should anticipate and handle a number of potential errors related to user input or the file data.
Optionally, an additional functionality that you choose can be added to the system. However, groups should aim for a basic working system before enhancing it.

GRADING

All group members of the group will receive the same grade, which will be based on: Quality of the design
Quality of the code (including logic, error handling, commenting)
Ability to meet the requirements
Your final .py file(s) for the program as well as a “Read me” word document for basic instructions need to be submitted to BlackBoard.
