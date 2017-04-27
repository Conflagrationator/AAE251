from scipy import *
from Reference import *

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

def liftCoefficientAtAngleOfAttack(angle):
    AnglesAndCls = list(map(lambda row: (row["Alpha"], row["Cl"]), airfoilData))
    return interpolate(AnglesAndCls, angle)

def profileDragCoefficient(CL):
    ClsAndCds = list(map(lambda row: (row["Cl"], row["Cd"]), airfoilData))
    return interpolate(ClsAndCds, CL)

def inducedDragCoefficient(CL, AR, spanEfficiencyFactor):
    return CL**2 / (pi * AR * spanEfficiencyFactor)

def powerRequired(airplaneWeight, CL, CD, density):
    return sqrt((2 * airplaneWeight * CD**2) / (density * S * CL**2))

# CONVENIENCE FUNCTIONS

def totalDragCoefficient(CL, AR, spanEfficiencyFactor):
    return profileDragCoefficient(CL) + inducedDragCoefficient(CL, AR, spanEfficiencyFactor)

def powerGivenThrust(thrust, freestreamVelocity):
    return thrust * freestreamVelocity

def thrustGivenPower(power, freestreamVelocity):
    return power / freestreamVelocity

# PERFORMANCE

def turbojetRange(freestreamDensity, S, CL, CD, tsfc, fullWeight, emptyWeight):
    return 2 * sqrt(2 / (freestreamDensity * S)) * (sqrt(CL) / CD) * (1 / tsfc) * (sqrt(fullWeight) - sqrt(emptyWeight))

def turbojetEndurance(tsfc, CL, CD, fullWeight, emptyWeight):
    return (1 / tsfc) * (CL / CD) * log(fullWeight / emptyWeight)

def liftoffDistance(altitude, airplaneWeight, stallVelocity, thrust, coefficientOfRollingFriction, b, c, CL, wingHeightOffGround, spanEfficiencyFactor):
    liftoffVelocity = 1.2 * stallVelocity # approximate
    averageVelocity = 0.7 * liftoffVelocity
    freestreamDensity = densityAtAltitude(altitude)
    averageLift = 0.5 * freestreamDensity * averageVelocity**2 * S * CL
    groundEffectCoefficient = (16 * wingHeightOffGround/b)**2 / (1 + (16 * wingHeightOffGround/b)**2)
    averageDrag = 0.5 * freestreamDensity * averageVelocity**2 * S * (profileDragCoefficient(CL, AR) + groundEffectCoefficient * inducedDragCoefficient(CL, aspectRatio(c, b), spanEfficiencyFactor))
    
    return (liftoffVelocity**2 * airplaneWeight) / (g0 * 2 * (thrust - averageDrag + coefficientOfRollingFriction * (airplaneWeight - averageLift)))

def landingDistance(altitude, airplaneWeight, stallVelocity, thrust, b, c, CL, wingHeightOffGround, spanEfficiencyFactor):
    touchdownVelocity = 1.3 * stallVelocity
    averageVelocity = 0.7 * touchdownVelocity
    averageLift = 0.5 * freestreamDensity * averageVelocity**2 * S * CL
    groundEffectCoefficient = (16 * wingHeightOffGround/b)**2 / (1 + (16 * wingHeightOffGround/b)**2)
    averageDrag = 0.5 * freestreamDensity * averageVelocity**2 * S * (profileDragCoefficient(CL, AR) + groundEffectCoefficient * inducedDragCoefficient(CL, aspectRatio(c, b), spanEfficiencyFactor))
    
    return (touchdownVelocity**2 * airplaneWeight) / (g0 * 2 * (averageDrag + 0.4 * (airplaneWeight - averageLift)))

################################################################################
# ENGINE ANALYSIS
################################################################################
