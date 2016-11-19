import numpy as np

# L (bande verticali)
# Variabili
# ---------

# mm, fenditura schermo
L = [780.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0] 
# mm, diametro banda nera
d = np.array([19.7, 16.9, 15.7, 14.2, 12.0, 10.5, 9.1, 8.3, 7.7, 6.0, 4.2]) / 2.0

# Calcoli
# -------
ran = 11
lam = 632.8 * (10e-7)
theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	theta[i] = np.arctan2((d[i] / 2), L[i])
D = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	D[i] = ((2.0 * lam) / np.sin(theta[i]))

# Print
# -----

print("- - - - Fenditura orizzontale (primo minimo) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*L))
print("x (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*d))
print("theta (rad):      {:.4f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*theta))
print("l (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*D))


# H (bande orizzontali)
# Variabili
# ---------

# mm, fenditura schermo
op_L = [780.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0] 
# mm, diametro banda nera
op_d = np.array([16.3, 14.7, 13.1, 12.1, 10.8, 9.0, 8.1, 7.3, 6.3, 5.0, 3.3]) / 2

# Calcoli
# -------
op_theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_theta[i] = np.arctan2((op_d[i] / 2), op_L[i])
op_D = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_D[i] = ((2.0 * lam) / np.sin(op_theta[i]))

# Print
# -----

print("- - - - Fenditrura orizzontale (secondo minimo) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*op_L))
print("x (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*op_d))
print("theta (rad):      {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_theta))
print("h (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_D))
