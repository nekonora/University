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
		self.value = value
		self.name = name
		self.error = error
		self.rad = value * np.pi / 180							### Se gradi > radianti
		self.grad = value * 180 / np.pi							### Se rad > gradi
		self.mean = np.mean(value)								### Media
		self.meanErr = error / np.sqrt(len(value))				### Errore sulla media
		self.semiMaxDisp = 0.5 * (value[-1] - value[0])			### Errore max
		self.percRelErr = (self.semiMaxDisp / self.mean) * 100	### Errore relativo (%)


### Plotter - prende array 2D(+ stile linea) come args
def plot_graf(*args) :
	if args :
		for ar in args :
			pl.plot(ar[0], ar[1], ar[2])
	pl.xlabel("")
	pl.ylabel("")
	pl.title("")
	pl.grid(True)
	pl.show()

### Polynomial Regression - y = a+mx - restituisce un array [a,m,R^2]
def poly_fit(x, y, degree):
	results = np.empty(3)
	coeffs = np.polyfit(x, y, degree)
	### Polynomial Coefficients
	results[0] = coeffs[0]
	results[1] = coeffs[1]
	### r-squared
	p = np.poly1d(coeffs)
	### fit values, and mean
	yhat = p(x)
	ybar = np.sum(y)/len(y)
	ssreg = np.sum((yhat-ybar)**2)
	sstot = np.sum((y - ybar)**2)    #
	results[2] = ssreg / sstot
	return results

### Result Printer
def print_results(array) :
	print("\n")
	title = "| "
	tableLine = "|"
	valuesArray = []
	for i in array :
		title += i.name
		title += " |"
		tableLine += "---|"
		valuesArray.append(i.value)
	print(title)
	print(tableLine)
	for row in zip(*valuesArray) :
		tableText = "|"
		for i in range(len(row)) :
			tableText += " {:.3f} |"
		print(tableText.format(*row))

#---------------------------------------------------------------------------------------#
#-/////////////////////// CONSTANTS ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
Lambda = 632.8E-6

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_x = [1,4,3]
x = misura(value= np.array(_x), name="$x$", error= 0.5)

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_y = []
for i in _x :
	_y.append(i**2)
y = misura(value= np.array(_y), name="$y$", error= 0.5)

### Correlazione lineare tra due valori (x,y)
#fitLine = poly_fit(x,y,1)

### Errori
#errTheta = []
#for i in range(10) :
#	errTheta.append(np.sqrt((0.025) / (x[i] ** 2 + y[i] ** 2)) * 180 / np.pi)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([x, y])

print(y.percRelErr)

#print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea) - stile linea: colore + "o","-","--"
#plotArrayTheta = np.array([thetaI, Theta, "ko"])
#plot_graf(myArray)
