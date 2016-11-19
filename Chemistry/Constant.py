import numpy as np

# Define Avogadro's number
Na = 6.022140857 * (10**23) 

# Define an "object" element with the properties: el(electrons), 
# pr(protons), ne(neutrons) and mW(molecular weight).

class element(object) :
	def __init__(self, el, pr, ne, mW, Name) :
		self.electrons = el
		self.protons = pr
		self.neutrons = ne
		self.name = Name
		self.molW = mW
		# Define primitive orbital configuration
		self.orbConfig = np.zeros((28), dtype=np.int).reshape(7,4)
		# State function
		if self.electrons != self.protons :
			if self.protons > self.electrons :
				self.isCation = True
			elif self.protons < self.electrons :
				self.isAnion = True	
		# Orbital function - for now max 12 electrons
	

# Elements (electrons, protons, neutrons, molecuar weight, name)	
H = element(1, 1, 0, 1.00794, "Hydrogen")
He = element(2, 2, 2, 4.002602, "Helium")
Li = element(3, 3, 4, 6.941, "Lithium")
Be = element(4, 4, 5, 9.01218, "Beryllium")
B = element(5, 5, 6, 10.81, "Boron")
C = element(6, 6, 6, 12.011, "Carbon")
N = element(7, 7, 7, 14.007, "Nitrogen")
O = element(8, 8, 8, 15.999, "Oxygen")
F = element(9, 9, 10, 18.998403163, "Fluorine")
Ne = element(10, 10, 10, 20.1797, "Neon")
Na = element(11, 11, 12, 22.98976928, "Sodium")
Mg = element(12, 12, 12, 24.305, "Magnesium")
Al = element(13, 13, 14, 26.9815385, "Aluminium")
Si = element(14, 14, 14, 28.085, "Silicon")
P = element(15, 15, 16, 30.973761998, "Phosphorus")
S = element(16, 16, 16, 32.06, "Sulfur")
Cl = element(17, 17, 18, 35.45, "Chlorine")
Ar = element(18, 18, 22, 39.948, "Argon")
K = element(19, 19, 20, 39.0983, "Potassium")
Ca = element(20, 20, 20, 40.078, "Calcium")
Sc = element(21, 21, 24, 44.9559008, "Scandium")
Ti = element(22, 22, 26, 47.867, "Titanium")
V = element(23, 23, 28, 50.9415, "Vanadium")
Cr = element(24, 24, 28, 51.9961, "Chromium")
Mn = element(25, 25, 30, 54.9380044, "Manganese")
Fe = element(26, 26, 30, 55.845, "Iron")
Co = element(27, 27, 32, 58.933194, "Cobalt")
Ni = element(28, 28, 30, 58.6934, "Nickel")
Cu = element(29, 29, 24, 63.546, "Copper")
Zn = element(30, 30, 34, 65.38, "Zinc")
Ga = element(31, 31, 38, 69.723, "Gallium")
Ge = element(32, 32, 42, 72.630, "Germanium")
As = element(33, 33, 42, 74.921595, "Arsenic")
Se = element(34, 34, 46, 78.971, "Selenium")
Br = element(35, 35, 44, 79.904, "Bromine")
Kr = element(36, 36, 48, 83.798, "Krypton")
Rb = element(37, 37, 48, 85.4678, "Rubidium")
Sr = element(38, 38, 50, 87.62, "Strontium")
Y = element(39, 39, 50, 88.90584, "Yttrium")
Zr = element(40, 40, 50, 91.224, "Zirconium")
Nb = element(41, 41, 52, 92.90637, "Niobium")
Mo = element(42, 42, 56, 95.95, "Molybdenum")
Tc = element(43, 43, 55, 98.0, "Technetium")
Ru = element(44, 44, 58, 101.07, "Ruthenium")
Rh = element(45, 45, 58, 102.90550, "Rhodium")
Pd = element(46, 46, 60, 106.42, "Palladium")
Ag = element(47, 47, 60, 107.8682, "Silver")
Cd = element(48, 48, 66, 112.414, "Cadmium")
In = element(49, 49, 66, 144.818, "Indium")
Sn = element(50, 50, 70, 118.710, "Tin")
Sb = element(51, 51, 70, 121.760, "Antimony")
Te = element(52, 52, 78, 127.60, "Tellirium")
I = element(53, 53, 76, 126.9044, "Iodine")
Xe = element(54, 54, 78, 131.293, "Xenon")
Cs = element(55, 55, 78, 132.905, "Caesium")
Ba = element(56, 56, 81, 137.327, "Barium")
La = element(57, 57, 82, 138.90547, "Lanthanum")
Ce = element(58, 58, 82, 140.116, "Cerium")
Pr = element(59, 59, 82, 140.90766, "Praseodyum")
Nd = element(60, 60, 80, 144.242, "Neodyum")
Pm = element(61, 61, 86, 145.0, "Promethium")
Sm = element(62, 62, 90, 150.36, "Samarium")
Eu = element(63, 63, 90, 151.964, "Europium")
Gd = element(64, 64, 94, 157.25, "Gadolinium")
Tb = element(65, 65, 94, 158.92535, "Terbium")
Dy = element(66, 66, 98, 162.500, "Dysprosium")
Ho = element(67, 67, 98, 164.93033, "Holmium")
Er = element(68, 68, 98, 167.259, "Erbium")
Tm = element(69, 69, 100, 168.93422, "Thulium")
Yb = element(70, 70, 104, 173.045, "Ytterbium")
Lu = element(71, 71, 104, 174.9668, "Lutetium")
Hf = element(72, 72, 106, 178.49, "Hafnium")
Ta = element(73, 73, 108, 180.94788, "Tantalum")
W = element(74, 74, 110, 183.84, "Tungsten")
Re = element(75, 75, 112, 186.207, "Rhenium")
Os = element(76, 76, 116, 190.23, "Osmium")
Ir = element(77, 77, 116, 192.21, "Iridium")
Pt = element(78, 78, 116, 195.084, "Platinum")
Au = element(79, 79, 118, 196.966569, "Gold")
Hg = element(80, 80, 122, 200.592, "Mercury")
Tl = element(81, 81, 124, 204.38, "Thallium")
Pb = element(82, 82, 126, 207.2, "Lead")
Bi = element(83, 83, 126, 208.98040, "Bismuth")
Po = element(84, 84, 126, 209.0, "Polonium")
At = element(85, 85, 126, 210.0, "Astatine")
Rn = element(86, 86, 126, 222.0, "Radon")


print(H.orbConfig)

for x in np.nditer(H.orbConfig) : 
	print(x)