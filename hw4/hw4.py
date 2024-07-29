import numpy as np
import math
import matplotlib.pyplot as plt

def DAG_model(force_y_to_1=False):
    probabilities = []
    N_values = []
    for N in range(10, 10001, 10): 
        Y1 = 0
        Z1_given_Y1 = 0
        for _ in range(N):
            
            x = np.random.binomial(n=1, p=0.5)

            # Define simulation and intervention conditions
            if force_y_to_1 == True:
                y = 1
                condition = 'intervention'
            else:
                y = np.random.binomial(n=1, p=math.e**(4*x-2) / (1+math.e**(4*x-2)))
                condition = 'simulation'

            z = np.random.binomial(n=1, p=(math.e**(2*(x+y)-2) / (1+math.e**(2*(x+y)-2))))
            
            if y == 1:
                Y1 += 1
                if z == 1:
                    Z1_given_Y1 += 1

        if Y1 != 0:
            pr = Z1_given_Y1 / Y1        #proportion of the time where z is 1 given that y is 1
        else:
            pr = 0.0
        
        probabilities.append(pr)
        N_values.append(N)

    convergence_value = probabilities[len(probabilities)-1]

    # Plot Pr(Z=1 | Y=1) as a function of N
    plt.figure()
    plt.plot(N_values, probabilities, label = 'Pr(Z=1 | Y=1)')
    plt.plot(N_values, [convergence_value]*len(N_values), label = f'Convergence value = {convergence_value:.3f}')
    plt.xlabel('Simulation Size N')
    plt.ylabel('Probability')
    plt.title(f'Pr(Z=1 | Y=1) vs N: {condition}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{condition}.png')
    # plt.show()
    
simulation = DAG_model()
intervention = DAG_model(force_y_to_1=True)
