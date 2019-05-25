epsilon = 6e-2
xc = x - 0.5
yc = y - 0.5
zc = z - 0.5
phi = atan2(yc, xc) if abs(xc) > 0 else 0
psi = atan2(zc, xc) if abs(xc) > 0 else 0

if phi < 0:
    phi += 2*pi

N = len(a)/4

a1 = a[:N]

b1 = a[N:2*N]

a2 = a[2*N, 3*N]

b2 = a[3*N, 4*N]

normalization1 = sum(a1)

if abs(normalization1) < 1e-8:
    normalization1 = N

perturbation = epsilon * sum([a1[n] * cos(phi+2*pi*b1[n]) for n in range(N)]) / normalization1

perturbation += epsilon * sum([a2[n] * cos(phi+2*pi*b2[n]) for n in range(N)]) / normalization2


r = sqrt((xc)**2+(yc)**2 + (zc)**2)
if r < 0.1:
    p = 20
else:
    p = 1

if r < 0.25 + perturbation:
    rho = 2
else:
    rho = 1
ux = 0
uy = 0
uz = 0



