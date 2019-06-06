import numpy as np
import exceptions as ex

def LogWalk(T, nSteps, mu, sigma, x_0=1, t_0=0, boundary=500):

    ex._check_params(T, nSteps, t_0)
    dt = T/(10*nSteps)
    x_t = []
    t = t_0
    for i in range((10*nSteps)):
       
        x = x_0*np.exp((mu - sigma**2/2)*t + sigma*np.random.randn()*np.sqrt(t))
		if abs(x) > boundary:
            raise Warning("Risk of going beyond the definition of a random process. Boundary: " + str(boundary) + ". If You wish You could change boundary conditions in parameters (default:'boundary'=500).")
        x_t.append(x) 
        t += dt

    return x_t

# 4. Процесс Орнштейна-Уленбека

def OrnsteinUlenbekProcess(T, nSteps, alpha, beta, _sigma, x_0=1, t_0=0, boundary=500):
    ex._check_params(T, nSteps, t_0)

    dt = T/(10*nSteps)
    x_t = []
    x_t.append(x_0)
    t = t_0
    
    for i in range(1, 10*nSteps):
        x = alpha + (x_0 - alpha)*np.exp(-beta*t) + _sigma/np.sqrt(2*beta)*np.sqrt(1-np.exp(-2*beta*t))*np.random.randn()
		if abs(x) > boundary:
            raise Warning("Risk of going beyond the definition of a random process. Boundary: " + str(boundary) + ". If You wish You could change boundary conditions in parameters (default:'boundary'=500).")
        x_t.append(x)
        t += dt
    return x_t

# 6. Броуновский мост

def BrownianBridge(T, nSteps, alpha, _sigma, x_0=1, t_0=0, boundary=500):

    ex._check_params(T, nSteps, t_0)	

    dt = T/(10*nSteps)
    x_t = []
    x_t.append(x_0)
    t = t_0
    
    for i in range(1, 10*nSteps):
        x = alpha + (x_0 - alpha)*(T - t)/(T - t_0) + _sigma*np.sqrt((t - t_0)*(T - t)/T - t_0)*np.random.randn()
		if abs(x) > boundary:
            raise Warning("Risk of going beyond the definition of a random process. Boundary: " + str(boundary) + ". If You wish You could change boundary conditions in parameters (default:'boundary'=500).")
        x_t.append(x)
        t += dt
    return x_t
