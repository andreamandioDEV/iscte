import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#Refs: https://www.pythonanywhere.com/forums/topic/5017/
#	   https://plot.ly/matplotlib/bar-charts/

class MyPlot():

	def __init__(self):
		return

	def linear_graph(X, Y, imgName, title, xLabel, yLabel, xTickslables, xOrientation='horizontal'):
		fig, ax = plt.subplots()
		plt.xticks(X, xTickslables, rotation=xOrientation,fontsize=6)
		plt.yticks(fontsize=6)
		plt.plot(X,Y)
		plt.xlabel(xLabel, fontsize=12)
		plt.ylabel(yLabel, fontsize=12)
		fig.suptitle(title, fontsize=14)
		fig.savefig('static/images/plot/'+imgName+'_linear.png',dpi=150)


	def bar_graph(X, Y, imgName, title, xLabel, yLabel,xTickslables, xOrientation='horizontal'):
		fig, ax = plt.subplots()
		width = 1
		plt.xticks(X, xTickslables, rotation=xOrientation,fontsize=6)
		plt.yticks(fontsize=6)
		plt.bar(X, Y, width, color="steelblue")
		plt.xlabel(xLabel, fontsize=12)
		plt.ylabel(yLabel, fontsize=12)
		fig.suptitle(title, fontsize=14)
		fig.savefig('static/images/plot/'+imgName+'_bar.png',dpi=150)