#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:06:15 2017

@author: christopher
"""

from scipy import *
import sys

# 
#g = 9.8
#f_inert = .11
#isp = 350
#dV = 1500
#m_pay = 1000

def mass_inert(m_pay, dV, isp, f_inert): # Calculates Intital mass
    eV = exp(dV/(g0*isp))
    
    m_inert = (m_pay*f_inert*(eV-1))/(1-f_inert*eV)
    #print(m_inert)
    return(m_inert)
    
    
def mass_prop(m_pay, dV, g0, isp): # calculates the weight of the propellent 
    eV = exp(dV/(g0*isp))
    
    mProp = (m_pay*(eV-1)*(1-f_inert))/(1-f_inert*eV)
    
    #print(mProp)
    return(mProp)
    
def initial_mass(m_pay,f_inert, dV, g0, isp): # Calculates the intial mass of the stage
    
    eV = exp(dV/(g0*isp))
    
    initialMass = ((m_pay*eV)*(1-f_inert))/(1-f_inert*eV)
    #print(initialMass)
    return(initialMass)
    
def deltaV(f_inert,g0,isp): # Calculated DeltaV 
    deltaV = -(log(f_inert))*g0*isp
    #print(deltaV)
    return(deltaV)
    


    
#mass_inert(m_pay, dV, isp, f_inert)
#mass_prop(m_pay, dV, g, isp)
#initial_mass(m_pay,f_inert, dV, g, isp)   
#deltaV(f_inert,g,isp)
#

