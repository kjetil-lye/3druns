def init_global(rho, ux, uy, uz, p, nx, ny, nz, ax, ay, az, bx, by, bz):
    N = int(len(a)/4)
    a1 = a[:N]
    a2 = a[N:2*N]
    b1 = a[2*N:3*N]
    b2 = a[3*N:4*N]

    perturbation=epsilon
    normalization1 = sum(a1)
    if abs(normalization1) < 1e-10:
        normalization1 = 1
    normalization2 = sum(a2)
    if abs(normalization2) < 1e-10:
        normalization2 = 1

    x = linspace(ax, bx, nx)
    y = linspace(ay, by, ny)
    z = linspace(az, bz, nz)
    Y, X, Z = meshgrid(y, x, z)
    X = X
    Y = Y
    Z = Z

    R = sqrt((Y - 0.5)**2 + (Z - 0.5)**2)

    Theta = arctan2((Z-0.5), (Y-0.5))
    perturbation_radius = perturbation*sum([a1[i]*cos(2*pi*(i+1)*(X+b2[i]))*cos(2*pi*(i+1)*(Theta+b1[i])) for i in range(len(a1))], 0)/normalization1
    perturbation_radius /= 2

    middle = (R < 0.25 + perturbation_radius)

    rho[:, :, :] = 2.0 * middle + 1.0*(1-middle)
    ux[:, :, :] = -0.5*middle + 0.5*(1-middle)
    uy[:,:,:] = zeros_like(X)
    uz[:,:,:] = zeros_like(X)
    p[:,:,:] = 2.5*ones_like(X)
