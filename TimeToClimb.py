###############################################################################
#TIME TO CLIMB
###############################################################################

import scipy as sp
from Atmosphere import*
from Reference import*

def TimeToClimb():

    ###########################################################################
    #INITIAL VALUES
    ###########################################################################
    
    h1 = 0 #initial altitude (m)
    theta = theta * pi / 180 #angle of attack (rad)
    rho0 = densityAtAltitude(0) #air density at sea level (kg/m^3)
    
    ###########################################################################
    #CALCULATIONS
    ###########################################################################
    
    V0 = (2*W/(rho0*S*Cl))**.5 #Velocity at sea-level (m/s)
    PR0 = ((2*(W**3)*(Cd**2))/(rho0*S*(Cl**3)))**.5
    PA0 = ThrustMax * V0    

    RCarray = [] 
    altitudes = [] 

    for h in range(h1,hf+1):
        rhoAlt = densityAtAltitude(h) #density of air at altitude 'h' (kg/m^3)
        V = V0 * ((rho0/rhoAlt)**.5) #Velocity of aircraft (m/s)
        PA = PA0 * (rhoAlt/rho0) #power available (N)
        PR = PR0 * ((rho0/rhoAlt)**.5) #power required (N)
        RC = (PA - PR) / W #Rate of Climb (m/min)
        RCarray.append(1/RC)
        altitudes.append(h)
    tClimb = sp.trapz(RCarray, altitudes) #Time to altitude (min)
    
    return tClimb
