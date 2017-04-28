from Reference import *
from AirplaneParameters import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(chord, wingspan)
AR = aspectRatio(chord, wingspan)
maxCL = max(list(map(lambda row: row["Cl"], mainAirfoilData)))
CL0 = liftCoefficientAtAngleOfAttack(mainAirfoilData, 0)
VStall = stallSpeed(fullWeight, densityAtAltitude(convert(60000, "ft", "m")), S, maxCL)

################################################################################
# PERFORMANCE
################################################################################

# RANGE

Range = airplaneRange(densityAtAltitude(convert(60000, "ft", "m")), S, Cl, Cd, tsfc, fullWeight, emptyWeight)
print(Range)

# ENDURANCE

Endurance = airplaneEndurance(0.00008064, Cl, Cd, 32267, 30000)
print(convert(Endurance, "s", "hr"))

# TIME TO CLIMB

Climb = timeToClimbToAltitude(maxAltitude, fullWeight, chord, wingspan)
print(convert(Climb, "s", "hr"))

# TAKEOFF DISTANCE

Stakeoff = liftoffDistance(0, fullWeight, VStall, Thrust, coefficientOfRF, wingspan, chord, CL0, wingHeight, spanEF)
print(Stakeoff)

# LANDING DISTANCE

Slanding = landingDistance(0, fullWeight, VStall, Thrust, wingspan, chord, CL0, wingHeight, spanEF)
print(Slanding)

################################################################################
# PLOTS
################################################################################
