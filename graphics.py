import matplotlib.pyplot as plot 
import numpy as numpy

from w2052371_Part01 import eachOutcomesCount as eachOutcomesCount


plot.get_current_fig_manager().set_window_title("Histogram")

keys,values = [],[]
for key,value in eachOutcomesCount.items():
    keys.append(key) , values.append(value)    
    
x = numpy.array(keys)
y = numpy.array(values)

plot.bar(x,y,color = "#4CAF50")
plot.show()