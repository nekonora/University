###########################################################################################
#    _ _             ___                               _             _                  _ _
#  _| | |_     ___  / __|  _  _   _ __   ___   _ _    | |     __ _  | |__     ___     _| | |_
# |_  .  _|   |___| \__ \ | || | | '_ \ / -_) | '_|   | |__  / _` | | '_ \   |___|   |_  .  _|
# |_     _|         |___/  \_,_| | .__/ \___| |_|     |____| \__,_| |_.__/           |_     _|
# __|_|_|                  _     |_|                                                   |_|_|
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

# Funzioni e classi -----------------------------------------------------------------------
class misura:
	def __init__(self, value, name):
		self.value = value
		self.name = name
		#self.rad = value * np.pi / 180
		#self.grad = value * 180 / np.pi

# Plotter - prende array 2D(+ stile linea) come args
def plot_graf(*args) :
	if args :
		for ar in args :
			pl.plot(ar[0], ar[1], ar[2])
	pl.xlabel("")
	pl.ylabel("")
	pl.title("")
	pl.grid(True)
	pl.show()

# Polynomial Regression - y = a+mx - restituisce un array [a,m,R^2]
def poly_fit(x, y, degree):
	results = np.empty(3)
	coeffs = np.polyfit(x, y, degree)
	# Polynomial Coefficients
	results[0] = coeffs[0]
	results[1] = coeffs[1]
	# r-squared
	p = np.poly1d(coeffs)
	# fit values, and mean
	yhat = p(x)                         # or [p(z) for z in x]
	ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
	ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
	sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
	results[2] = ssreg / sstot
	return results

# Result Printer
def print_results(values, names) :
	print("\n")
	title = "| "
	tableLine = "|"
	for i in names :
		title += i
		title += " |"
		tableLine += "---|"
	print(title)
	print(tableLine)
	for row in zip(*values) :
		tableText = "|"
		for i in range(len(row)) :
			tableText += " {:.3f} |"
		print(tableText.format(*row))
	print("\n")

# Constants -----------------------------------------------------------------------------
#
Lambda = 632.8E-6

# Variables -----------------------------------------------------------------------------
#
#
_L = np.array([780.0, 700.0, 630.0, 560.0, 490.0])
_d1 = np.array([23.9, 21.8, 19.5, 17.3, 15.2]) / 2.0
_d2 = np.array([23.2, 21.8, 19.8, 17.5, 15.1]) / 2.0

L = misura(value= _L, name="$L$")
d1 = misura(value= _d1 / 2.0, name="$d$")
d2 = misura(value= _d2 / 2.0, name="$d$")

# Calculations -------------------------------------------------------------------------
#
#
_theta1 = []
_D1 = []
_theta2 = []
_D2 = []

for i in range(5) :
	_theta1.append(np.arctan2(_d1[i], _L[i]))
for i in range(5) :
	_D1.append(((1.0 * Lambda) / np.sin(_theta1[i])))
for i in range(5) :
	_theta2.append(np.arctan2(_d2[i], _L[i]))
for i in range(5) :
	_D2.append(((1.0 * Lambda) / np.sin(_theta2[i])))

theta1 = misura(value= _theta1, name= "$\\theta$")
D1 = misura(value= _D1, name="$D$")
theta2 = misura(value= _theta2, name= "$\\theta$")
D2 = misura(value= _D2, name="$D$")

# Un array con tutte le misure
varArrayValues1 = [L.value, d1.value, theta1.value, D1.value]
varArrayNames1 = [L.name, d1.name, theta1.name, D1.name]
varArrayValues2 = [L.value, d2.value, theta2.value, D2.value]
varArrayNames2 = [L.name, d2.name, theta2.name, D2.name]

#fitLine = poly_fit(x,y,1)

# Errors -------------------------------------------------------------------------------
#
#
#errTheta = np.array([0.0] * 10)
#for i in range(10) :
#	errTheta[i] = np.sqrt((0.025) / (x[i] ** 2 + y[i] ** 2)) * 180 / np.pi

# Results ------------------------------------------------------------------------------
#
#

print_results(varArrayValues1, varArrayNames1)
print_results(varArrayValues2, varArrayNames2)


#print("\nMedia indice: {}".format(np.mean(index)))
#print("R^2: {}\n".format(fitLine[2]))

# Plot: crea un array con argomenti (x, y, stile linea) - stile linea: colore + "o","-","--"
#plotArrayTheta = np.array([thetaI, Theta, "ko"])
#plot_graf(myArray)
