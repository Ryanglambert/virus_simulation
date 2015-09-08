# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import pdb
import numpy
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from ps3b_precompiled_27 import *

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
#class SimpleVirus(object):

    #"""
    #Representation of a simple virus (does not model drug effects/resistance).
    #"""
    #def __init__(self, maxBirthProb, clearProb):
        #"""
        #Initialize a SimpleVirus instance, saves all parameters as attributes
        #of the instance.        
        #maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        #clearProb: Maximum clearance probability (a float between 0-1).
        #"""
        #self.maxBirthProb = float(maxBirthProb)
        #self.clearProb = float(clearProb)

        ## TODO

    #def getMaxBirthProb(self):
        #"""
        #Returns the max birth probability.
        #"""
        ## TODO
        #return self.maxBirthProb  

    #def getClearProb(self):
        #"""
        #Returns the clear probability.
        #"""
        ## TODO
        #return self.clearProb  

    #def doesClear(self):
        #""" 
        #Stochastically determines whether this virus particle is cleared from the
        #patient's body at a time step. 
        #returns: True with probability self.getClearProb and otherwise returns
        #False.
        #"""
        #if self.getClearProb() >= random.random():
            #return True
        #else:
            #return False

        ## TODO

    
    #def reproduce(self, popDensity):
        #"""
        #Stochastically determines whether this virus particle reproduces at a
        #time step. Called by the update() method in the Patient and
        #TreatedPatient classes. The virus particle reproduces with probability
        #self.maxBirthProb * (1 - popDensity).
        
        #If this virus particle reproduces, then reproduce() creates and returns
        #the instance of the offspring SimpleVirus (which has the same
        #maxBirthProb and clearProb values as its parent).         

        #popDensity: the population density (a float), defined as the current
        #virus population divided by the maximum population.         
        
        #returns: a new instance of the SimpleVirus class representing the
        #offspring of this virus particle. The child should have the same
        #maxBirthProb and clearProb values as this virus. Raises a
        #NoChildException if this virus particle does not reproduce.               
        #"""
        #try:
            #if random.random() <= (self.maxBirthProb * (1-popDensity)):
                #return SimpleVirus(self.maxBirthProb,self.clearProb)
                
        #except NoChildException:
            #pass






#class Patient(object):
    #"""
    #Representation of a simplified patient. The patient does not take any drugs
    #and his/her virus populations have no drug resistance.
    #"""    

    #def __init__(self, viruses, maxPop):
        #"""
        #Initialization function, saves the viruses and maxPop parameters as
        #attributes.

        #viruses: the list representing the virus population (a list of
        #SimpleVirus instances)

        #maxPop: the maximum virus population for this patient (an integer)
        #"""
        #self.viruses = viruses
        #self.maxPop = maxPop

        ## TODO

    #def getViruses(self):
        #"""
        #Returns the viruses in this Patient.
        #"""
        ## TODO
        #return self.viruses


    #def getMaxPop(self):
        #"""
        #Returns the max population.
        #"""
        ## TODO
        #return self.maxPop


    #def getTotalPop(self):
        #"""
        #Gets the size of the current total virus population. 
        #returns: The total virus population (an integer)
        #"""

        ## TODO        
        #return len(self.viruses)



    #def update(self):
        #"""
        #Update the state of the virus population in this patient for a single
        #time step. update() should execute the following steps in this order:
        
        #- Determine whether each virus particle survives and updates the list
        #of virus particles accordingly.   
        
        #- The current population density is calculated. This population density
          #value is used until the next call to update() 
        
        #- Based on this value of population density, determine whether each 
          #virus particle should reproduce and add offspring virus particles to 
          #the list of viruses in this patient.                    

        #returns: The total virus population at the end of the update (an
        #integer)
        #"""

        ## TODO
        ##Clear viruses that clear
        #for virus in self.getViruses():
            #if virus.doesClear():
                #self.viruses.remove(virus)

        #popDensity = float(self.getTotalPop()) / float(self.getMaxPop())
        
        #for virus in self.getViruses():
            ##virus.reproduce(popDensity)
            ##pdb.set_trace()
            #virus_spawn = virus.reproduce(popDensity)
            #if virus_spawn != None:
                #self.viruses.append(virus_spawn)

        #return self.getTotalPop()

        



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials, timeSteps):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    virusesAtTimeStep = [list() for i in range(timeSteps)]


    for j in range(numTrials):
        patient = Patient([SimpleVirus(maxBirthProb,clearProb) for virus in range(numViruses)], maxPop)
        for i in range(timeSteps):
            virusesAtTimeStep[i].append(patient.getTotalPop())
            patient.update()

    average_at_time_step = []

    for i in range(len(virusesAtTimeStep)):
        average_at_time_step.append(numpy.average(virusesAtTimeStep[i]))

    return average_at_time_step




