from Launch import *

################################################################################
# REFERENCE NUMBERS
################################################################################

# EARTH PARAMETERS

g0 = 9.80665 # m/s^2

# ATMOSPERE PARAMETERS

airIdealGasConstant = 287.058 # J/(kg*K) # ideal gas constant of air
airHeatCapacityRatio = 1.4 # unitless # ratio of specific heats

# LAUNCH LOSSES

dVdragLoss = dragLossUpToAltitude(20000) # m/s
dVgravityLoss = gravityLossUpToAltitude(20000) # m/s
dVSteeringLoss = steeringLoss() # m/s

# TRANSFERS

dVfor500 = 195.40362680297374 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoTransfer = 2467.596447585046 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoStatOrbit = 4478.0452652 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s

# ROCKET INFORMATION

# [(name of rocket, Isp, mass, fuel capacity)]
