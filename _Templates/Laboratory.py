###########################################################################################
#    _ _             ___                               _             _                  _ _
#  _| | |_     ___  / __|  _  _   _ __   ___   _ _    | |     __ _  | |__    ___     _| | |_
# |_  .  _|   |___| \__ \ | || | | '_ \ / -_) | '_|   | |__  / _` | | '_ \  |___|   |_  .  _|
# |_     _|         |___/  \_,_| | .__/ \___| |_|     |____| \__,_| |_.__/          |_     _|
# __|_|_|                  _     |_|                                                  |_|_|
# \ \ / /  ___   __   __  | |_   (_)
#  \ V /  / -_) / _| / _| | ' \  | |
#  _\_/   \___| \__| \__| |_||_| |_|   _   _          _
# | _ \  ___   _ __    ___   _ _    __| | (_)  _ _   (_)
# |   / / -_) | '  \  / _ \ | ' \  / _` | | | | ' \  | |
# |_|_\ \___| |_|_|_| \___/ |_||_| \__,_|_|_| |_||_| |_|
# |_  /  __ _   / _|  / _|  ___   _ _   (_)
#  / /  / _` | |  _| |  _| / _ \ | ' \  | |
# /___| \__,_| |_|   |_|   \___/ |_||_| |_|
###########################################################################################

import numpy as np
import pylab as pl

#---------------------------------------------------------------------------------------#
#-/////////////////////// FUNCS & CLASSES /////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
class misura:
	def __init__(self, value, name, error):
		self.value = np.array(value, dtype= float)
		self.name = name
		if len(error) == 1 :
			self.error = np.array(error * len(value))
		else :
			self.error = error
		self.mean = np.mean(value)							        	### Media
		self.meanErr = error / np.sqrt(len(value))				### Errore sulla media
		self.semiMaxDisp = 0.5 * (value[-1] - value[0])	  ### Errore max

def err(value1, value2, type) :
	error = []
	if type == "sum" :
		for i in range(len(value1.value)) :
			error.append(np.sqrt((value1.error[0] ** 2) + (value2.error[0] ** 2)))
	elif type == "arctan" :
		for i in range(len(value1.value)) :
			error.append(np.sqrt((value1.error[0] * value2.error[0]) / (value1.value[i] ** 2 + value2.value[i] ** 2)) * 180 / np.pi)
	elif type == "const" :
		for i in range(len(value1.value)) :
			error.append(value1.error[0] * value2)
	else :
		error = 0.0
	return error

### Plotter - prende array 2D(+ stile linea) come args
def plot_graf(xLabel, yLabel, *args) :
	if args :
		for ar in args :
			pl.plot(ar[0], ar[1], ar[2])
			pl.errorbar(ar[0], ar[1], ar[3], ar[4], fmt=None, ecolor='k', capthick=2)
	pl.xlabel(xLabel)
	pl.ylabel(yLabel)
	pl.title("")
	pl.grid(True)
	pl.show()

### Polynomial Regression - y = a+mx - restituisce un array [a,m,R^2]
def poly_fit(x, y, degree):
	results = np.empty(3)
	coeffs = np.polyfit(x.value, y.value, degree)
	### Polynomial Coefficients
	results[0] = coeffs[0]
	results[1] = coeffs[1]
	### r-squared
	p = np.poly1d(coeffs)
	### fit values, and mean
	yhat = p(x.value)
	ybar = np.sum(y.value)/len(y.value)
	ssreg = np.sum((yhat-ybar)**2)
	sstot = np.sum((y.value - ybar)**2)    #
	results[2] = ssreg / sstot
	return results

### Result Printer
def print_results(array) :
	print("\n")
	title = "| "
	tableLine = "|"
	tableText = "|"
	valuesArray = []
	for i in array :
		title += "{}|".format(i.name)
		tableLine += "---|"
		tableText += "{:.2f}|"
		valuesArray.append(i.value)
		if np.mean(i.error) != 0.0 :
			tableLine += "---|"
			title += "$\\sigma${}|".format(i.name)
			tableText += "$\\pm${:.1f}|"
			valuesArray.append(i.error)
	print(title)
	print(tableLine)
	for row in zip(*valuesArray) :
		print(tableText.format(*row))

#---------------------------------------------------------------------------------------#
#-/////////////////////// CONSTANTS ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
Lambda = 632.8E-6

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_x = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
x = misura(value= _x, name="$x$", error= [0.5])

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_y = []
for i in _x :
	_y.append(i*2 + 5)
y = misura(value= _y, name="$y$", error= err(x, 2, "const"))

### Correlazione lineare tra due valori (x,y)
fitLine = poly_fit(x,y,1)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([x, y])

print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea, xErr, yErr)
plotArray = np.array([x.value, y.value, "ko", x.error, y.error])
plot_graf("$\\theta_i$", "$\\Theta$", plotArray)