##
## PROBLEM 4
##
#class ResistantVirus(SimpleVirus):
    #"""
    #Representation of a virus which can have drug resistance.
    #"""   

    #def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        #"""
        #Initialize a ResistantVirus instance, saves all parameters as attributes
        #of the instance.

        #maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        #clearProb: Maximum clearance probability (a float between 0-1).

        #resistances: A dictionary of drug names (strings) mapping to the state
        #of this virus particle's resistance (either True or False) to each drug.
        #e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        #particle is resistant to neither guttagonol nor srinol.

        #mutProb: Mutation probability for this virus particle (a float). This is
        #the probability of the offspring acquiring or losing resistance to a drug.
        #"""

        ## TODO
        #self.maxBirthProb = maxBirthProb
        #self.clearProb = clearProb
        #self.resistances = resistances
        #self.mutProb = mutProb


    #def getResistances(self):
        #"""
        #Returns the resistances for this virus.
        #"""
        ## TODO
        #return self.resistances.copy()

    #def getMutProb(self):
        #"""
        #Returns the mutation probability for this virus.
        #"""
        ## TODO
        #return self.mutProb

    #def isResistantTo(self, drug):
        #"""
        #Get the state of this virus particle's resistance to a drug. This method
        #is called by getResistPop() in TreatedPatient to determine how many virus
        #particles have resistance to a drug.       

        #drug: The drug (a string)

        #returns: True if this virus instance is resistant to the drug, False
        #otherwise.
        #"""
        
        ## TODO
        #return self.getResistances()[drug]


    #def reproduce(self, popDensity, activeDrugs):
        #"""
        #stochastically determines whether this virus particle reproduces at a
        #time step. Called by the update() method in the TreatedPatient class.

        #A virus particle will only reproduce if it is resistant to ALL the drugs
        #in the activeDrugs list. For example, if there are 2 drugs in the
        #activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        #then it will NOT reproduce.

        #Hence, if the virus is resistant to all drugs
        #in activeDrugs, then the virus reproduces with probability:      

        #self.maxBirthProb * (1 - popDensity).                       

        #If this virus particle reproduces, then reproduce() creates and returns
        #the instance of the offspring ResistantVirus (which has the same
        #maxBirthProb and clearProb values as its parent). The offspring virus
        #will have the same maxBirthProb, clearProb, and mutProb as the parent.

        #For each drug resistance trait of the virus (i.e. each key of
        #self.resistances), the offspring has probability 1-mutProb of
        #inheriting that resistance trait from the parent, and probability
        #mutProb of switching that resistance trait in the offspring.       

        #For example, if a virus particle is resistant to guttagonol but not
        #srinol, and self.mutProb is 0.1, then there is a 10% chance that
        #that the offspring will lose resistance to guttagonol and a 90%
        #chance that the offspring will be resistant to guttagonol.
        #There is also a 10% chance that the offspring will gain resistance to
        #srinol and a 90% chance that the offspring will not be resistant to
        #srinol.

        #popDensity: the population density (a float), defined as the current
        #virus population divided by the maximum population       

        #activeDrugs: a list of the drug names acting on this virus particle
        #(a list of strings).

        #returns: a new instance of the ResistantVirus class representing the
        #offspring of this virus particle. The child should have the same
        #maxBirthProb and clearProb values as this virus. Raises a
        #NoChildException if this virus particle does not reproduce.
        #"""

        #try:
            #if random.random() <= (self.maxBirthProb * (1-popDensity)):
                #return SimpleVirus(self.maxBirthProb,self.clearProb)
                
        #except NoChildException:
            #pass


            

