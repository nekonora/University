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
		if len(error) == 1 :
			self.error = np.array(error * len(value))
		else :
			self.error = error
		self.rad = value * np.pi / 180													### Se gradi > radianti
		self.grad = value * 180 / np.pi													### Se rad > gradi
		self.mean = np.mean(value)															### Media
		self.meanErr = error / np.sqrt(len(value))							### Errore sulla media
		self.semiMaxDisp = 0.5 * (value[-1] - value[0])					### Errore max
		self.percRelErr = (self.semiMaxDisp / self.mean) * 100	### Errore relativo (%)
		
def err(value1, value2, type) :
	error = []
	if type == "sum" :
		for i in range(len(value1.value)) :
			error.append(np.sqrt((value1.error[0] ** 2) + (value2.error[0] ** 2)))
	elif type == "arctan" :
		for i in range(len(value1.value)) :
			error.append(np.sqrt((value1.error[0] * value2.error[0]) / (value1.value[i] ** 2 + value2.value[i] ** 2)) * 180 / np.pi)
	else :
		error = 0.0
	return error

### Plotter - prende array 2D(+ stile linea) come args
def plot_graf(*args) :
	if args :
		for ar in args :
			pl.plot(ar[0], ar[1], ar[2])
			pl.errorbar(ar[0], ar[1], ar[3], ar[4])
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
_theta0 = [0.0] * 10
_y = [25.0] * 10

theta0 = 	misura(value= np.array(_theta0), name= "$\\theta_0$", error= [1.0])
y = 			misura(value= np.array(_y), name= "$y$", error = [0.5])
#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_theta1 = [45,42,40,38,36,30,26,22,20,18]
_x = [0,2.4,4.1,5.9,7.9,14.2,19.4,25.7,30.3,34.5]

theta1 = 	misura(value= np.array(_theta1), name= "$\\theta '$", error= [1.0])
x =				misura(value= np.array(_x), name="$x$", error= [0.5])

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_thetaI =	 []
_Theta =	 []
_index = 	 []

for i in range(10) :
	_thetaI.append(_theta1[i] - _theta0[i])
	_Theta.append(np.arctan2(_y[i], _x[i]) * 180 / np.pi)
	_index.append((_thetaI[i] * 2) - _Theta[i])

### Errori
#errTheta = []
#for i in _x :
#	errTheta.append(np.sqrt((0.025) / (x.value[i] ** 2 + y.value[i] ** 2)) * 180 / np.pi)

thetaI = 	misura(value= np.array(_thetaI), name= "$\\theta_i$", error= err(theta1, theta0, "sum"))
Theta = 	misura(value= np.array(_Theta), name="$\\Theta$", error= err(x, y, "arctan"))
index = 	misura(value= np.array(_index), name="$2\\theta_i - \\Theta$", error= [0.0])

### Correlazione lineare tra due valori (x,y)
fitLine = poly_fit(thetaI.value,Theta.value, 1)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([theta0, theta1, thetaI, y, x, Theta, index])

print("\nMedia indice: {}".format(index.mean))
print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea) - stile linea: colore + "o","-","--"
plotArrayTheta = np.array([thetaI.value, Theta.value, "ko", thetaI.error, Theta.error])
plotArrayThetaFit = np.array([thetaI.value, thetaI.value * fitLine[0] + fitLine[1], "k--", 0, 0])
plotArrayThetaTheoric = np.array([thetaI.value, thetaI.value * 2, "r-", 0, 0])
plot_graf(plotArrayTheta, plotArrayThetaFit, plotArrayThetaTheoric)


