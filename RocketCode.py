#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:08:24 2017

@author: christopher
"""

import sys
from scipy import *
import matplotlib.pyplot as plt


Calculate500 = True

def dragLossUpToAltitude(altitude):
    """gives the drag loss up to the given altitude"""
    if 0 <= altitude and altitude <= 20000:
        return 150 - 0.0075*altitude # m/s
    else:
        raise Exception("Invalid at given altitude: {0}".format(altitude))

def gravityLossUpToAltitude(altitude):
    """gives the gravity loss up to a given altitude"""
    if 0 <= altitude and altitude <= 20000:
        return 1500 - 0.075*altitude # m/s
    else:
        raise Exception("Invalid at given altitude: {0}".format(altitude))

def steeringLoss():
    """gives the steering loss for a flight"""
    return 200 # m/s


def launchinfo(orbitalInclination):

    if orbitalInclination <=150:
        loc = "KSC"
        if orbitalInclination >=33 and orbitalInclination <= 150:
            delta = 0
        else :
            delta = abs(90-(57+orbitalInclination))
        
    else:
        loc = "VAFB"
        delta = 0 
        
        
    orbRad = (orbitalInclination*pi)/180
    
    if orbitalInclination <= 30:
        azimuth = 35
    elif loc == "KSC":
        azimuth = arcsin(cos(orbRad)/cos(0.4974188))
        azimuth = abs((azimuth*180)/pi)
        
    else:
        azimuth = arcsin(cos(orbRad)/cos(0.6056293))
        azimuth = abs((azimuth*180)/pi)
        
   
    delta = (delta*3.14)/180

    
    return delta, loc, azimuth

    

    
def mission(Calculate500,fairing):
    if(Calculate500 == True):
        m_pay = fairing + 15000
    else:
        m_pay = fairing + 5000
        
    return(m_pay)
        
# UNIVERSAL CONSTANTS

G = 6.67408e-11 # m^3/(kg*s^2) # universal gravitation constant
 
# EARTH CONSTANTS

g0 = 9.80665 # m/s^2 # gravitational acceleration at sea level
mEarth = 5.9723e24 # kg # mass of earth
rEarth = 6378137 # m # radius of earth
muEarth = G * mEarth # m^3/s^2

# ATMOSPERE PARAMETERS

airIdealGasConstant = 287.058 # J/(kg*K) # ideal gas constant of air
airHeatCapacityRatio = 1.4 # unitless # ratio of specific heats

# LAUNCH LOSSES

dVdragLoss = dragLossUpToAltitude(0) # m/s
dVgravityLoss = gravityLossUpToAltitude(0) # m/s
dVSteeringLoss = steeringLoss() # m/s

# TRANSFERS

dVfor500 = 195.40362680297374 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoTransfer = 2467.596447585046 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoStatOrbit = 4478.0452652 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s

# ROCKET INFORMAT





# [(name of rocket, Isp, mass, fuel capacity)]


f_inert = [0.1, 0.1] # inert mass fraction CENTUR .105
#
Isp = [336, 470] # s
fairing = 3000
m_pay = mission(Calculate500,fairing) #payload + fairing #kg
thrust = 1860000 # N 
engineCount = 6 
maxMass = 2500000
burnTime = 350 # seconds


# ORBIT INFORMATION

h1 = 200000 #m

orbitalInclination = 0# 0 in north 180 is south 

loc = launchinfo(orbitalInclination)[1]

delta = launchinfo(orbitalInclination)[0]


def mass_inert(m_pay, dV, Isp, f_inert): # Calculates Intital mass
    eV = exp(dV/(g0*Isp))
    
    m_inert = (m_pay*f_inert*(eV-1))/(1-f_inert*eV)
   
    return(m_inert)
    
    
def mass_prop(m_pay, dV, g0, Isp,f_inert): # calculates the weight of the propellent 
    eV = exp(dV/(g0*Isp))
    
    mProp = (m_pay*(eV-1)*(1-f_inert))/(1-f_inert*eV)

    return(mProp)
    
def initial_mass(m_pay,f_inert, dV, g0, Isp): # Calculates the intial mass of the stage
    
    eV = exp(dV/(g0*Isp))
    
    initialMass = ((m_pay*eV)*(1-f_inert))/(1-f_inert*eV)
  
    return(initialMass)
    
def deltaV(f_inert,g0,Isp): # Calculated DeltaV 
    deltaV = -(log(f_inert))*g0*Isp
    
    return(deltaV)

    
def rocket_mass(g0, f_inert, dV, Isp, m_pay):  #Calculates the total rocket mass

    stage2 = initial_mass(m_pay, f_inert[1], dV[1], g0, Isp[1])
 
    rocketMass = initial_mass(stage2, f_inert[0], dV[0], g0, Isp[0])


    return(rocketMass)
    
def thrustWeight(initialmass,thrust, engineCount):
    ttw = ((thrust/g0)*engineCount)
    ttw = ttw/ initialmass
    return(ttw)
    
def phase1(alt):

    velocity = sqrt(muEarth/(alt+rEarth))
    
    velocity += (dVdragLoss +dVgravityLoss+ dVSteeringLoss)
    return(velocity)
    
def split_deltaV(g0, f_inert, dV_needed, Isp,maxMass,m_pay): # calculates the split deltaV 
  
    massList = [] # Will hold the list of masses 
    splitList = []
    x = 0.2
    while x <= 0.8:
        
        v0 = dV_needed * x
        v1 = dV_needed * (1 - x)
        altDV = [v0, v1]
        mass = rocket_mass(g0, f_inert, altDV, Isp, m_pay)
      
        massList.append(mass)
        splitList.append(x)
        x += 0.1
        
    m = 0 
    minMass = maxMass
    
    for m in massList:
       if m > 0:
           if m <= minMass:
               minMass = m 
               
    if minMass == maxMass:
        split = 0
    else:
         minIndex = massList.index(minMass)
         split = splitList[minIndex]
   
    return(split)
    

def maxDeltaV(g0, f_inert, Isp,maxMass,m_pay):
    dvTest = 0 
    splitList = [] 
    dvTestList = []

    while dvTest <= 20000:
        split = split_deltaV(g0, f_inert, dvTest, Isp,maxMass,m_pay)
        splitList.append(split)
        dvTestList.append(dvTest)
        dvTest += 1000
        
        
    maxSplit = max(splitList)
    
    maxIndex = splitList.index(maxSplit)
    max_DeltaV = dvTestList[maxIndex]
    
    return(max_DeltaV)
        

def HohmannTransfer(Calculate500):
     
    if Calculate500 == True:
        h2 = 500000 #m        
        rat =(h2 +rEarth) # = 2at 
        rpt = h1 + rEarth         
        twoAT = rpt + rat        
        vC1 = sqrt(muEarth/(rpt)) # deltaV needed for circular orbit        
        energy = -muEarth/(twoAT)    
        vMan1 = sqrt((energy + (muEarth/rpt))* 2 )   
        deltaV1 = vMan1 - vC1
        # manuever 2    
        vC2 = sqrt(muEarth/rat) 
        deltaRad = delta #* pi/180
        vMan2 = sqrt((energy + (muEarth/rat))* 2 )
        deltaV2 =  vC2 - vMan2 
        planeChangeV = 2*vC2*sin(deltaRad/2)
        #print(planeChangeV)
        #print(planeChangeV)
        #planeChangeV = ((vMan2*cos(deltaRad) - vC2)**2 + (vMan2 - sin(delta))**2)**.5
        dVH = deltaV1 + deltaV2 +planeChangeV
       
    else:
        h2 = 35622000       
        rat =(h2 +rEarth) # = 2at 
        rpt = h1 + rEarth         
        twoAT = rpt + rat        
        vC1 = sqrt(muEarth/(rpt)) # deltaV needed for circular orbit 
        energy = -muEarth/(twoAT)       
        vMan1 = sqrt((energy + (muEarth/rpt))* 2 )
      
        deltaV1 = vMan1 - vC1
            
        
        dVH = deltaV1 
        
    return dVH

    
    
def calcDeltaV():
    deltaV = phase1(h1)
    deltaV += HohmannTransfer(Calculate500)
    if Calculate500 == True:
        deltaV +=0.225
    else:
        deltaV += 2.49
    return deltaV
    
    
    
    
def propCost(m_pay, dV, g0, Isp,f_inert):
    stageTwo = mass_inert(m_pay, dV[1], Isp[1], f_inert[1])
    
    costTwo = mass_prop(m_pay, dV[1], g0, Isp[1],f_inert[1]) * 20
    costOne = mass_prop(stageTwo, dV[0], g0, Isp[0],f_inert[0]) * 20
    return costOne+costTwo
    
def stageCost(m_pay, dV, Isp, f_inert):
    stageTwo = mass_inert(m_pay, dV[1], Isp[1], f_inert[1])
    stageOne = mass_inert(stageTwo, dV[0], Isp[0], f_inert[0])

    stageTwoCost = stageTwo*2000
    stageOneCost = stageOne*2000
    
    return stageOneCost + stageTwoCost
    
    
def findFInert(givenProp, givenDry):
    return (givenDry/(givenProp+givenDry))

def firstStageRange(burnTime, dVOne):
    return((dVOne/2)*burnTime)
    
    
def missionProfile():
    #Calculate500 = True
    loc = launchinfo(orbitalInclination)[1]
    azimuth = launchinfo(orbitalInclination)[2]
    deltaVNeeded =  calcDeltaV()
    split = split_deltaV(g0, f_inert, deltaVNeeded, Isp,maxMass,m_pay)
    dV = [(split*deltaVNeeded), (1-split)*deltaVNeeded]
    returnProp = mass_prop(m_pay, 300, g0, Isp[0],f_inert[0])
    rocketMass = rocket_mass(g0, f_inert, dV, Isp, m_pay) + returnProp
    deltaV = maxDeltaV(g0, f_inert, Isp,maxMass,m_pay)
    thrustToWeight = thrustWeight(rocketMass,thrust, engineCount)   
    rocketCost = stageCost(m_pay, dV, Isp, f_inert)
    propellantCost = propCost(m_pay, dV, g0, Isp,f_inert)
    totalCost = rocketCost +propellantCost 
    excessDeltaV = sum(dV)-deltaVNeeded
    secondStageReturn = mass_inert(m_pay, dV[1], Isp[1], f_inert[1])
    downRange = firstStageRange(burnTime,dV[0])
    print("Payload Mass:", m_pay,"kg")    
    if Calculate500 == True:
        print("Posigrade Orbit to 500km at", orbitalInclination,"degrees")
    else:
        print("Geostationary Orbit")
    print("Launch Location:",loc)
    print("Azimuth:",azimuth,"Degrees")
    print("∆V Needed:",calcDeltaV(),"m/s")
    print("∆V Available:", deltaV, "m/s")
    print("Excess ∆V:",excessDeltaV)
    print("Optimal ∆V Split: First Stage:", dV[0],"m/s",dV[1],"m/s")
    print("Second Stage Mass:", initial_mass(m_pay,f_inert[1], dV[1], g0, Isp[1]))
    print("Second Stage Return Mass:",secondStageReturn,"kg")
    print("First Stage Landing Distance:", downRange,"m")
    print("Rocket Mass:",rocketMass,"kg")
    print("Return Propellent Mass:", returnProp,"kg")
    print("Thrust to Weight Ratio:",thrustToWeight)
    print("Rocket Cost: $", rocketCost)
    print("Propellent Cost: $", propellantCost)
    print("Total Cost: $",totalCost)
    

    return totalCost,deltaVNeeded,  excessDeltaV,  secondStageReturn, rocketMass
    
missionProfile()


azimuthList = [] 
orbitalInclinationList = [] 
totalCostList = []
deltaVNeededList = []
excessDeltaVList = [] 
secondStageReturnList = [] 
rocketMassList = [] 
engine_count = []

oI = 0 

while oI <= 180:
    
    loc  = launchinfo(oI)[1]
    delta = launchinfo(oI)[0]
    azimuthList.append(launchinfo(oI)[2])
    totalCostList.append(missionProfile()[0])
    deltaVNeededList.append(missionProfile()[1])
    excessDeltaVList.append(missionProfile()[2])
    secondStageReturnList.append(missionProfile()[3])
    rocketMassList.append(missionProfile()[4])
    orbitalInclinationList.append(oI)
    
    eC = 0
    while thrustWeight(missionProfile()[4],thrust, eC) <=1.2:
            eC += 1 
    engine_count.append(eC)
    orbitalInclination += 1
    

print(totalCostList)
print(rocketMassList)
print(engine_count)



plt.figure(1)
plt.plot(orbitalInclinationList,totalCostList)
plt.title("Total Cost v Orbital Inclination")
plt.xlabel("Orbital Inclination (degrees)")
plt.ylabel("Cost in Tens of Millions ($)")
plt.figure(2)
plt.plot(orbitalInclinationList,deltaVNeededList)
plt.title("∆V Needed v Orbital Inclination")
plt.xlabel("Orbital Inclination (degrees)")
plt.ylabel("∆V Needed (m/s)")
plt.figure(3)
plt.plot(orbitalInclinationList,excessDeltaVList)
plt.title("Excess ∆V v Orbital Inclination" )
plt.xlabel("Orbital Inclination (degrees)")
plt.ylabel("Excess ∆V (m/s)")
plt.figure(4)
plt.plot(orbitalInclinationList,secondStageReturnList)
plt.title("Second Stage Return Mass v Orbital Inclination")
plt.xlabel("Orbital Inclination (degrees)")
plt.ylabel("Mass (kg)")
plt.figure(5)
plt.plot(orbitalInclinationList,rocketMassList)
plt.title("Rocket Mass v Orbital Inclination")
plt.xlabel("Orbital Inclination (degrees)")
plt.ylabel("Rocket Mass (kg)")
plt.figure(6)
plt.plot(orbitalInclinationList,azimuthList)
plt.title("Azimuth v Orbital Inclination")
plt.xlabel("Orbital Inclination (degrees)")
plt.ylabel("Azimuth (degrees)")

    