# 6.00.2x Problem Set 4

import random
import pdb 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt 
from ps3b_precompiled_27 import *
from ps3b import *


#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    #finalPopulation = []
    #for i in xrange(numTrials):
        #finalPopulation.append(simulationWithDrug(
            #numViruses=100,
            #maxPop=1000,
            #maxBirthProb=.1,
            #clearProb=.05,
            #resistances={"guttaganol":False},
            #mutProb=.005,
            #numTrials=1,
            #timeSteps=400,
            #timeAddPrescription=treatmentTime
            #)[-1])
    #return finalPopulation
        


    # example data
    #mu = 100 # mean of distribution
    #sigma = 15 # standard deviation of distribution
    #x = mu + sigma * np.random.randn(10000)
    
    # finalPopulation avg,stdev



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    finalPopulation = []
    for i in xrange(numTrials):
        finalPopulation.append(simulationWithDrug(
            numViruses=100,
            maxPop=1000,
            maxBirthProb=.1,
            clearProb=.05,
            resistances={"guttaganol":False, "grimpex":False},
            mutProb=.005,
            numTrials=1,
            timeSteps=450,
            timeAddPrescription=treatmentTime,
            timeAddPrescription2=treatmentTime2,
###input drugs here
            firstPrescription="grimpex",
            secondPrescription="guttaganol"
            )[-1])
    return finalPopulation


def main():

    global treatmentTime
    global treatmentTime2
### input treatment times here
    treatmentTime = 150
    treatmentTime2 = 150
## input no. of trials and pick simulation here:
    finalPopulation = simulationTwoDrugsDelayedTreatment(
            numTrials=100
            )

    sigma = numpy.std(finalPopulation)
    mu = numpy.average(finalPopulation)
    num_bins = 10
    x_limit = 1000

    
### plot histogram
    plt.figure()
    #plt.subplot(211)
    n, bins, patches = plt.hist(finalPopulation, 
            bins=np.arange(0, 1000, 50), 
            normed=False, 
            cumulative=False, 
            facecolor='green'
            )


    # formatting
    plt.xticks(np.arange(0, x_limit, x_limit/num_bins))
    plt.ylim([0,120])
    plt.xlim([0,x_limit])
    plt.xlabel('Number of Viruses') 
    plt.ylabel('Number of Patients')
    plt.title(r'Final Virus Pop in Patient')
    plt.grid(True)

### plot CDF
    #plt.subplot(212)
    #n, bins, patches = plt.hist(finalPopulation, num_bins, normed=True, cumulative=True, facecolor='green')

    ## insert fit line
    #y = mlab.normpdf(bins, mu, sigma).cumsum()
    ##y /= y[-1]
    #plt.plot(bins,y,'k--', linewidth=1.5)

    ## formatting
    #plt.xticks(np.arange(0, x_limit, 50))
    #plt.subplots_adjust(hspace=.5)
    #plt.ylim([0,1.05])
    #plt.xlim([0,x_limit])
    #plt.xlabel('Cumulative Number of Viruses') 
    #plt.ylabel('Percentage of Patients')
    #plt.title(r'Virus Pop in Patients CDF treatmentTime = %d treatmentTime2 = %d' % (
        #treatmentTime, 
        #treatmentTime2
        #)
    #) 
    #plt.grid(True)

    plt.subplots_adjust(hspace=.6)

    plt.show()

if __name__ == "__main__":
    main()
