import numpy as np
import matplotlib.pyplot as plt


def Graph(ψ, l, t, E):
    #x = np.linspace(0, l)
    f = lambda x, t, E: 1/((4*np.pi*t)**(1/2))*np.exp(-x**2/(4*t)) + E*((x**2) - t)/(4*(np.pi**(1/2))*(t**(3/2)))*np.exp(-(x**2)/(2*t)) - (E**2)*((x**2)/2)*(9*(x**4)-39*t*(x**2)+14*(t**2))/(32*np.pi*(t**4))*np.exp(-3*(x**2)/(4*t))
    plt.plot(l, f(l, t-0.9, E), '-g', label="Analythical")
    plt.plot(l, ψ, '-b', label="Numerical")
    plt.title("Analythical solution up to 2nd perturbation", loc = 'left')
    plt.legend(["Analythical", "Numerical"])
    plt.xlabel("x")
    plt.ylabel("ψ(x, {}t)".format(t))
    plt.ylim([0, 2.5])
    plt.grid()
    plt.show()

#f = lambda x, t, E: 1/((4*np.pi*t)**(1/2))*np.exp(-x**2/(4*t)) + E*((x**2) - t)/(4*(np.pi**(1/2))*(t**(3/2)))*np.exp(-(x**2)/(2*t)) - (E**2)*((x**2)/2)*(9*(x**4)-39*t*(x**2)+14*(t**2))/(32*np.pi*(t**4))*np.exp(-3*(x**2)/(4*t))


#Graph(f, 1, 0.1, 0.00001)