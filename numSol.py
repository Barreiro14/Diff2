import math
import numpy as np
from graph import Graph


def NumSol(E, T):
    def ψ0(x):
        #condiciones iniciales de la solucion numerica
        return 1.08*(np.tanh(100*(x+0.001)) - np.tanh(100*(x-0.001)))

    L = 10
    Nx = 99
    Nt = 15
    x = np.linspace(-L, L, Nx + 1)
    dx = x[1] + x[0]
    t = np.linspace(0, T, Nt + 1)
    dt = t[1] - t[0]
    #F = dt/dx**2
    F = 0.25 #TODO: find a way to fix f to 0.25 without manually doing it
    ψ = np.zeros(Nx + 1)
    ψ_n = np.zeros(Nx + 1)

    for i in range(0, Nx + 1):
        ψ_n[i] = ψ0(x[i])

    for t in range(1, Nt):
        for i in range(1, Nx):
            ψ[i] = ψ_n[i] + F*(ψ_n[i+1] - 2*ψ_n[i] + \
                ψ_n[i-1] + 2*E*((ψ_n[i]*ψ_n[i-1] + \
                    (ψ_n[i+1]**2) - (ψ_n[i]**2) - \
                        (ψ_n[i]*ψ_n[i+1]))))

        ψ[0] = 0; ψ[Nx] = 0
        ψ_n[:] = ψ
        ψ = ψ/(2.19791091e-9) #TODO: find a way to better normalize the function
        print("para t={}".format(dt*t), ψ)
        Graph(ψ, x, t*dt, E, 1)
    
    