#class TreatedPatient(Patient):
    #"""
    #Representation of a patient. The patient is able to take drugs and his/her
    #virus population can acquire resistance to the drugs he/she takes.
    #"""

    #def __init__(self, viruses, maxPop):
        #"""
        #Initialization function, saves the viruses and maxPop parameters as
        #attributes. Also initializes the list of drugs being administered
        #(which should initially include no drugs).              

        #viruses: The list representing the virus population (a list of
        #virus instances)

        #maxPop: The  maximum virus population for this patient (an integer)
        #"""

        #self.viruses = viruses
        #self.maxPop = maxPop
        #self.drugList = []


    #def addPrescription(self, newDrug):
        #"""
        #Administer a drug to this patient. After a prescription is added, the
        #drug acts on the virus population for all subsequent time steps. If the
        #newDrug is already prescribed to this patient, the method has no effect.

        #newDrug: The name of the drug to administer to the patient (a string).

        #postcondition: The list of drugs being administered to a patient is updated
        #"""
        #assert type(newDrug) == str
        #if newDrug not in self.drugList:
            #self.drugList.append(newDrug)


    #def getPrescriptions(self):
        #"""
        #Returns the drugs that are being administered to this patient.

        #returns: The list of drug names (strings) being administered to this
        #patient.
        #"""
        #return self.drugList

    #def getResistPop(self, drugResist):
        #"""
        #Get the population of virus particles resistant to the drugs listed in
        #drugResist.       

        #drugResist: Which drug resistances to include in the population (a list
        #of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        #returns: The population of viruses (an integer) with resistances to all
        #drugs in the drugResist list.
        #"""
        #virusesResistant = 0
        #for virus in self.viruses:
            #for drug in drugResist:
                #if drug not in self.getResistances.keys():
                    #break
                #else:
                    #virusesResistant += 1
        #return virusesResistant
                    


    #def update(self):
        #"""
        #Update the state of the virus population in this patient for a single
        #time step. update() should execute these actions in order:

        #- Determine whether each virus particle survives and update the list of
          #virus particles accordingly

        #- The current population density is calculated. This population density
          #value is used until the next call to update().

        #- Based on this value of population density, determine whether each 
          #virus particle should reproduce and add offspring virus particles to 
          #the list of viruses in this patient.
          #The list of drugs being administered should be accounted for in the
          #determination of whether each virus particle reproduces.

        #returns: The total virus population at the end of the update (an
        #integer)
        #"""

        ## TODO
        #for virus in self.getViruses():
            #if virus.doesClear():
                #self.viruses.remove(virus)

        #popDensity = float(self.getTotalPop()) / float(self.getMaxPop())
    
        ##Reproduce viruses
        #for virus in self.getViruses():
            ##virus.reproduce(popDensity)
            ##pdb.set_trace()
            #virus_spawn = virus.reproduce(popDensity, self.getPrescriptions())
            #if virus_spawn != None:
                #self.viruses.append(virus_spawn)

        #return self.getTotalPop()



#
# PROBLEM 5
#
def simulationWithDrug(numViruses, 
                        maxPop, 
                        maxBirthProb, 
                        clearProb, 
                        resistances,
                        mutProb, 
                        numTrials, 
                        timeSteps, 
                        timeAddPrescription, 
                        timeAddPrescription2, 
                        firstPrescription, 
                        secondPrescription,
                        stdev=False
                        ):
                        #virusAverage=True,
                        #resistantAverage=False,
                        #virusHighStdev=False,
                        #virusLowStdev=False,
                        #resistantHighStdev=False,
                        #resistantLowStdev=False
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    virusesAtTimeStep = [list() for i in range(timeSteps)]
    resistantPopulationAtTimeStep = [list() for i in range(timeSteps)]
    local_resistances = resistances.copy()

    for j in xrange(numTrials):
        patient = TreatedPatient(
                [ResistantVirus(maxBirthProb,clearProb,local_resistances, mutProb) for virus in range(numViruses)], 
                maxPop
                )

        for i in range(timeAddPrescription):
            resistantPopulationAtTimeStep[i].append(patient.getResistPop(patient.getPrescriptions()))
            virusesAtTimeStep[i].append(patient.getTotalPop())
            patient.update()

        patient.addPrescription(firstPrescription)

        for i in range(timeAddPrescription, timeAddPrescription2):
            resistantPopulationAtTimeStep[i].append(patient.getResistPop(patient.getPrescriptions()))
            virusesAtTimeStep[i].append(patient.getTotalPop())
            patient.update()

        patient.addPrescription(secondPrescription)

        for i in range(timeAddPrescription2, timeSteps):
            resistantPopulationAtTimeStep[i].append(patient.getResistPop(patient.getPrescriptions()))
            virusesAtTimeStep[i].append(patient.getTotalPop())
            patient.update()

        patient = None
    average_at_time_step = []
    average_resistant_population = []
    high_stdev_at_time_step = []
    low_stdev_at_time_step = []
    high_stdev_resistant_at_time_step = []
    low_stdev_resistant_at_time_step = []

    for i in range(len(virusesAtTimeStep)): 
        average_at_time_step.append(numpy.average(virusesAtTimeStep[i]))
        average_resistant_population.append(numpy.average(resistantPopulationAtTimeStep[i]))
    for i in range(len(virusesAtTimeStep)):
        high_stdev_at_time_step.append(average_at_time_step[i] + numpy.std(virusesAtTimeStep[i]))
        low_stdev_at_time_step.append(average_at_time_step[i] - numpy.std(virusesAtTimeStep[i]))
        high_stdev_resistant_at_time_step.append(average_resistant_population[i] + numpy.std(resistantPopulationAtTimeStep[i]))
        low_stdev_resistant_at_time_step.append(average_resistant_population[i] - numpy.std(resistantPopulationAtTimeStep[i]))

    if stdev == True:
        return average_at_time_step,average_resistant_population,high_stdev_at_time_step, low_stdev_at_time_step, high_stdev_resistant_at_time_step,low_stdev_resistant_at_time_step
    else:
        return average_at_time_step



    #plt.figure(1)
    #plt.plot(numpy.arange(0,timeSteps) ,average_at_time_step,'ro')
    #plt.plot(numpy.arange(0,timeSteps) ,average_resistant_population,'-')
    #plt.plot(numpy.arange(0,timeSteps) ,[530 for i in range(timeSteps)],'x')
    #plt.axis([0, timeSteps, 0, 1000])
    #plt.show()
