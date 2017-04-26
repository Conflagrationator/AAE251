from Launch import *

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
dV = [5000, 2000] #m/s
m_pay = 10000 #kg
dV_needed = 9000 # m/s
m_inert = [10000]

# PARAFOIL INFORMATION

#Found Cd using m*g = .5*Cd*rho*A*vt**2 (Drag at Terminal Velocity, solved for Cd)
CdChute = 2.510418402

# ORBIT INFORMATION

h1 = 200000 #m
h2 = 500000 #m
delta = 28.474 #Degrees
