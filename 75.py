"""
Exercise 75
Question: Please plot the data of this file into a graph of x and y axis.

"""
# Answer
import pandas
import pylab as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()