#Plot problem 3,4,5

def main():

    timeSteps = 450
    timeAddPrescription = 0
    timeAddPrescription2 = 150
    firstPrescription = "grimpex"
    secondPrescription = "guttaganol"
    maxPop = 1000
    numTrials = 100
    #t = numpy.arange(0,timeSteps)

    average_at_time_step, average_resist_at_time_step, high_stdev, low_stdev, high_resist_stdev,low_resist_stdev = simulationWithDrug(                                                                     
            numViruses=100, 
            maxPop=maxPop, 
            maxBirthProb=.1,
            clearProb=.05,
            resistances={"guttaganol":False, "grimpex":False},
            mutProb=.005,
            numTrials=numTrials,
            timeSteps=timeSteps,
            timeAddPrescription=timeAddPrescription,
            timeAddPrescription2=timeAddPrescription2,
            firstPrescription=firstPrescription,
            secondPrescription=secondPrescription,
            stdev=True
            )

    #average_at_time_step = simulationWithDrug(                                                                     
            #numViruses=100, 
            #maxPop=maxPop, 
            #maxBirthProb=.1,
            #clearProb=.05,
            #resistances={"guttaganol":False, "grimpex":False},
            #mutProb=.005,
            #numTrials=5,
            #timeSteps=timeSteps,
            #timeAddPrescription=timeAddPrescription,
            #timeAddPrescription2=timeAddPrescription2,
            #firstPrescription=firstPrescription,
            #secondPrescription=secondPrescription,
            #stdev=False
            #)


    #average_at_time_step_no_drugs = simulationWithoutDrug(
            #numViruses=100, 
            #maxPop=1000, 
            #maxBirthProb=.1,
            #clearProb=.05,
            #resistances={"guttaganol":False},
            #mutProb=.3,
            #numTrials=10,
            #timeSteps=350,
            #)
    
    # plotting
    plt.figure(1)
    x_scale = numpy.arange(timeSteps)
    plt.subplot(211)
    plt.plot(x_scale ,average_at_time_step,'ro', label="average") 
    plt.plot(x_scale ,high_stdev,',', label="+1 STDEV") 
    plt.plot(x_scale, low_stdev, ',', label="-1 STDEV")
    plt.vlines([timeAddPrescription, timeAddPrescription2],0 , 1000, label=u'Prescription Times', colors=u'k')

    plt.annotate(firstPrescription, xy=(timeAddPrescription , 800),  xycoords='data',
                xytext=(20,10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                )
    plt.annotate(secondPrescription, xy=(timeAddPrescription2 , 800),  xycoords='data',
                xytext=(20,-20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                )

    # formatting
    plt.axis([0, timeSteps, 0, 1000])
    plt.xticks(numpy.arange(0, timeSteps, 50))
    plt.yticks(numpy.arange(0, maxPop, 100))
    plt.xlabel('TimeSteps') 
    plt.ylabel('Virus Population')
    plt.title(r'Total Virus Population')
       
    plt.grid(True)

    # Plotting
    plt.subplot(212)
    plt.plot(x_scale ,average_resist_at_time_step,'ro', label="average") 
    plt.plot(x_scale ,high_resist_stdev,'_', label="+1 STDEV") 
    plt.plot(x_scale, low_resist_stdev, '_', label="-1 STDEV")
    plt.legend(bbox_to_anchor=(0., 1.02, 1, .5), loc=3,
                       ncol=3, mode="expand", borderaxespad=1.5)
    plt.vlines([timeAddPrescription, timeAddPrescription2],0 , 1000, label=u'Prescription Times', colors=u'k')
    plt.annotate(firstPrescription, xy=(timeAddPrescription , 800),  xycoords='data',
                xytext=(20,10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                )
    plt.annotate(secondPrescription, xy=(timeAddPrescription2 , 800),  xycoords='data',
                xytext=(20,-20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                )

    # formatting
    plt.axis([0, timeSteps, 0, 1000])
    plt.xticks(numpy.arange(0, timeSteps, 50))
    plt.yticks(numpy.arange(0, maxPop, 100))
    plt.xlabel('TimeSteps') 
    plt.ylabel('Resistant Virus Population')
    plt.title(r'Resistant Viruses Population')  
       
    plt.subplots_adjust(hspace=.7)
    plt.grid(True)


    plt.show()

if __name__ == "__main__":
    main()
