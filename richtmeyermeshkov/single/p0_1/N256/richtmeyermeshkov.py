def init_global(rho, ux, uy, uz, p, nx, ny, nz, ax, ay, az, bx, by, bz):
    x = linspace(ax, bx, nx)
    y = linspace(ay, by, ny)
    z = linspace(az, bz, nz)
    Y, X, Z = meshgrid(y, x, z)


    XC = X - 0.5
    YC = Y - 0.5
    ZC = Z - 0.5

    R = sqrt(XC**2+YC**2+ZC**2)

    Theta = arctan2(ZC, YC)
    Phi = arctan2(XC, YC)

    N = int(len(a)/4)

    a1 = a[:N]
    b1 = a[N:2*N]
    a2 = a[2*N:3*N]
    b2 = a[3*N:4*N]

    normalization1 = sum(a1)
    if abs(normalization1) < 1e-8:
        normalization1 = N

    normalization2 = sum(a2)
    if abs(normalization2) < 1e-8:
        normalization2 = N

    perturbation = epsilon * sum([a1[n] * cos(Phi+2*pi*b1[n]) for n in range(N)], 0) / normalization1
    
    perturbation += epsilon * sum([a2[n] * cos(Theta+2*pi*b2[n]) for n in range(N)], 0) / normalization2

    inner_01 = (R < 0.1)

    inner_025 = (R < 0.25 + perturbation)
    
    p[:,:,:] = 20.0 * inner_01 + 1.0 * (1-inner_01)

    rho[:,:,:] = 2.0 * inner_025 + 1.0 * (1-inner_025)
    ux[:,:,:] = zeros_like(X)
    uy[:,:,:] = zeros_like(X)
    uz[:,:,:] = zeros_like(X)




