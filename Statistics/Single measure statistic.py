# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# --- Functions

def measure():
	
	valuesArray = []
	print("\n--- --- --- --- --- --- ---")
	print("\n- NEW MEASUREMENT -\n")
	print("\nWrite every values, when you have finished, write \"end\" to end the process.\n")
		
	# Taking the values
	value = 0.0
	measureNumber = 0
	while value != "end":
		value = raw_input("%d: " % measureNumber)
		if value != "end":
			valuesArray.append(float(value))
			measureNumber += 1
		
	# Convert the array to numpy array
	np.asarray(valuesArray)
		
	print("\nEnded taking values. The array is the foloowing:\n")
	print(valuesArray)
		
	print("\nMean is:      %.4f" % np.mean(valuesArray, dtype=np.float64))
	print("Max value is: %.4f" % np.amax(valuesArray))
	print("Min value is: %.4f" % np.amin(valuesArray))
	print("Range is:     %.4f" % (np.amax(valuesArray) - np.amin(valuesArray)))
	print("Std dev:      %.4f" % np.std(valuesArray))
	print("Variance:     %.4f" % np.var(valuesArray))
		
	count, bins, ignored = plt.hist(valuesArray, 30, normed=True)
	plt.plot(bins, 1/(np.std(valuesArray) * np.sqrt(2 * np.pi)) * np.exp( - (bins - np.mean(valuesArray, dtype=np.float64))**2 / (2 * np.std(valuesArray)**2) ), linewidth=2, color='r')
	plt.show()
	
def rndMeasure():
	
	print("\n--- --- --- --- --- --- ---")
	print("\n- NEW RANDOM VALUES -\n")
	numbers = int(raw_input("\nNumber of measures: "))
	rValue = float(raw_input("True value: "))
	rError = float(raw_input("Measurment error: "))
	print("\nGenerating %d random values..." % numbers)
		
	a = np.random.normal(rValue, rError, numbers)
		
	print("\nMean is:      %.4f" % np.mean(a, dtype=np.float64))
	print("Max value is: %.4f" % np.amax(a))
	print("Min value is: %.4f" % np.amin(a))
	print("Range is:     %.4f" % (np.amax(a) - np.amin(a)))
	print("Std dev:      %.4f" % np.std(a))
	print("Variance:     %.4f" % np.var(a))
		
	count, bins, ignored = plt.hist(a, 30, normed=True)
	plt.plot(bins, 1/(np.std(a) * np.sqrt(2 * np.pi)) * np.exp( - (bins - np.mean(a, dtype=np.float64))**2 / (2 * np.std(a)**2) ), linewidth=2, color='r')
	plt.show()

def rSquared(x, y): # X and Y as arrays!
	vecProd = x * y
	xSquared = x**2
	ySquared = y**2
	numerator = np.mean(vecProd) - (np.mean(x) * np.mean(y))
	denominator = np.sqrt((np.mean(xSquared) - np.mean(x)**2) * (np.mean(ySquared) - np.mean(y)**2))
	r = numerator / denominator
	RSquared = r**2
	beta = r * (np.std(y) / np.std(x))
	alpha = np.mean(y) - beta * np.mean(x)
	results = [r, RSquared, alpha, beta] 
	return results	
		
def linReg():
	
	print("\n--- --- --- --- --- --- ---")
	print("\n- NEW LINEAR REGRESSION -\n")
	linChoiche = raw_input("Do you want to give one(1) or both measures(2)? ")
	
	x = []
	y = []

	if linChoiche == "1":
		print("\nWrite the value X for every measurment Y. When finished, write \"end\" as an X value.\n")
		value = 0.0
		measureNumber = 0
		while value != "end":
			value = raw_input("Y = %d, X = " % measureNumber)
			if value != "end":
				x.append(float(value))
				measureNumber += 1
				y.append(int(measureNumber))
		print(x)
	elif linChoiche == "2":
		print("\nWrite in order the Y value, press enter and then the X value.When finished write \"end\" as an Y value.\n")
		valueX = 0.0
		valueY = 0.0
		measureNumber = 0
		while valueY != "end":
			valueY = raw_input("(%d) - Y: " % measureNumber)
			if valueY != "end":
				valueX = raw_input("  (%d) - X: " % measureNumber)
				x.append(float(valueX))
				y.append(float(valueY))
				measureNumber += 1
				
	print(x)
	print(y)
	
	np.asarray(x)
	np.asarray(y)
	
	fit = np.polyfit(x,y,1)
	fit_fn = np.poly1d(fit) 
	# fit_fn is a function which takes in x and returns an estimate for y
	
	minLimit = np.amin(np.array([np.amin(x), np.amin(y)]))
	maxLimit = np.amax(np.array([np.amax(x), np.amax(y)]))
	
	print(rSquared)
	
	plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
	plt.xlim(minLimit, maxLimit)
	plt.ylim(minLimit, maxLimit)		
	plt.show()
	
# --- Main

def main() :
	firstChoiche = raw_input("Do you want to start a new measure (N), input a random values (R) or calculate linear regression(L): ")
	
	if firstChoiche.upper() == "N":
		measure()
	elif firstChoiche.upper() == "R":
		rndMeasure()
	elif firstChoiche.upper() == "L":
		linReg()
			
main()