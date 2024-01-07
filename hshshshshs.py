#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20234054
# Date: 10/12/2023

from graphics import *

def histogram(progress_count, retriever_count, trailer_count, exclude_count):

    window = GraphWin("Histogram Results", 700, 500)

    title_label = Text(Point(150,35),"Histogram Result")
    title_label.setSize(15)
    title_label.setStyle("bold")
    title_label.draw(window)

    progress_rect = Rectangle(Point(50,420), Point(150,420 - progress_count * 10))
    retriever_rect = Rectangle(Point(200,420), Point(300,420 - retriever_count * 10))
    trailer_rect = Rectangle(Point(350,420), Point(450,420 - trailer_count * 10))
    exclude_rect = Rectangle(Point(500,420), Point(600,420 - exclude_count * 10))

    progress_rect.setFill("light green")
    retriever_rect.setFill("green")
    trailer_rect.setFill("yellow")
    exclude_rect.setFill("pink")

    progress_rect.draw(window)
    retriever_rect.draw(window)
    trailer_rect.draw(window)
    exclude_rect.draw(window)

    Text(Point(100,435), "Progress").draw(window)
    Text(Point(250,435), "Retriever").draw(window)
    Text(Point(400,435), "Trailer").draw(window)
    Text(Point(550,435), "Exclude").draw(window)

    Text(Point(100,475), f"Total Outcomes: {progress_count + trailer_count + retriever_count + exclude_count}").draw(window)

    window.getMouse()
    window.close()

def valid_credit_input():
    while True:
        try:           
            pass_credit = int(input("Please enter your credits at PASS: "))
            if pass_credit not in range(0,121,20):
                print("Out of range")
                continue

            defer_credit = int(input("Please enter your credits at DEFER: "))
            if defer_credit not in range(0,121,20):
                print("Out of range")
                continue
        
            fail_credit = int(input("Please enter your credits at FAIL: "))
            if fail_credit not in range(0,121,20):
                print("Out of range")
                continue

            if (pass_credit + defer_credit + fail_credit) != 120:
                print("Total incorrect")
                continue

        except ValueError:
            print("Interger required")
            continue

        credit_list = [pass_credit , defer_credit , fail_credit]
        return credit_list

def credit_marks(type=None):
    progress_count = 0
    exclude_count = 0
    trailer_count = 0
    retriever_count = 0

    while True:
        pass_credit , defer_credit , fail_credit = valid_credit_input()

        if pass_credit == 120:
            outcome = "Progress"
            progress_count += 1

        elif (pass_credit+defer_credit) < fail_credit:
            outcome = "Exclude"
            exclude_count += 1

        elif pass_credit == 100 and (defer_credit==20 or fail_credit==20):
            outcome = "Progress (module trailer)"
            trailer_count += 1

        elif (pass_credit in [0,20,40,60,80]) and (defer_credit in [0,20,40,60,80,100,120]) and (fail_credit in [0,20,40,60]):
            outcome = "Module retriever"
            retriever_count += 1

        print(outcome)

        if type == "STUDENT":
            return
        
        result = f"{outcome} : {pass_credit}, {defer_credit} {fail_credit}"
        outcome_list.append(result)

        need_to_continue = input("Would you like to enter another set of data (y to continue / q to quit)? ").strip()
        if need_to_continue == "q":
            break

    if type != "STUDENT":
        histogram(progress_count, retriever_count, trailer_count, exclude_count)

outcome_list = []

def student_outcome(type):
    credit_marks(type)

def modertor_outcome(data_list):
    credit_marks()
    store_in_list(data_list)
    store_in_file(data_list)

def store_in_list(outcome_list):
    print()
    print("Part 02")
    for data in outcome_list:
        print(data)

def store_in_file(outcome_list):
    with open("progression_data.txt","w") as file:
        for data in outcome_list:
            file.write(data+"\n")
    
    print()
    print("Part 03")
    with open("progression_data.txt","r") as file: 
        linesOfData = file.readlines()
        for eachLine in linesOfData:
            print(eachLine.strip())

user_type = input("Student or Staff ('s' for Student / 'm' for Moderator)  : ").strip()

if user_type.lower() == "s":
    student_outcome("STUDENT")

elif user_type.lower() =="m" :
    modertor_outcome(outcome_list)#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20234054
