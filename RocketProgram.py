from Reference import*
from sys import*
from RocketParameters import*
from RocketStaging import* 
from HohmannTransfer import* 

# This is the program for all the rocket calculations 

# The program will calculate the ∆V from the top down 

totalDeltaV = 0


################################################################################
#Tansfer Orbit 
################################################################################

totalDeltaV += HohmannTransfer(Calculate500)[0] # This calculates the optimal ∆V for to put the payload into a geostationary orbit and plane change

################################################################################
#Second Stage/ Circular Orbit 
################################################################################


### Finding ∆V 

totalDeltaV += hohmann_transfer(delta ,h1, h2, rEarth, muEarth )[0] # This calculates the optimal ∆V for to put the payload into a geostationary orbit and plane change
velocityP = hohmann_transfer(-delta ,h2, h1, rEarth, muEarth )[1] # delta V for the return burn.
totalDeltaV += velocityP # - drag + grav 
totalDeltaV += sqrt(mu_earth/(h1+r_earth)) # ∆V to get into the parking orbit 

## get a rough estimate on what the split should be. 
#splitTemp = split_deltaV(g0,f_inert, totalDeltaV, Isp)
#firstReenterV = totalDeltaV*splitTemp 
#totalDeltaV +=firstReenterV 


# Now we have a total ∆V.  

#Size the rocket 

#Stage 2 
split = split_deltaV(g0,f_inert, totalDeltaV, Isp)
v2 = totalDeltaV*split
v1 = totalDeltaV*(1-split)

print(v1)
print(v2)

stageTwoMass = initialMass(m_pay, f_inert[1], totalDeltaV*(split), Isp[1])
print(stageTwoMass)
stageOneMass = initialMass(stageTwoMass, f_inert[0], totalDeltaV*(1-split), Isp[0])
print(stageOneMass)



################################################################################
#1st Stage 
################################################################################

# add landing ∆V after split 
