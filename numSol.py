import numpy as np
from graph import Graph
def ψ0(x):
    #condiciones iniciales de la solucion numerica
    return 1.08*(np.tanh(100*(x-0.25)) - np.tanh(100*(x-0.26)))

def NumSol(E, T):
    L = 10
    Nx = 99
    Nt = 10
    x = np.linspace(-L, L, Nx + 1)
    dx = x[1] - x[0]
    t = np.linspace(0, T, Nt + 1)
    dt = t[1] - t[0]
    F = dt/dx**2
    ψ = np.zeros(Nx + 1)
    ψ_n = np.zeros(Nx + 1)

    for i in range(0, Nx + 1):
        ψ_n[i] = ψ0(x[i])

    for T in range(1, Nt):
        for i in range(1, Nx):
            ψ[i] = ψ_n[i] + F*(ψ_n[i-1] - 2*ψ_n[i] + ψ_n[i+1]) + \
                + 2*E*F*((ψ_n[i-1] - ψ_n[i])**2) + 2*E*ψ_n[i]*F*(ψ_n[i-1] - 2*ψ_n[i] + ψ_n[i+1])

        ψ[0] = 0; ψ[Nx] = 0
        ψ_n[:] = ψ
        print("para t={}".format(T), ψ)
        Graph(ψ, x, T, E)
    
    
    #Graph(ψ, x, T, E)

NumSol(0.1, 10)