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
lam = 632.8 * (10 ** (-6))

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
# FRAUNHOFER
# mm, fenditura schermo
_L = ne([770.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0], 0.5) 
# mm, diametro banda nera
_d = ne([25.2, 21.3, 20.0, 17.7, 15.4, 13.2, 12.8, 10.1, 9.5, 7.1, 5.2], 0.05)   

L = misura(value=_L, name="$L$ (mm)")
d = misura(value=_d, name="$d$ (mm)")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_theta = []
_D = []
_indice = []

for i in range(len(L.value)) :
	_theta.append(atan((_d[i] / 2) / _L[i]))
	_D.append((1.22 * lam) / unp.sin(_theta[i]))
	_indice.append((_D[i] ** 2) / (_L[i] * lam))
		
theta = misura(value=_theta, name="$\\theta$ (rad)")
D = misura(value=_D, name="$D$ (mm)")
indice = misura(value=_indice, name="indice")

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

print_results([L, d, theta, D, indice])

# FRAUNHOFER Opzionale
# Variabili
# ---------

# mm, fenditura schermo
_op_L = ne([930.0, 880.0, 830.0, 780.0, 730.0, 680.0, 630.0, 580.0, 530.0, 480.0, 430.0], 0.5) 
# mm, diametro banda nera
_op_d = ne([7.6, 7.4, 6.8, 6.1, 5.9, 5.4, 5.0, 4.8, 4.0, 3.7, 3.5], 0.05)   

op_L = misura(value=_op_L, name="$L$ (mm)")
op_d = misura(value=_op_d, name="$d$ (mm)")

# Calcoli
# -------

_op_theta = []
_op_D = []
_op_indice = []

for i in range(len(op_L.value)) :
	_op_theta.append(atan((_op_d[i] / 2) / _op_L[i]))
	_op_D.append(((1.22 * lam) / sin(_op_theta[i])))
	_op_indice.append((_op_D[i] ** 2) / (_op_L[i] * lam))
	
op_theta = misura(value= _op_theta, name="$\\theta$ (rad)")
op_D = misura(value= _op_D, name = "$D$ (mm)")
op_indice = misura(value=_op_indice, name="Indice")

# Print
# -----

print("- - - - Diffrazione Fraunhofer (opzionale) - - - -\n")
print_results([op_L, op_d, op_theta, op_D, op_indice])
