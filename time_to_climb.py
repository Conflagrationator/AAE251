"""
This function calculates the time to climb by using the rate to climb given the 
weight, drag, and thrust available of the airplane.
"""
import scipy as sp
from Atmosphere import*
#BPR, length, fandia, weight1, thrust_available
def time_to_climb():
    """
    BPR is unitless
    length should be given in units of m
    fandia, or diameter of the fan, should be given in units of m
    weight1, or weight of the engine, should be given in units of kg
    thrust_available should be given in units of N
    """
    #values given by airplane
    V0 = 51.4444 #velocity of airplane in m/s (converted from 100 knots) at sea level
    hf = 100000 #final altitude in m, calcualted with a conversion from feet
    h1 = 0 #initial altitude
    theta = 16.5 * pi / 180 #optimal angle of attack in radians

    #test values
    weight = 150000 * 0.453592 #weight of airplane in pounds (this value is an average for now)
    Cd = 0.04423 #coefficient of drag
    Cl = 1.582 #coefficient of lift
    rho0 = densityAtAltitude(0) #air density at sea level in SI units
    S = 2 #reference area of wing in m^2
    
    #calculations
    R_Carray = [] #initialization for R/C values for use of loop
    altitudes = [] #initialization of altitudes used
    for h in range(h1,hf+1):
        rho_alt = densityAtAltitude(h) #density of air at altitude 'h'
        V = V0*(rho0/rho_alt)**.5 #freestream velocity at altitude 'h' in m/s
        drag = Cd * 0.5 * rho_alt * V**2 * S #calculation using drag equation in N
        ADuct = pi * (fandia/2)**2 #area of the inlet of the fan duct in m^2
        mDotDuct = rho_alt * V * ADuct #mass flow rate of the fan duct in kg/s
        mDotAir = mDotDuct / (1.05 * BPR) #mass flow rate of the core in kg/s
        mDotFuel = .05 * mDotAir #mass flow rate of fuel in kg/s
#        thrust_available = (mDotAir + mDotFuel)*Ve - mDotAir*V+ (pe - pressureAtAltitude(h))*Ae
        #how to calculate V, p, and A at exit?
        PA = thrust_available * V #power available
        PR = drag * V #power required
        RC = (PA - PR) / weight #Rate of Climb
        print(RC)
        R_Carray.append(1/RC)
        altitudes.append(h)
    t_climb = sp.trapz(R_Carray, altitudes)

    return t_climb