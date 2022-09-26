import matplotlib.pyplot as plt
import json


def plotter():
    fitness_results = json.loads(open('out.txt', encoding='utf8').read())
    number_of_generations = len(fitness_results['min'])
    x = [i for i in range(number_of_generations)]
    fig, ax = plt.subplots(nrows=3, figsize=(10, 10))
    ax[0].plot(x, fitness_results['min'])
    ax[0].set(title="Min")
    ax[1].plot(x, fitness_results['max'])
    ax[1].set(title="Max")
    ax[2].plot(x, fitness_results['mean'])
    ax[2].set(title="Mean")
    fig.tight_layout(pad=3)
    plt.show()


plotter()
