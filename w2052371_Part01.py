# # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.

# Student ID: 20234004
# Date: 07/11/2023

from graphics import *

print(" **** STUDENT PROGRESSION SOFTWARE ****")

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

            except:
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


def drawBar(window, x, y, barWidth, barHeight, color, value):
    if value > 0:
        bar = Rectangle(Point(x, y), Point(x + barWidth, y - barHeight))
        bar.setFill(color)
        bar.draw(window)

        valueText = Text(Point(x + barWidth / 2, y - barHeight - 10), str(value))
        valueText.setSize(13), valueText.setStyle("bold")
        valueText.draw(window)

def histogram(eachOutcomesCount):
    values = list(eachOutcomesCount.values())
    xLabels = list(eachOutcomesCount.keys())
    colors = ["#CCCCCC", "#AED9E0", "#B7E4C7", "#FFD3E0"]

    maxValue =max(values)
    windowWidth, windowHeight = 600, max(450, maxValue*10+100)
    barWidth = 80

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

eachOutcomesCount = {"Progress": 0,"Trailer": 0,"Retriever": 0,"Exclude": 0}

while True:
    print(progressionOutcome(eachOutcomesCount))
    userChoice = str(input("\nWould you like to enter another set of data ?\nEnter for Yes or 'q' to Quit and view results: ")).title()
    if userChoice == "Q":
        break

histogram(eachOutcomesCount)

