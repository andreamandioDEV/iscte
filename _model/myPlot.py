# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: myPlot.py
# Ultima modificação: 01/02/2018
# Refs: https://www.pythonanywhere.com/forums/topic/5017/
#	   https://plot.ly/matplotlib/bar-charts/
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


# classe MyPlot:
#	- gerador de gráficos de barras e linear.
class MyPlot():

	def __init__(self):
		return

	# Função para gerar gráficos lineares
	# @param X -> eixo X
	# @param Y -> eixo Y
	# @param imgName -> nome da imagem a guardar
	# @param xLabel -> "rótulo" de X
	# @param yLabel -> "rótulo" de Y
	# @param xTicklables -> nomes em X
	# @param xOrientation -> disposição de X
	def linear_graph(X, Y, imgName, title, xLabel, yLabel, xTickslables, xOrientation='horizontal'):
		fig, ax = plt.subplots()
		plt.xticks(X, xTickslables, rotation=xOrientation,fontsize=6)
		plt.yticks(fontsize=6)
		plt.plot(X,Y)
		plt.xlabel(xLabel, fontsize=12)
		plt.ylabel(yLabel, fontsize=12)
		fig.suptitle(title, fontsize=14)
		fig.savefig('static/images/plot/'+imgName+'_linear.png',dpi=150)

	# Função para gerar gráficos de barras
	# @param X -> eixo X
	# @param Y -> eixo Y
	# @param imgName -> nome da imagem a guardar
	# @param xLabel -> "rótulo" de X
	# @param yLabel -> "rótulo" de Y
	# @param xTicklables -> nomes em X
	# @param xOrientation -> disposição de X
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