from Launch import *

################################################################################
# REFERENCE NUMBERS
################################################################################

# EARTH PARAMETERS

g0 = 9.80665 # m/s^2

# LAUNCH LOSSES

dVdragLoss = dragLossUpToAltitude(20000) # m/s
dVgravityLoss = gravityLossUpToAltitude(20000) # m/s
dVSteeringLoss = steeringLoss() # m/s

# TRANSFERS

dVfor500 = .19540362680297374 * 10**3 + dragdV + gravdV + steeringdV # m/s
dVforGeoTransfer = 2.467596447585046 * 10**3 + dragdV + gravdV + steeringdV # m/s
dVforGeoStatOrbit = 4.4780452652 * 10**3 + dragdV + gravdV + steeringdV # m/s

# ROCKET INFORMATION

# [(name of rocket, Isp, mass, fuel capacity)]
