# # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.

# Student ID: 20234004
# Date: 07/11/2023

from graphics import *

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

def drawBar(window,x,y,width,height,color):
    bar = Rectangle(Point(x,y), Point(x+width,y-height))
    bar.setFill(color)
    bar.draw(window)

def histogram(eachOutcomesCount):
    values = list(eachOutcomesCount.values())
    colors = ["#7FCCE5", "#5DA4D9", "#3B7ABD", "#235D9F"]

    maxValue =max(values)
    windowWidth, windowHeight = 600, max(500, maxValue*10+100)
    window = GraphWin("Histogram",windowWidth,windowHeight)
    barWidth, spacing, x = 80,30,50

    totalMessage = Text(Point(windowWidth/2,windowHeight-30),f"{sum(values)} Total Outcomes!")
    totalMessage.setSize(14)
    totalMessage.draw(window)

    title = Text(Point(windowWidth/2,30),"Histogram Result")
    title.setSize(16), title.setStyle("bold")
    title.draw(window)
    
    for i,value in enumerate(values):
        drawBar(window, x, windowHeight-80, barWidth, value*10,colors[i])
        x += barWidth + spacing

    yTicks = [tick for tick in range(0,max(values)+10,10)]
    for yTick in yTicks:
        label = Text(Point(30,windowHeight-80-yTick*10), str(yTick))
        label.setSize(10)
        label.draw(window)
    
    xLabels = list(eachOutcomesCount.keys())
    availableWidth = windowWidth - 2*barWidth
    xLabelPositions = [
        barWidth + (i*availableWidth)/3 for i in range(4)
    ]

    for index, labelText in enumerate(xLabels):
        xLabel = Text(Point(xLabelPositions[i],windowHeight-60),labelText)
        xLabel.setSize(12), xLabel.setStyle("bold"), xLabel.setTextColor("#3b393a")
        xLabel.draw(window)
    
    yAxisLine = Line(Point(47,windowHeight-81), Point(windowWidth-120,windowHeight-81))
    yAxisLine.draw(window)
    
    # xLabel = Text(Point(50 + barWidth / 2, 370), "Progress")
    # xLabel.draw(window)

    # xLabel = Text(Point(50 + barWidth + spacing + barWidth / 2, 370), "Trailer")
    # xLabel.draw(window)

    # xLabel = Text(Point(50 + 2 * (barWidth + spacing) + barWidth / 2, 370), "Retriever")
    # xLabel.draw(window)

    # xLabel = Text(Point(50 + 3 * (barWidth + spacing) + barWidth / 2, 370), "Excluded")
    # xLabel.draw(window)

    # yAxisLine = Line(Point(47, 351), Point(380,351))
    # yAxisLine.draw(window)

    window.getMouse()
    window.close()

while True:
    print(progressionOutcome(eachOutcomesCount))
    userChoice = str(input("\nWould you like to enter another set of data ?\nEnter for Yes or 'q' to Quit and view results: ")).title()
    if userChoice == "Q":
        break

histogram(eachOutcomesCount)

