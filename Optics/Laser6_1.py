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
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties.umath import *

#---------------------------------------------------------------------------------------#
#-/////////////////////// FUNCS & CLASSES /////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
class misura:
	def __init__(self, value, name):
		self.nominal = np.array(unp.nominal_values(value))
		self.err = np.array(unp.std_devs(value))
		self.value = np.array(value)		
		self.name = name
		
### Funzione per creare numeri con errori integrati
def ne(array, error) :
	result = []
	for i in range(len(array)) :
		result.append(ufloat(array[i], error))
	return result
						
### Plotter - prende array 2D(+ stile linea) come args
def plot_graf(xLabel, yLabel, *args) :
	if args :
		for ar in args :
			pl.plot(ar[0].nominal, ar[1].nominal, ar[2])
			if ar[3] :
				pl.errorbar(ar[0].nominal, ar[1].nominal, ar[0].err, ar[1].err, fmt=None, ecolor='k', capthick=2)
	pl.xlabel(xLabel)
	pl.ylabel(yLabel)
	pl.title("")
	pl.grid(True)
	pl.show()

### Polynomial Regression - y = a+mx - restituisce un array [a,m,R^2]
def poly_fit(x, y):
	results = np.empty(3)
	coeffs = np.polyfit(x.nominal, y.nominal, 1)
	### Polynomial Coefficients
	results[0] = coeffs[0]
	results[1] = coeffs[1]
	### r-squared
	p = np.poly1d(coeffs)
	### fit values, and mean
	yhat = p(x.nominal)
	ybar = np.sum(y.nominal)/len(y.nominal)
	ssreg = np.sum((yhat-ybar)**2)
	sstot = np.sum((y.nominal - ybar)**2)    
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
		tableText += "${:L}$|"
		valuesArray.append(i.value)
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
### Immettere valori come ne([valori], errore)
_thetaP = ne([55.0], 1.0)
thetaP = misura(value=_thetaP, name="$$\\theta_p")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_nT = []
for i in range(1) :
	_nT.append(tan(_thetaP[i] * 3.14 / 180 ))

nT = misura(value=_nT, name="$n_t$")

### Correlazione lineare tra due valori (x,y)
#fitLine = poly_fit(x,y)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([thetaP, nT])

#print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea, xErr, yErr)
#plotArray = np.array([x, y, "ko", True])
#plot_graf("$\\theta_i$", "$\\Theta$", plotArray)
