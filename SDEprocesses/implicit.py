import numpy as np
import exceptions as ex

#Винеровская с.в
def dW(dt):
    return np.random.randn()*np.sqrt(dt)

# 2. Стохастическое дифференциальное уравнение в неявном виде

def a(x, t):
    return 0

def b(x, t):
    return t

def stoch_proc(T, nSteps, a, b, x_0=1, t_0=0, boundary=500):

    ex._check_params(T, nSteps, t_0)

    x_t = []
    t = t_0
    dt = T*/(10*nSteps)
    x = x_0
    x_t.append(x_0)
    
    for i in range(1, 10*nSteps):
        t += dt
        x += a(x_t[i], t)*dt + b(x_t[i], t)*dW(dt)
		if abs(x) > boundary:
            raise Warning("Risk of going beyond the definition of a random process. Boundary: " + str(boundary) + ". If You wish You could change boundary conditions in parameters (default:'boundary'=500).")
        x_t.append(x)
        
    return x_t

# 3. Логарифмическое блуждание

def LogWalk(T, nSteps, _mu, _sigma, x_0=1, t_0=0, boundary=500):
    def mu(x, t):
        return _mu*x
    
    def sigma(x, t):
        return _sigma*x
    
    return stoch_proc(T, nSteps, mu, sigma, x_0=1, t_0=0, boundary)

# 4. Процесс Орнштейна-Уленбека

def OrnsteinUlenbekProcess(T, nSteps, alpha, beta, _sigma, x_0=1, t_0=0, boundary=500):
   
    def mu(x, t):
        return -beta*(x - alpha)
    
    def sigma(x, t):
        return _sigma
    
    return stoch_proc(T, nSteps, mu, sigma, x_0=1, t_0=0, boundary)

# 5. Броуновская ловушка

def BrownianTrap(T, nSteps, alpha, beta, _sigma, x_0=1, t_0=0, boundary=500):
   
    def mu(x, t):
        return -beta*(x - alpha)
    
    def sigma(x, t):
        return _sigma*(x - alpha)
    
    return stoch_proc(T, nSteps, mu, sigma, x_0=1, t_0=0, boundary)

# 6. Броуновский мост

def BrownianBridge(T, nSteps, alpha, _sigma, x_0=1, t_0=0, boundary=500):
   
    def mu(x, t):
        return -(x - alpha)/(T - t)
    
    def sigma(x, t):
        return _sigma
    
    return stoch_proc(T, nSteps, mu, sigma, x_0=1, t_0=0, boundary)


