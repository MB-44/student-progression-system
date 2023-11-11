# # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20234004
# Date: 07/11/2023


print(" **** STUDENT PROGRESSION SOFTWARE ****")


Progress = Trailer = Retriever = Exclude = 0

eachOutcomesCount = {
            "Progress": Progress,
            "Trailer": Trailer,
            "Retriever": Retriever,
            "Exclude": Exclude
                     }

while True:
    while True:
        try:
            Pass = int(input("Enter your credits at Pass: "))
            if Pass not in range(0,130,20):
                print("Out of range")
                continue

            Defer = int(input("Enter your credits at Defer: "))
            if Pass not in range(0,130,20):
                print("Out of range")
                continue

            Fail = int(input("Enter your credits at Fail: ")) 
            if Pass not in range(0,130,20):
                print("Out of range")
                continue

            if (Pass + Defer + Fail) != 120:
                print("Total incorrect")
            else:
                break
            
        except ValueError:
            print("Integer required")
    
    if Pass == 120:
        eachOutcomesCount["Progress"] += 1
        print("Progress")

    elif (Pass+Defer) < Fail:
        eachOutcomesCount["Exclude"] += 1
        print("Exclude")

    elif Pass == 100 and (Defer==20 or Fail==20):
        eachOutcomesCount["Trailer"] += 1
        print("Progress (module trailer)")

    elif (Pass in [0,20,40,60,80]) and (Defer in [0,20,40,60,80,100,120]) and (Fail in [0,20,40,60]):
        eachOutcomesCount["Retriever"] += 1
        print("Do not progress - Module retriever")
    
    
    userChoice = str(input("\nWould you like to enter another set of data ?\nEnter 'y' for Yes or 'q' to Quit and view results: ")).title()
    if userChoice != "Y":
        break