# Date: 10/12/2023

from graphics import *

def histogram(progress_count, retriever_count, trailer_count, exclude_count):

    window = GraphWin("Histogram Results", 700, 500)

    title_label = Text(Point(150,35),"Histogram Result")
    title_label.setSize(15)
    title_label.setStyle("bold")
    title_label.draw(window)

    progress_rect = Rectangle(Point(50,420), Point(150,420 - progress_count * 10))
    retriever_rect = Rectangle(Point(200,420), Point(300,420 - retriever_count * 10))
    trailer_rect = Rectangle(Point(350,420), Point(450,420 - trailer_count * 10))
    exclude_rect = Rectangle(Point(500,420), Point(600,420 - exclude_count * 10))

    progress_rect.setFill("light green")
    retriever_rect.setFill("green")
    trailer_rect.setFill("yellow")
    exclude_rect.setFill("pink")

    progress_rect.draw(window)
    retriever_rect.draw(window)
    trailer_rect.draw(window)
    exclude_rect.draw(window)

    Text(Point(100,435), "Progress").draw(window)
    Text(Point(250,435), "Retriever").draw(window)
    Text(Point(400,435), "Trailer").draw(window)
    Text(Point(550,435), "Exclude").draw(window)

    Text(Point(100,475), f"Total Outcomes: {progress_count + trailer_count + retriever_count + exclude_count}").draw(window)

    window.getMouse()
    window.close()

def valid_credit_input():
    while True:
        try:
            pass_credit = int(input("Please enter your credits at PASS: "))
            if pass_credit not in range(0,121,20):
                print("Out of range")
                continue

            defer_credit = int(input("Please enter your credits at DEFER: "))
            if defer_credit not in range(0,121,20):
                print("Out of range")
                continue
        
            fail_credit = int(input("Please enter your credits at FAIL: "))
            if fail_credit not in range(0,121,20):
                print("Out of range")
                continue

            if (pass_credit + defer_credit + fail_credit) != 120:
                print("Total incorrect")
                continue

        except ValueError:
            print("Interger required")
            continue

        credit_list = [pass_credit , defer_credit , fail_credit]
        return credit_list

def credit_marks(type=None): # type = None / type = "STUDENT"
    progress_count = 0
    exclude_count = 0
    trailer_count = 0
    retriever_count = 0

    while True: 
        pass_credit , defer_credit , fail_credit = valid_credit_input()

        if pass_credit == 120:
            outcome = "Progress"
            progress_count += 1

        elif (pass_credit+defer_credit) < fail_credit:
            outcome = "Exclude"
            exclude_count += 1

        elif pass_credit == 100 and (defer_credit==20 or fail_credit==20):
            outcome = "Progress (module trailer)"
            trailer_count += 1

        elif (pass_credit in [0,20,40,60,80]) and (defer_credit in [0,20,40,60,80,100,120]) and (fail_credit in [0,20,40,60]):
            outcome = "Module retriever"
            retriever_count += 1

        print(outcome)

        if type == "STUDENT":
            return
        
        result = f"{outcome} : {pass_credit}, {defer_credit} {fail_credit}"
        outcome_list.append(result)

        need_to_continue = input("Would you like to enter another set of data (y to continue / q to quit)? ").strip()
        if need_to_continue == "q":
            break

    if type != "STUDENT":
        histogram(progress_count, retriever_count, trailer_count, exclude_count)

outcome_list = []

def student_outcome(type):
    credit_marks(type) # "STUDENT"

def modertor_outcome(data_list):
    credit_marks()
    store_in_list(data_list)
    store_in_file(data_list)

def store_in_list(outcome_list):
    print()
    print("Part 02")
    for data in outcome_list:
        print(data)

def store_in_file(outcome_list):
    with open("progression_data.txt","w") as file:
        for data in outcome_list:
            file.write(data+"\n")
    
    print()
    print("Part 03")
    with open("progression_data.txt","r") as file: 
        linesOfData = file.readlines()
        for eachLine in linesOfData:
            print(eachLine.strip())

user_type = input("Student or Staff ('s' for Student / 'm' for Moderator)  : ").strip()

if user_type.lower() == "s":
    student_outcome("STUDENT")

elif user_type.lower() =="m" :
    modertor_outcome(outcome_list)