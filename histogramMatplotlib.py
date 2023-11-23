import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

from w2052371_Part01 import eachOutcomesCount as outcome

xLabels = list(outcome.keys())
yLabels = list(outcome.values())

plt.yticks([num for num in yLabels])

plt.bar(xLabels,yLabels)
plt.show()