import numpy as np
import matplotlib.pyplot as plt


def Graph(ψ, l, t, E, s):
    #x = np.linspace(0, l)
    f = lambda x, t, E: 1/((4*np.pi*t)**(1/2))*np.exp(-x**2/(4*t)) + \
        E*((x**2) - t)/(4*(np.pi**(1/2))*(t**(3/2)))*np.exp(-(x**2)/(2*t)) - \
        (E**2)*((x**2)/2)*(9*(x**4)-39*t*(x**2)+14*(t**2))/(32*np.pi*(t**4))*np.exp(-3*(x**2)/(4*t))
    F = lambda x, t: 1/((4*np.pi*t)**(1/2))*np.exp(-x**2/(4*t))
    plt.plot(l, s*f(l, t, E), '-g', label="Analytical non linear")
    plt.plot(l, ψ, '-b', label="Numerical")
    plt.plot(l, s*F(l, t), '-r', label="Analythical linear")
    plt.title("Ɛ = {}".format(E), loc = 'left')
    plt.legend(["Analytical 2nd perturbation", "Numerical", "Analytical linear"])
    plt.xlabel("x")
    plt.ylabel("ψ(x, {}t)".format(t))
    plt.ylim([0, 0.8])
    plt.xlim([l[0], l[-1]])
    plt.grid()
    plt.show()

