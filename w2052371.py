# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.

# Student ID: 20234004
# Date: 07/11/2023

from graphics import *

print(""" **** STUDENT PROGRESSION SOFTWARE ****\n--Enter 1 for STUDENT version, 2 for STAFF version--\n--If you are a staff member, Enter to continue program and 'q' to Quit and view results: """)

# function to get the version choice from the user
def versionChoice():
    versionInput = input("Select your version: ").strip().upper()
    if versionInput == "1":
        return "student"
    elif versionInput == "2":
        return "staff"
    else: 
        print("Invalid Version")
        return versionChoice()

# Part 1 - function for input validation
def validation(prompt):
    while True:
        try:
            credit = input(prompt)
            if credit.strip() == "":
                print("Please enter a value")
            elif int(credit) not in range(0,121,20):
                print("Out of range")
            else: 
                return int(credit)
        except ValueError:
            print("Integer required")

# Part 1 - Main Function for progression outcome calculation
def progressionOutcome(storedDataList,eachOutcomesCount,version=None):
        while True:
            Pass = validation("Enter your credits at Pass: ")
            Defer = validation("Enter your credits at Defer: ")
            Fail = validation("Enter your credits at Fail: ")
               
            if (Pass + Defer + Fail) != 120:
                print("Total incorrect")
                continue
            
            tempList = [Pass, Defer, Fail]
            output = None

            if Pass == 120:
                output = "Progress"
            elif (Pass+Defer) < Fail:
                output = "Exclude"
            elif Pass == 100 and (Defer==20 or Fail==20):
                output = "Progress (module trailer)"
            elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
                output = "Module retriever"
            
            if output is not None:
                print(output)
                if version == "STUDENT":
                    return
                eachOutcomesCount[output] += 1
                storedDataList.append(f'{output} - {", ".join([str(credit) for credit in tempList])}')

            userChoice = str(input("\nWould you like to enter another set of data ?")).upper().strip()
            if userChoice == "Q":
                return

# Part 1 - function to draw the rectangle bars for the histogram
def drawBar(window, x, y, barWidth, barHeight, color, value):
    if value > 0:
        # create a rect bar
        bar = Rectangle(Point(x, y), Point(x + barWidth, y - barHeight))
        bar.setFill(color), bar.draw(window)

        # display the count above the bar
        valueText = Text(Point(x + barWidth / 2, y - barHeight - 10), str(value))
        valueText.setSize(13), valueText.setStyle("bold"), valueText.draw(window)

# Part 1 - without rect bars, function to draw the all the elements for the histogram
# I change the window height based on the maximum count, 
# because If height is given then maximum count reach that height, it won't display correctly
def displayHistogram(eachOutcomesCount):

    # extract the values 
    values = list(eachOutcomesCount.values()) 
    xLabels = ["Progress","Trailer","Retriever","Exclude"]
    colors = ["#79db7c", "#2a782d", "#698729", "#e374c7"]

    # calculate necessary dimensions for window, based on the highest bar
    maxValue, barWidth = max(values), 80
    windowWidth, windowHeight = 600, max(450, maxValue*10+100)

    window = GraphWin("Histogram",windowWidth,windowHeight)

    # calculate positions for the x axis labels   
    availableWidth = windowWidth - 2 * barWidth
    xLabelPositions = [barWidth + (i * availableWidth) / 3 for i in range(4)]

    # display title of the histogram
    title = Text(Point(120, 30),"Histogram Result")
    title.setSize(18), title.setStyle("bold"),title.draw(window)
    
    # display total num of outcomes 
    totalMessage = Text(Point(150, windowHeight - 25), f"{sum(values)} outcomes in total.")
    totalMessage.setSize(16), totalMessage.setStyle("bold"),totalMessage.draw(window)

    # draw a bar for each category
    for i, value in enumerate(values):
        drawBar(window, xLabelPositions[i] - barWidth/2, windowHeight - 80, barWidth, value * 10, colors[i], value)

    # draw a labels for each category
    for index, labelText in enumerate(xLabels):
        xLabel = Text(Point(xLabelPositions[index], windowHeight - 60), labelText)
        xLabel.setSize(15), xLabel.setStyle("bold"), xLabel.setTextColor("#3b393a"), xLabel.draw(window)
    
    # draw a horizontal line for x axis
    xAxisLine = Line(Point(xLabelPositions[0] - barWidth / 2, windowHeight - 81), Point(xLabelPositions[-1] + barWidth /2, windowHeight - 81))
    xAxisLine.draw(window)

    # wait for a mouse clcik to close the window
    try:
        window.getMouse()
        window.close()
    except GraphicsError:
        pass

# Part 02 - function to print the data that stored
def storedData(storedDataList):
    print("Part 2:")
    for eachData in storedDataList:
        print(eachData)

# Part 03 - function to write input data to a file and display from it
def writeInAFile(storedDataList):

    # clear the content of the existing datafile / create a new one
    open('dataFile.txt', 'w').close()
    for eachData in storedDataList:
        try:
            with open("dataFile.txt","a") as dataFile:
                dataFile.write(eachData.strip()+"\n")
        except FileNotFoundError:
            with open("dataFile.txt",'w') as dataFile:
                dataFile.write(eachData.strip()+"\n")
    
    print("Part 3:")
    with open('dataFile.txt','r') as dataFile:
        linesOfData = dataFile.readlines()
        for line in linesOfData:
            print(line.strip())

# starts here
if __name__ == "__main__":

    eachOutcomesCount = {
        "Progress": 0,
        "Progress (module trailer)": 0,
        "Module retriever": 0,
        "Exclude": 0
    }
    storedDataList = []
    if versionChoice().upper() == "STUDENT":
        progressionOutcome(None,None,"STUDENT")

    else: 
        progressionOutcome(storedDataList,eachOutcomesCount)

        # Part 01 - histogram
        displayHistogram(eachOutcomesCount)
        print()

        # Part 02 - print the stored date
        storedData(storedDataList)
        print()

        # Part 03 - write to file & display
        writeInAFile(storedDataList)