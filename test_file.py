print("student progression software")

def check_input():
    while True:
        try:
            pass_credit = int(input("Enter your credit at pass: "))
            defer_credit = int(input("Enter your credit at defer: "))
            fail_credit = int(input("Enter your credit at fail: "))

            for credit in [pass_credit,defer_credit,fail_credit]:
                

        except ValueError:
            print("Integer required!")
            continue