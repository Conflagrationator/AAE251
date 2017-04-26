from scipy import *
from Reference import *

################################################################################
# AIRPLANE PARAMETER FUNCTIONS
################################################################################
# tsfc = thrust specific fuel consumption
# CL = airplane lift coefficient
# CD = airplane drag coefficient

def stallSpeed(weight, freestreamDensity, wingReferenceArea, maxCL):
    return sqrt((2 * weight) / (freestreamDensity * wingReferenceArea * maxCL))

def turbojetRange(freestreamDensity, wingReferenceArea, CL, CD, tsfc, fullWeight, emptyWeight):
    return 2 * sqrt(2 / (freestreamDensity * wingReferenceArea)) * (sqrt(CL) / CD) * (1 / tsfc) * (sqrt(fullWeight) - sqrt(emptyWeight))

def turbojetEndurance(tsfc, CL, CD, fullWeight, emptyWeight):
    return (1 / tsfc) * (CL / CD) * log(fullWeight / emptyWeight)


################################################################################
# ENGINE ANALYSIS
################################################################################

def runForEachTurbofan(function):
    map(function, turbofanData)
