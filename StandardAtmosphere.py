from scipy import *

################################################################################
# DATA
################################################################################

# EARTH FACTS

R = 287.058 # ideal gas constant for earth air, in J/kg*K
r = 6356766 # radius of the earth, in m
g = 9.80665 # gravitational acceleration at sea level, in m/s^2

# ATMOSPHERE FACTS

baseHeights = [0, 11000, 25000, 47000, 53000, 79000, 90000, 105000] # (geopotential) heights for the beginning of each layer, in m
baseTemperatures = [288.16, 216.66, 216.66, 282.66, 282.66, 165.66, 165.66, 225.66] # temperature for the beginning of each layer, in K
tempGradients = [-0.0065, 0, 0.003, 0, -0.0045, 0, 0.004, NaN] # temperature gradients for each layer, in K/m (last one represents no information above that height)
basePressures = [101325.0, 22634.008746132295, 2489.1856086672196, 120.49268001877302, 58.347831704016428, 1.0101781258352585, 0.10452732009352216, nan] # in Pa # precalculated
baseDensities = [1.225, 0.3639451299338376, 0.040025034448687088, 0.0014850787413445172, 0.00071914015402165508, 2.124386216253755e-05, 2.1981905205581133e-06, nan] # in kg/m^3 # precalculated

################################################################################
# FUNCTIONS
################################################################################

def layerIndexForheight(h): # get a reference to the place in the lists where the base information is
    return baseHeights.index(next(height for height in reversed(baseHeights) if height <= h))

def geopotentialAltitudeForHeight(hg):
    return (r * hg) / (r + hg)

def temperatureAtHeight(h):
    i = layerIndexForheight(h)
    return baseTemperatures[i] + tempGradients[i] * (h - baseHeights[i])

def isothermalLayerPressureAtHeight(h, basePressure, baseHeight, layerTemperature):
    return basePressure * exp(-(g * (h - baseHeight) / (R * layerTemperature)))

def isothermalLayerDensityAtHeight(h, baseDensity, basePressure, pressureAtHeight):
    return baseDensity * (pressureAtHeight / basePressure)

def gradientLayerPressureAtHeight(h, basePressure, temperatureAtHeight, baseTemperature, layerTemperatureGradient):
    return basePressure * (temperatureAtHeight / baseTemperature)**(-(g) / (R * layerTemperatureGradient))

def gradientLayerDensityAtHeight(h, baseDensity, temperatureAtHeight, baseTemperature, layerTemperatureGradient):
    return baseDensity * (temperatureAtHeight / baseTemperature)**-(g/(R * layerTemperatureGradient) + 1)

def baseInformation(h):
    i = layerIndexForheight(h)
    return baseHeights[i], baseTemperatures[i], tempGradients[i], basePressures[i], baseDensities[i]

def informationAtHeight(hg):
    """Takes a Geometric Altitude and Returns the Geometric Altitude, Geopotential
     Altitude, Temperature, Pressure and Density at that altitude in that order"""
    h = geopotentialAltitudeForHeight(hg)
    t = temperatureAtHeight(h)

    baseHeight, baseTemperature, layerGradient, basePressure, baseDensity = baseInformation(h)
    
    if (layerGradient == 0): # isothermal layer
        p = isothermalLayerPressureAtHeight(h, basePressure, baseHeight, baseTemperature)
        d = isothermalLayerDensityAtHeight(h, baseDensity, basePressure, p)
    else: # gradient layer
        p = gradientLayerPressureAtHeight(h, basePressure, t, baseTemperature, layerGradient)
        d = gradientLayerDensityAtHeight(h, baseDensity, t, baseTemperature, layerGradient)
    
    return hg, h, t, p, d
