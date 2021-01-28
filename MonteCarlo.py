import numpy as np
import math
import matplotlib.pyplot as plt
import unicodedata

goodEstimates = []
trials = 1000
runs = 4

def throwDarts(cirlceDarts,times):
    # Calculates random throws
    throwsX = np.random.rand(times)
    throwsY = np.random.rand(times)
    throwsX = [x - 0.5 for x in throwsX]
    throwsY = [y - 0.5 for y in throwsY]
    # print(throwsX)
    # print(throwsY)
    checkDarts(throwsX,throwsY, cirlceDarts)

def checkDarts(xPoints, yPoints, circleDarts):
    goodEstimate = "";
    threshold = 0.005
    estimates = []
    i = 1
    for x, y in zip(xPoints, yPoints):
        if math.sqrt(x ** 2 + y ** 2) <= 0.5:
            circleDarts.append(1)
        else:
            circleDarts.append(0)
        estimate = np.cumsum(circleDarts)[-1]/ len(circleDarts)
        estimate = estimate * 4
        if math.pi-threshold <= estimate <= math.pi+threshold  and not goodEstimate :
            goodEstimate = [("Trial " + str(i)+ " -> " + "Estimate is: " + str(estimate)),(i),(estimate)]
        estimates.append(estimate)
        # print("Trial " + str(i)+ " -> " + "estimate is: " + str(estimate))
        i = i+1

    # Code for the case where there was no good estimate
    if not goodEstimate:
        # Calculate the closest value to pi and return that sample and estimate
        i = 1
        min = [(10),(0)]
        for val in estimates:
            if(abs(val -math.pi) < abs(min[0] - math.pi)):
                min = [(val),(i)]
            i = i+1
        goodEstimate = [(""), (min[1]), (min[0])]

    # Code for plotting
    x = range(trials)
    plt.plot(x, estimates, label = 'Estimated ' + unicodedata.lookup("GREEK SMALL LETTER PI"))
    pi = [math.pi]*trials
    plt.plot(x, pi, label = unicodedata.lookup("GREEK SMALL LETTER PI"))
    plt.xlabel('# of Monte Carlo Samples')
    plt.ylabel('Estimate of ' + unicodedata.lookup("GREEK SMALL LETTER PI"))
    plt.title('Estimate of ' + unicodedata.lookup("GREEK SMALL LETTER PI")+ ' vs. # of Monte Carlo Samples')
    plt.legend()
    # plt.savefig('Estimate.jpg')
    plt.show()

    goodEstimates.append(goodEstimate)

if __name__ == '__main__':
    # Code for creating the plot for one test
    circleDarts = []
    throwDarts(circleDarts, trials)


    # Code for creating the plot for 4 addional tests
    for x in range(runs):
        circleDarts = []
        throwDarts(circleDarts,trials)

    # Code printing out how many samples are needed for a good estimate individually (also prints out the sample estimate for the first test)
    for tuple in goodEstimates:
        if tuple[0]:
            print(tuple[0])
        else:
            print("No trial was close enough for a good estimate, however, this was the closest: " + ("Trial " + str(tuple[1])+ " -> " + "Estimate is: " + str(tuple[2])))

    # Code for figuring out how many samples are needed for a good estimate when all 5 experiments are considered in aggregate
    sum = 0
    for tuple in goodEstimates:
        sum = sum + tuple[1]
    print(str(sum/len(goodEstimates)) + " Monte Carlo samples are needed to arrive at a good estimate of " + unicodedata.lookup("GREEK SMALL LETTER PI"))

