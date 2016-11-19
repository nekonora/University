import numpy as np

# FRAUNHOFER
# Variabili
# ---------

# mm, fenditura schermo
L = [770.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0] 
# mm, diametro banda nera
d = [25.2, 21.3, 20.0, 17.7, 15.4, 13.2, 12.8, 10.1, 9.5, 7.1, 5.2]   

# Calcoli
# -------
ran = 11
lam = 632.8 * (10 ** (-6))
theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	theta[i] = np.arctan2((d[i] / 2), L[i])
D = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	D[i] = ((1.22 * lam) / np.sin(theta[i]))
indice = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	indice[i] = (D[i] ** 2) / (L[i] * lam)

# Print
# -----

print("- - - - Diffrazione Fraunhofer - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*L))
print("d (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*d))
print("theta (rad):      {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*theta))
print("D (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*D))
print("indice:           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n\n\n".format(*indice))


# FRAUNHOFER Opzionale
# Variabili
# ---------

# mm, fenditura schermo
op_L = [930.0, 880.0, 830.0, 780.0, 730.0, 680.0, 630.0, 580.0, 530.0, 480.0, 430.0] 
# mm, diametro banda nera
op_d = [7.6, 7.4, 6.8, 6.1, 5.9, 5.4, 5.0, 4.8, 4.0, 3.7, 3.5]   

# Calcoli
# -------
op_theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_theta[i] = np.arctan2((op_d[i] / 2), op_L[i])
op_D = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_D[i] = ((1.22 * lam) / np.sin(op_theta[i]))
op_indice = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_indice[i] = (op_D[i] ** 2) / (op_L[i] * lam)

# Print
# -----

print("- - - - Diffrazione Fraunhofer (opzionale) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*op_L))
print("d (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*op_d))
print("theta (rad):      {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_theta))
print("D (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_D))
print("indice:           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_indice))
