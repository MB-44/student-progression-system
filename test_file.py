from graphics import *

print("Student test record")

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

    progress_rect.setFill("green")
    retriever_rect.setFill("pink")
    trailer_rect.setFill("blue")
    exclude_rect.setFill("yellow")

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

def credit_input():
    while True:
        try:           
            pass_credit = int(input("Please enter your credits at pass: "))
            if pass_credit not in range(0,121,20):
                print("Out of range")
                continue

            defer_credit = int(input("Please enter your credits at defer: "))
            if defer_credit not in range(0,121,20):
                print("Out of range")
                continue
        
            fail_credit = int(input("Please enter your credits at fail: "))
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
        pass_credit , defer_credit , fail_credit = credit_input()

        if pass_credit == 120:
            output = "Progress"
            progress_count += 1

        elif (pass_credit+defer_credit) < fail_credit:
            output = "Exclude"
            exclude_count += 1

        elif pass_credit == 100 and (defer_credit==20 or fail_credit==20):
            output = "Trailer"
            trailer_count += 1

        elif (pass_credit in [0,20,40,60,80]) and (defer_credit in [0,20,40,60,80,100,120]) and (fail_credit in [0,20,40,60]):
            output = "Retriever"
            retriever_count += 1

        print(output)

        if type == "STUDENT":
            return
        
        result = f"{output} : {pass_credit}, {defer_credit} {fail_credit}"
        data_list.append(result)

        next_round = input("Would you like to enter another set of data (y to continue / q to quit)? ").strip()
        if next_round == "q":
            break
    
    histogram(progress_count, retriever_count, trailer_count, exclude_count)

data_list = []

def student_version(type):
    credit_marks(type)

def staff_version(data_list):
    credit_marks()
    stored_data(data_list)
    write_in_file(data_list)

# part 02
def stored_data(data_list):
    print()
    print("Part 02")
    for data in data_list:
        print(data)

# part 03
def write_in_file(data_list):
    with open("data_file.txt","w") as file:
        for data in data_list:
            file.write(data+"\n")
    
    print()
    print("Part 03")
    with open("data_file.txt","r") as file: 
        lines = file.readlines()
        for line in lines:
            print(line.strip())

user_type = input("Student or Staff (1 for Student / 2 for Staff)  : ").strip()
if user_type == "1":
    student_version("STUDENT")
elif user_type =="2" :
    staff_version(data_list)

