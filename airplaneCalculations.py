from Reference import *
from AirplaneParameters import *
from Conversions import *
from Atmosphere import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(c,b)
AR = aspectRatio(c, b)
maxCL = max(list(map(lambda row: row["Cl"], airfoilData)))
VStall = stallSpeed(W, densityAtAltitude(convert(60000,"ft","m")), S, maxCL)

################################################################################
# PERFORMANCE VALUES
################################################################################

# RANGE

#airplaneRange = turbojetRange(densityAtAltitude(convert(60000,"ft","m")), S, Cl, Cd, tsfc, fullWeight, emptyWeight)
#print(airplaneRange)

# ENDURANCE

Endurance = airplaneEndurance(.00008064, Cl, Cd, 32267, 30000)
print(convert(Endurance, "s", "hr"))

# TIME TO CLIMB

Climb = timeToClimb()
print(convert(Climb,"s","hr"))

# TAKEOFF DISTANCE



# LANDING DISTANCE



################################################################################
# PLOTS
################################################################################
