# virus_simulation
a stochastic simulation from edx.org

The two files you want to use are ps3b.py and ps4.py 

to configure files for different populations / prescription times edit the following entries

ps3b.py 
"""
566     timeSteps = 450
567     timeAddPrescription = 0
568     timeAddPrescription2 = 150
569     firstPrescription = "grimpex"    ### the name doesn't matter
570     secondPrescription = "guttaganol"  ### the name doesn't matter
571     maxPop = 1000
572     numTrials = 100
"""

ps4.py
"""
 96 ### input treatment times here
 97     treatmentTime = 150
 98     treatmentTime2 = 150
 99 ## input no. of trials and pick simulation here:
100     finalPopulation = simulationTwoDrugsDelayedTreatment(
101             numTrials=100
102             )
"""

dependencies: numpy, matplotlib, 
