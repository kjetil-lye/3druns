epsilon = 0.01
if x < 0.04 + 5 * epsilon * X[0]:
    rho = 3.86859 + 0.1 * X[1];
    ux = 11.2536;
    p = 167.345 + 5 * X[2]
else:
    r = (x-0.25)**2 + (y-0.5)**2 + (z-0.5)**2;
    phi = (x-0.25) / sqrt(r);
    xi  = (y-0.5)  / sqrt(r);
    r_max = ( 0.13 + 10 * epsilon * X[3] * sin(phi) + 5 *epsilon * X[4] * sin(10*phi) + 5 * epsilon * X[5] * sin(10*xi) )**2
    if r <= r_max:
      rho = 10.0;
      rho += 0.5 * X[6];
      rho += 1.0 * X[7] * sin(4*(x-0.25));
      rho += 0.5 * X[8] * cos(8*(y-0.5));
      rho += 1.0 * X[9] * sin(6*(z-0.5));
    else:
      rho = 1.0;
    p = 1.0;
  
