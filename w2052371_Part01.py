# # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20234004
# Date: 07/11/2023


print(" **** STUDENT PROGRESSION SOFTWARE ****")

eachOutcomesCount = {"Progress": 0,"Trailer": 0,"Retriever": 0,"Exclude": 0}

def progressionOutcome(eachOutcomesCount):
        while True:
            try:
                Pass = int(input("Enter your credits at Pass: "))
                Defer = int(input("Enter your credits at Defer: "))
                Fail = int(input("Enter your credits at Fail: ")) 

                if not (Pass%20==0 and Defer%20==0 and Fail%20==0):
                    print("Out of range")
                    continue
                
                if (Pass + Defer + Fail) != 120:
                    print("Total incorrect")
                    continue

            except ValueError:
                print("Integer required")
                continue

            if Pass == 120:
                eachOutcomesCount["Progress"] += 1
                return "Progress"

            elif (Pass+Defer) < Fail:
                eachOutcomesCount["Exclude"] += 1
                return "Exclude"

            elif Pass == 100 and (Defer==20 or Fail==20):
                eachOutcomesCount["Trailer"] += 1
                return "Progress (module trailer)"

            elif (Pass in [0,20,40,60,80]) and (Defer in [0,20,40,60,80,100,120]) and (Fail in [0,20,40,60]):
                eachOutcomesCount["Retriever"] += 1
                return "Do not progress - Module retriever"

while True:
    print(progressionOutcome(eachOutcomesCount))
    userChoice = str(input("\nWould you like to enter another set of data ?\nEnter 'y' for Yes or 'q' to Quit and view results: ")).title()
    if userChoice != "Y":
        break
