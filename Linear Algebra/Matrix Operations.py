import numpy as np

inputChoiceShapes = "n"
while inputChoiceShapes == "n":	
	print("--- Input matrices shapes ---\n")
	M1R = int(input("M1 Rows: "))
	M1C = int(input("M1 Columns: "))
	M2R = int(input("M2 Rows: "))
	M2C = int(input("M2 Columns: "))
	
	M1 = np.zeros([M1R,M1C], dtype=np.float)
	M2 = np.zeros([M2R,M2C], dtype=np.float)
	
	print("\nA is a {0}X{1} matrix\nB is a {2}X{3} matrix.\n".format(M1R,M1C,M2R,M2C))
	inputChoiceShapes = input("Is it correct? (y/n): ")
	if inputChoiceShapes == "n":
		print("\n--- Repeat.. ---\n")
	
print("\n--- Input Matrix A values ---\n")
inputChoiceM1Values = "n"
while inputChoiceM1Values == "n":
	for index, x in np.ndenumerate(M1):
		M1[index[0],index[1]] = float(input("A{}{}: ".format(index[0]+1,index[1]+1)))
	print("\n",M1)
	inputChoiceM1Values = input("\nIs this correct? (y/n): ")
	if inputChoiceM1Values == "n":
		print("\n--- Re–enter A values... ---") 
	
print("\n--- Input Matrix B values ---\n")
inputChoiceM2Values = "n"
while inputChoiceM2Values == "n":
	for index, x in np.ndenumerate(M2):
		M2[index[0],index[1]] = float(input("B{}{}: ".format(index[0]+1,index[1]+1)))
	print("\n",M2)
	inputChoiceM2Values = input("\nIs this correct? (y/n): ")
	if inputChoiceM2Values == "n":
		print("\n--- Re–enter B values... ---") 
		
print("\n--- Product ---\n\n{}".format(np.dot(M1,M2)))
