import numpy as np
import math
import matplotlib.pyplot as plt
import unicodedata

def throwDarts(cirlceDarts,times):
    throwsX = np.random.rand(times)
    throwsY = np.random.rand(times)
    throwsX = [x - 0.5 for x in throwsX]
    throwsY = [y - 0.5 for y in throwsY]
    # print(throwsX)
    # print(throwsY)
    trials = range(1000)
    checkDarts(throwsX,throwsY, cirlceDarts,trials)

def checkDarts(xPoints, yPoints, circleDarts,trials):
    probabilities = []
    i = 1
    for x, y in zip(xPoints, yPoints):
        if math.sqrt(x ** 2 + y ** 2) <= 0.5:
            circleDarts.append(1)
        else:
            circleDarts.append(0)
        probability = np.sum(circleDarts) / len(circleDarts)
        probability = probability * 4
        probabilities.append(probability)
        print("Trial " + str(i)+ " -> " + "Probability is: " + str(probability))
        i = i+1
    plt.plot(trials, probabilities)
    plt.xlabel('# of Monte Carlo Samples')
    plt.ylabel('Estimate of ' + unicodedata.lookup("GREEK SMALL LETTER PI"))
    plt.title('Estimate of ' + unicodedata.lookup("GREEK SMALL LETTER PI")+ ' vs. # of Monte Carlo Samples')
    plt.show()

if __name__ == '__main__':
    print("test")
    circleDarts = []
    throwDarts(circleDarts,1000)
