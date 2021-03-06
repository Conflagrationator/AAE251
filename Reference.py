import csv
from Launch import *
from Conversions import *
from scipy import *

################################################################################
# UTILITY FUNCTIONS
################################################################################

def safeFloat(x):
    """like float, but doesn't crash"""
    try:
        return float(x)
    except ValueError:
        return float("nan")

def interpolate(associatedValues, value): # [(a, b)] -> a -> b
    """given a list of tuples where the first item in a tuple is one value and 
    the second is an associated value, it finds the associated value to a given 
    value passed in"""
    
    # Validation
    if value < associatedValues[0][0]:
        raise Exception("value is below all values supplied")
    elif value > associatedValues[-1][0]:
        raise Exception("value is above all values supplied")
    
    # Find the values immediately above & below the value specified
    for association in associatedValues:
        if association[0] < value:
            below = association
        if association[0] > value:
            above = association
            break
    
    # Do Interpolation
    return (above[1]-below[1])/(above[0]-below[0]) * (value - below[0]) + below[1]

################################################################################
# REFERENCE NUMBERS
################################################################################

# UNIVERSAL CONSTANTS

G = 6.67408e-11 # m^3/(kg*s^2) # universal gravitation constant

# EARTH CONSTANTS

g0 = 9.80665 # m/s^2 # gravitational acceleration at sea level
mEarth = 5.9723e24 # kg # mass of earth
rEarth = 6378137 # m # radius of earth
muEarth = G * mEarth # m^3/s^2

# ATMOSPERE PARAMETERS

airIdealGasConstant = 287.058 # J/(kg*K) # ideal gas constant of air
airHeatCapacityRatio = 1.4 # unitless # ratio of specific heats

# LAUNCH LOSSES

dVdragLoss = dragLossUpToAltitude(0) # m/s
dVgravityLoss = gravityLossUpToAltitude(0) # m/s
dVSteeringLoss = steeringLoss() # m/s

# TRANSFERS

dVfor500 = 195.40362680297374 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoTransfer = 2467.596447585046 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoStatOrbit = 4478.0452652 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s

# ROCKET INFORMATION

# [(name of rocket, Isp, mass, fuel capacity)]

#[Stage 1 , Stage 2]

f_inert = [0.08, 0.12] # inert mass fraction 
Isp = [310, 360] # s
dV = [5716, 8612] #m/s
m_pay = 5000 #kg
dV_needed = 14.354 # m/s
m_inert = [10000]

# TODO: guys, please fix your naming conflicts...

f_inert = [.08,.15] # inert mass fraction 
Isp = [360, 360] # s
payload = 5000
fairing = 1000
m_pay = payload+fairing #kg


# PARAFOIL INFORMATION

#Found Cd using m*g = 0.5*Cd*rho*A*vt**2 (Drag at Terminal Velocity, solved for Cd)
CdChute = 2.510418402

# ORBIT INFORMATION

h1 = 200000 # m
h2 = 500000 # m
delta = 28.474 # Degrees

# PLANE DATA 

coefficientOfRF = 0.02 
spanEF = 0.8
wingHeight = 4
captureAltitude = convert(55000, "ft", "m") #final altitude (m)
theta = 16.5 #angle of attack (Degrees)
Cd = 0.04423 #coefficient of drag
EngineNum = 4 #Number of engines on the plane
Thrust = convert(12670, "lbs", "N") * EngineNum #(N)
tsfc = convert(0.655, "lbm/hr/lbf", "kg/s/N")
wingspan = 40 #(m)
chord = 4 #(m)
fullMass = 37000 #(kg)
fullWeight = fullMass * g0 #(N)
emptyMass = 20000
emptyWeight = emptyMass * g0
fuelMass = 5000 
fuelWeight = fuelMass * g0
engineMass = 2335 * EngineNum
engineWeight = engineMass * g0
Cm = 0.0525
cruiseAltitude = convert(20000, "ft", "m")
CostperKGofJF = 100 #$/kg
CostperKGofIM = 1000 #$/kg

# Creates a list "airfoilData" which has the format [{"category": value}] for
# each entry in the csv file
with open("Resources/TurbofanData.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    columnTitles = next(reader) # consume first line & get column titles
    turbofanData = list(map(lambda row: dict(zip(columnTitles, [row[0]] + list(map(safeFloat, row[1:])))), reader))

# AIRFOIL DATA

# Creates a list "airfoilData" which has the format [{"category": value}] for
# each entry in the csv file
with open("Resources/Naca2412.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    columnTitles = next(reader) # consume first line & get column titles
    mainAirfoilData = list(map(lambda row: dict(zip(columnTitles, map(float, row))), reader)) # get rows as dictionaries

# AIRCRAFT PERFORMANCE
