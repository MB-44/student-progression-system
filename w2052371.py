# # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.

# Student ID: 20234004
# Date: 07/11/2023

from graphics import *

print(" **** STUDENT PROGRESSION SOFTWARE ****")

# Part 1
def rangeCheck(prompt):
    while True:
        try:
            credit = input(prompt)
            if credit.strip() == "":
                print("please enter a value")
            elif int(credit) not in range(0,121,20):
                print("Out of range")
            else:
                return int(credit)
        except ValueError:
            print("Integer required!")

# Part 1 - Main Function
def progressionOutcome(eachOutcomesCount):
        while True:
            Pass = rangeCheck("Enter your credits at Pass: ")
            Defer = rangeCheck("Enter your credits at Defer: ")
            Fail = rangeCheck("Enter your credits at Fail: ")
               
            if (Pass + Defer + Fail) != 120:
                print("Total incorrect")
                continue
            
            tempList = [Pass, Defer, Fail]

            if Pass == 120:
                eachOutcomesCount["Progress"] += 1
                print("Progress")
                return storedDataList.append(f'Progress - {", ".join([str(credit) for credit in tempList])}')
                
            elif (Pass+Defer) < Fail:
                eachOutcomesCount["Exclude"] += 1
                print("Exclude")
                return storedDataList.append(f'Exclude - {", ".join([str(credit) for credit in tempList])}')

            elif Pass == 100 and (Defer==20 or Fail==20):
                eachOutcomesCount["Trailer"] += 1
                print("Progress (module trailer)")
                return storedDataList.append(f'Progress (module trailer) - {", ".join([str(credit) for credit in tempList])}')

            elif (Pass in [0,20,40,60,80]) and (Defer in [0,20,40,60,80,100,120]) and (Fail in [0,20,40,60]):
                eachOutcomesCount["Retriever"] += 1
                print("Module retriever")
                return storedDataList.append(f'Module retriever - {", ".join([str(credit) for credit in tempList])}')

# Part 1 - draw the rectangle bars for histogram
def drawBar(window, x, y, barWidth, barHeight, color, value):
    if value > 0:
        bar = Rectangle(Point(x, y), Point(x + barWidth, y - barHeight))
        bar.setFill(color)
        bar.draw(window)

        valueText = Text(Point(x + barWidth / 2, y - barHeight - 10), str(value))
        valueText.setSize(13), valueText.setStyle("bold")
        valueText.draw(window)

# Part 1 - draw all the things for histogram without rectangle bars
def histogram(eachOutcomesCount):
    values = list(eachOutcomesCount.values())
    xLabels = list(eachOutcomesCount.keys())
    colors = ["#79db7c", "#2a782d", "#698729", "#e374c7"]

    maxValue,barWidth =max(values), 80
    windowWidth, windowHeight = 600, max(450, maxValue*10+100)

    window = GraphWin("Histogram",windowWidth,windowHeight)
    
    availableWidth = windowWidth - 2 * barWidth
    xLabelPositions = [barWidth + (i * availableWidth) / 3 for i in range(4)]

    title = Text(Point(120, 30),"Histogram Result")
    title.setSize(18), title.setStyle("bold")
    title.draw(window)
    
    totalMessage = Text(Point(150, windowHeight - 25), f"{sum(values)} outcomes in total.")
    totalMessage.setSize(16), totalMessage.setStyle("bold")
    totalMessage.draw(window)

    for i, value in enumerate(values):
        drawBar(window, xLabelPositions[i] - barWidth/2, windowHeight - 80, barWidth, value * 10, colors[i], value)

    for index, labelText in enumerate(xLabels):
        xLabel = Text(Point(xLabelPositions[index], windowHeight - 60), labelText)
        xLabel.setSize(15), xLabel.setStyle("bold"), xLabel.setTextColor("#3b393a")
        xLabel.draw(window)
    
    yAxisLine = Line(Point(xLabelPositions[0] - barWidth / 2, windowHeight - 81), Point(xLabelPositions[-1] + barWidth /2, windowHeight - 81))
    yAxisLine.draw(window)

    window.getMouse()
    window.close()

# Part 02 - store the input data in a list & print out
def storedData(storedDataList):
    print("Part 2:")
    for eachData in storedDataList:
        print(eachData)

# Part 03 - input data will write in a file, and displayed after that
def writeInAFile(storedDataList):
    open('dataFile.txt', 'w').close()
    for eachData in storedDataList:
        try:
            with open("dataFile.txt"):
                with open("dataFile.txt","a") as dataFile:
                    dataFile.write(eachData.strip()+"\n")
        except IOError:
            with open("dataFile.txt",'w') as dataFile:
                dataFile.write(eachData.strip()+"\n")
    
    print("Part 3:")
    with open('dataFile.txt','r') as dataFile:
        linesOfData = dataFile.readlines()
        for line in linesOfData:
            print(line.strip())

eachOutcomesCount = {"Progress": 0,"Trailer": 0,"Retriever": 0,"Exclude": 0}
storedDataList = []

while True:
    progressionOutcome(eachOutcomesCount)
    userChoice = str(input("\nWould you like to enter another set of data ?\nEnter for Yes or 'q' to Quit and view results: ")).title()
    if userChoice == "Q":
        break

# Part 01
histogram(eachOutcomesCount)

# Part 02
storedData(storedDataList)
print()

# Part 03
writeInAFile(storedDataList)