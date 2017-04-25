#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:51:00 2017

@author: christopher
"""

from scipy import *
from RocketParameters import * 
from Reference import *
import sys

#g0 = 9.8
##[Stage 1 , Stage 2]
#f_inert = [.08,.12]
#isp = [310, 360]
#dV = [5000,2000]
#m_pay = 10000
#dV_needed = 9000

def rocket_mass(g0,f_inert, dV, isp,m_pay):  #Calculates the total rocket mass
    
    stage2 = initial_mass(m_pay,f_inert[1], dV[1], g0, isp[1])
    #print("Stage 2 Mass;", stage2)
    
    rocketMass = initial_mass(stage2,f_inert[0], dV[0], g0, isp[0])
    #print("Total Rocket Mass:", rocketMass)
    
    return(rocketMass)
    
#rocket_mass(g,f_inert, dV, isp)


def split_deltaV(g0,f_inert, dV_needed, isp): # calculates the split deltaV 
  
    massList = [] # Will hold the list of masses 
    splitList = []
    x = .2
    while x <= .8:
        
        v0 = dV_needed*x
        v1 = dV_needed*(1-x)
        altDV =[ v0,v1]
        #print(altDV)
        mass = rocket_mass(g0,f_inert, altDV, isp, m_pay)
        massList.append(mass)
        splitList.append(x)
        x += .01
        
    minMass = min(massList)
    minIndex = massList.index(minMass)
    split = splitList[minIndex]
    #print(split)
    return(split)
        
#print(split_deltaV(g0,f_inert, dV_needed, isp))