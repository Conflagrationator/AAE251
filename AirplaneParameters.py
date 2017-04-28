from scipy import *
from Reference import *
from Atmosphere import *

################################################################################
# AIRPLANE PARAMETER FUNCTIONS
################################################################################
# tsfc = thrust specific fuel consumption
# CL = airplane lift coefficient
# CD = airplane drag coefficient
# c = chord length
# b = span
# S = wingReferenceArea
# AR = aspect ratio
# q = dynamicPressure

def wingReferenceArea(c, b):
    return c*b

def aspectRatio(c, b):
    return b/c

def stallSpeed(airplaneWeight, freestreamDensity, S, maxCL):
    return sqrt((2 * airplaneWeight) / (freestreamDensity * S * maxCL))

def dynamicPressure(freestreamDensity, freestreamVelocity):
    return 0.5 * freestreamDensity * freestreamVelocity**2

def totalLiftCoefficient(totalLift, q, S):
    return totalLift / (q * S)

def liftCoefficientAtAngleOfAttack(airfoilData, angle):
    AnglesAndCls = list(map(lambda row: (row["Alpha"], row["Cl"]), airfoilData))
    return interpolate(AnglesAndCls, angle)

def profileDragCoefficient(airfoilData, CL):
    ClsAndCds = list(map(lambda row: (row["Cl"], row["Cd"]), airfoilData))
    return interpolate(ClsAndCds, CL)

def inducedDragCoefficient(CL, AR, spanEfficiencyFactor):
    return CL**2 / (pi * AR * spanEfficiencyFactor)

def powerRequired(airplaneWeight, CL, CD, density):
    return sqrt((2 * airplaneWeight * CD**2) / (density * S * CL**2))

# CONVENIENCE FUNCTIONS

def totalDragCoefficient(CL, AR, spanEfficiencyFactor, airfoilData):
    return profileDragCoefficient(airfoilData, CL) + inducedDragCoefficient(CL, AR, spanEfficiencyFactor)

def powerGivenThrust(thrust, freestreamVelocity):
    return thrust * freestreamVelocity

def thrustGivenPower(power, freestreamVelocity):
    return power / freestreamVelocity

# PERFORMANCE

def airplaneRange(freestreamDensity, S, CL, CD, tsfc, fullWeight, emptyWeight):
    return 2 * sqrt(2 / (freestreamDensity * S)) * (sqrt(CL) / CD) * (1 / tsfc) * (sqrt(fullWeight) - sqrt(emptyWeight))

def airplaneEndurance(tsfc, CL, CD, fullWeight, emptyWeight):
    return (1 / tsfc) * (CL / CD) * log(fullWeight / emptyWeight)

def liftoffDistance(altitude, airplaneWeight, stallVelocity, thrust, coefficientOfRollingFriction, b, c, CL, wingHeightOffGround, spanEfficiencyFactor):
    liftoffVelocity = 1.2 * stallVelocity # approximate
    averageVelocity = 0.7 * liftoffVelocity
    freestreamDensity = densityAtAltitude(altitude)
    S = wingReferenceArea(c, b)
    AR = aspectRatio(c, b)
    averageLift = 0.5 * freestreamDensity * averageVelocity**2 * S * CL
    groundEffectCoefficient = (16 * wingHeightOffGround/b)**2 / (1 + (16 * wingHeightOffGround/b)**2)
    averageDrag = 0.5 * freestreamDensity * averageVelocity**2 * S * (profileDragCoefficient(mainAirfoilData, CL) + groundEffectCoefficient * inducedDragCoefficient(CL, AR, spanEfficiencyFactor))
    
    return (liftoffVelocity**2 * airplaneWeight) / (g0 * 2 * (thrust - averageDrag + coefficientOfRollingFriction * (airplaneWeight - averageLift)))

def landingDistance(altitude, airplaneWeight, stallVelocity, thrust, b, c, CL, wingHeightOffGround, spanEfficiencyFactor):
    touchdownVelocity = 1.3 * stallVelocity
    averageVelocity = 0.7 * touchdownVelocity
    S = wingReferenceArea(c, b)
    AR = aspectRatio(c, b)
    freestreamDensity = densityAtAltitude(altitude)
    averageLift = 0.5 * freestreamDensity * averageVelocity**2 * S * CL
    groundEffectCoefficient = (16 * wingHeightOffGround/b)**2 / (1 + (16 * wingHeightOffGround/b)**2)
    averageDrag = 0.5 * freestreamDensity * averageVelocity**2 * S * (profileDragCoefficient(mainAirfoilData, CL) + groundEffectCoefficient * inducedDragCoefficient(CL, AR, spanEfficiencyFactor))
    
    return (touchdownVelocity**2 * airplaneWeight) / (g0 * 2 * (averageDrag + 0.4 * (airplaneWeight - averageLift)))

def timeToClimbToAltitude(altitude, weight, c, b):
    h1 = 0 #initial altitude (m)
    S = wingReferenceArea(c, b)
    rho0 = densityAtAltitude(0) #air density at sea level (kg/m^3)
    V0 = (2*weight/(rho0*S*Cl))**.5 #Velocity at sea-level (m/s)
    PR0 = ((2*(weight**3)*(Cd**2))/(rho0*S*(Cl**3)))**.5
    PA0 = Thrust * V0
    RCarray = [] 
    altitudes = []
    for h in range(h1, int(altitude)+1):
        rhoAlt = densityAtAltitude(h) #density of air at altitude 'h' (kg/m^3)
        V = V0 * ((rho0/rhoAlt)**.5) #Velocity of aircraft (m/s)
        PA = PA0 * (rhoAlt/rho0) #power available (N)
        PR = PR0 * ((rho0/rhoAlt)**.5) #power required (N)
        RC = (PA - PR) / weight #Rate of Climb (m/min)
        RCarray.append(1/RC)
        altitudes.append(h)
    return trapz(RCarray, altitudes) #Time to altitude (min)

def initialRoC(Weight):
    h1 = 0 #initial altitude (m)
    S = wingReferenceArea(c,b)
    rho0 = densityAtAltitude(0) #air density at sea level (kg/m^3)
    V0 = (2*Weight/(rho0*S*Cl))**.5 #Velocity at sea-level (m/s)
    PR0 = ((2*(Weight**3)*(Cd**2))/(rho0*S*(Cl**3)))**.5
    PA0 = Thrust * V0
    return (PA0 - PR0) / Weight
    
def wingLocation(altitude, L, c, b):
    q = dynamicPressure(densityAtAltitude(altitude), cruiseSpeedAtAltitude(altitude, emptyMass, c, b))
    S = wingReferenceArea(c, b)
    M = Cm * q * S * c # Moment of main wing
    return (-0.5*(emptyWeight - engineWeight)*L + (1/16)*emptyWeight + M)/(engineWeight - (7/8)*emptyWeight)

def cruiseSpeedAtAltitude(altitude, weight, c, b):
    rho0 = densityAtAltitude(altitude) # air density at altitude
    S = wingReferenceArea(c, b)
    Cl0 = liftCoefficientAtAngleOfAttack(mainAirfoilData, 0)
    return sqrt(7/8*weight / (0.5 * Cl0 * rho0 * S))

################################################################################
# ENGINE ANALYSIS
################################################################################
