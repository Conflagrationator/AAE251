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

def wingReferenceArea(c, b):
    return c*b

def stallSpeed(airplaneWeight, freestreamDensity, S, maxCL):
    return sqrt((2 * airplaneWeight) / (freestreamDensity * S * maxCL))

def profileDragCoefficient(CL):
    ClsAndCds = list(map(lambda row: (row["Cl"], row["Cd"]), airfoilData))
    return interpolate(ClsAndCds, CL)

def inducedDragCoefficient(CL, aspectRatio, spanEfficiencyFactor):
    return CL**2 / (pi * aspectRatio * spanEfficiencyFactor)

# PERFORMANCE

def turbojetRange(freestreamDensity, S, CL, CD, tsfc, fullWeight, emptyWeight):
    return 2 * sqrt(2 / (freestreamDensity * S)) * (sqrt(CL) / CD) * (1 / tsfc) * (sqrt(fullWeight) - sqrt(emptyWeight))

def turbojetEndurance(tsfc, CL, CD, fullWeight, emptyWeight):
    return (1 / tsfc) * (CL / CD) * log(fullWeight / emptyWeight)

################################################################################
# ENGINE ANALYSIS
################################################################################
