import numpy as np
import exceptions as ex


def DampedOscillator(T, nSteps, sigma, lambda_, omega, x_0, y_0, t_0=0):
    
	ex._check_params(T, nSteps, t_0)

	x_t, y_t = [], []
    t=t_0
    dt = T/(10*nSteps)
    x_t.append(x_0)
    y_t.append(y_0)
    
    for i in range((10*nSteps)):
        x_average = np.exp(-lambda_*t) * (x_0*np.cos(omega*t) - y_0*np.sin(omega*t))
        y_average = np.exp(-lambda_*t) * (x_0*np.sin(omega*t) + y_0*np.cos(omega*t))
        
        x = x_average + sigma/np.sqrt(2*lambda_) * np.random.normal()*np.sqrt(1 - np.exp(-2*lambda_*t))   
        y = y_average + sigma/np.sqrt(2*lambda_) * np.random.normal()*np.sqrt(1 - np.exp(-2*lambda_*t))
        
        t += dt
        x_t.append(x)
        y_t.append(y)
    
    return x_t, y_t


def linear_system(T, nSteps, x_0, y_0, t_0=0):
   
	ex._check_params(T, nSteps, t_0)

    t=t_0
    dt=T/(10*nSteps) 
    x_t=[]
    y_t=[]
    
    for i in range((10*nSteps)):
        eps=np.random.normal(0)
        x = x_0+eps*np.sqrt(t)
        
        y = y_0 + x_0*np.random.normal(0)*np.sqrt(t)+(1/2)*(np.random.normal(0)*np.random.normal(0)-1)*t
        
        t += dt
        x_t.append(x)
        y_t.append(y)
 
    return x_t, y_t


def correlated_wandering(T, nSteps, ro, sigma, x_0, t_0=0):

	ex._check_params(T, nSteps, t_0)

    t=t_0
    dt = T/(10*nSteps)
    
    x_t = []
    y_t = []
    x=x_0
    
    for i in range((10*nSteps)):
        nu = np.random.normal(1)
        zeta = ro*nu+np.sqrt(1-ro*ro)*np.random.normal(1)
        x = x_0 + sigma*nu*np.sqrt(t)
        y = x_0 + sigma*zeta*np.sqrt(t)
        t += dt
        x_t.append(x)
        y_t.append(y)

    return x_t, y_t

