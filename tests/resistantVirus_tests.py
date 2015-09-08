from nose.tools import *
from ps3b import *

def setup(): 
    global virus

    global global_maxBirthProb
    global global_clearProb
    global global_resistances
    global global_mutProb

    global_maxBirthProb = 1
    global_clearProb = 0
    global_resistances = {}
    global_mutProb = 0


    virus = ResistantVirus(
            global_maxBirthProb,
            global_clearProb,
            global_resistances,
            global_mutProb
            )


def teardown():
    print "TEAR DOWN!"

def test_return_values_properly():
    assert_equal(virus.maxBirthProb, global_maxBirthProb)
    assert_equal(virus.clearProb, global_clearProb)
    assert_equal(virus.resistances, global_resistances)
    assert_equal(virus.mutProb, global_mutProb)

def test_reproduce_properly():
    activeDrugs = []
    popDensity = .001
    child_virus = virus.reproduce(popDensity, activeDrugs)
    assert_equal(not child_virus,None)

    assert_equal(child_virus.maxBirthProb, global_maxBirthProb)
    assert_equal(child_virus.clearProb, global_clearProb)
    assert_equal(child_virus.resistances, global_resistances)
    assert_equal(child_virus.mutProb, global_mutProb)


setup()
test_return_values_properly()
test_reproduce_properly()
teardown()
