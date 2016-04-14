import numpy as np
import scipy.integrate as spIn
import matplotlib.pyplot as plt

def ode_system(y,t,a,b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1),b*(-y1 + y0*y1)]
    return dydt

if __name__ == "__main__":

    # part 1
    # initial value for y0 and y1 and the value for a and b
    a = 1.0
    b = 0.2
    initial_y0 = 0.1
    initial_y1 = 1.0
    initial_y = [initial_y0,initial_y1]
    # partitioning the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    #solving the nonlinear ODE system
    sol = spIn.odeint(ode_system,initial_y,t,args=(a,b))

    # plotting the graph for both y0 and y1 against t
    plt.plot(t, sol[:, 0], 'r', label='y0 against t')
    plt.plot(t, sol[:, 1], 'b', label='y1 against t')
    plt.title('y against t with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'r', label='y1 against y0')
    plt.title('y1 against y0 with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.grid()
    plt.show()
    

    # part 2 (To observe the sensitivity)
    # initial value for y0 and y1 and the value for a and b
    a = 1.0
    b = 0.2
    # different initial value for initial_y0
    initial_y0 = 0.11
    initial_y1 = 1.0
    initial_y = [initial_y0,initial_y1]
    # partitioning the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    #solving the nonlinear ODE system
    sol = spIn.odeint(ode_system,initial_y,t,args=(a,b))

    # plotting the graph for both y0 and y1 against t
    plt.plot(t, sol[:, 0], 'r', label='y0 against t')
    plt.plot(t, sol[:, 1], 'b', label='y1 against t')
    plt.title('y against t with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'r', label='y1 against y0')
    plt.title('y1 against y0 with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.grid()
    plt.show()
