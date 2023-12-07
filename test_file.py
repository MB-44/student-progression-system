print("Student test record")

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
        credit_list = [pass_credit , defer_credit , fail_credit]
        return credit_list

def credit_marks():
    pass_credit , defer_credit , fail_credit = credit_input()
    
    if pass_credit == 120:
        output = "Progress"

    elif (pass_credit+defer_credit) < fail_credit:
        output = "Exclude"

    elif pass_credit == 100 and (defer_credit==20 or fail_credit==20):
        output = "Trailer"

    elif (pass_credit in [0,20,40,60,80]) and (defer_credit in [0,20,40,60,80,100,120]) and (fail_credit in [0,20,40,60]):
        output = "Retriever"
    print(output)

def student_version():
    credit_marks()


def staff_version():
    pass

user_type = input("Student or Staff (1 for Student / 2 for Staff)  : ").strip()
if user_type == "1":
    student_version()
elif user_type =="2" : 
    print("staff_version")