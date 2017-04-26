from scipy import *
from RocketParameters import * 
from Reference import *
import sys

################################################################################
# ROCKET STAGING
################################################################################

def rocket_mass(g0, f_inert, dV, isp, m_pay):  #Calculates the total rocket mass
    
    stage2 = initial_mass(m_pay, f_inert[1], dV[1], g0, isp[1])
 
    rocketMass = initial_mass(stage2, f_inert[0], dV[0], g0, isp[0])

    return(rocketMass)

def split_deltaV(g0, f_inert, dV_needed, isp): # calculates the split deltaV 
  
    massList = [] # Will hold the list of masses 
    splitList = []
    x = 0.2
    while x <= 0.8:
        
        v0 = dV_needed * x
        v1 = dV_needed * (1 - x)
        altDV = [v0, v1]
        mass = rocket_mass(g0, f_inert, altDV, isp, m_pay)
        massList.append(mass)
        splitList.append(x)
        x += 0.01
        
    minMass = min(massList)
    minIndex = massList.index(minMass)
    split = splitList[minIndex]
    return(split)
