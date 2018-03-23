N = len(a)/60
a1 = a[:10]
a2 = a[10:20]
a3 = a[20:30]
b1 = a[30:40]
b2 = a[40:50]
b3 = a[50:60]



GAMMA=5.0/3.0

k = 1
u0 = 1

p_inf = 100
perturbation = 0.05
normalization1 = sum(a1)
if abs(normalization1) < 1e-10:
	normalization1 = 1
normalization2 = sum(a2)
if abs(normalization2) < 1e-10:
	normalization2 = 1
normalization3= sum(a3)
if abs(normalization3) < 1e-10:
	normalization3 = 1

perturbation_x = perturbation*sum([a1[i]*cos(2*pi*(i+1)*(x+b1[i])) for i in range(len(a1))])/normalization1
perturbation_y = perturbation*sum([a2[i]*cos(2*pi*(i+1)*(x+b2[i])) for i in range(len(a2))])/normalization2
perturbation_z = perturbation*sum([a3[i]*cos(2*pi*(i+1)*(x+b3[i])) for i in range(len(a3))])/normalization3

x_p = x + perturbation_x
y_p = y + perturbation_y
z_p = z + perturbation_z
ux = u0 * sin(2*pi*k*x_p)*cos(2*pi*k*y_p)*cos(2*pi*k*z_p)
uy = -u0 * cos(2*pi*k*x_p)*sin(2*pi*k*y_p)*cos(2*pi*k*z_p)
uz = 0

rho = 1
p = p_inf + 1.0/16.0*rho*u0**2 * (2 + cos(4*pi*k*z_p))*(cos(4*k*pi*x_p) + cos(4*pi*k*z_p))

