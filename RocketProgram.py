#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:32:55 2017

@author: christopher
"""

from Reference import*
from sys import*
from RocketParameters import*
from RocketStaging import* 
from HohmannTransfer import* 

# This is the program for all the rocket calculations 

# The program will calculate the ∆V from the top down 

totalDeltaV = 0

####################################################
#Tansfer Orbit 
####################################################


totalDeltaV += hohmann_transfer(delta ,h1, h2, rEarth, muEarth )[0] # This calculates the optimal ∆V for to put the payload into a geostationary orbit and plane change
print(hohmann_transfer(delta ,h1, h2, rEarth, muEarth ))

totalDeltaV += hohmann_transfer(delta ,h1, h2, r_earth, mu_earth )[0] # This calculates the optimal ∆V for to put the payload into a geostationary orbit and plane change

returnDeltaV = 100000 # return ∆V 

print(hohmann_transfer(delta ,h1, h2, r_earth, mu_earth ))


####################################################
#Second Stage/ Circular Orbit 
####################################################






####################################################
#1st Stage 
####################################################

# add landing ∆V after split 



