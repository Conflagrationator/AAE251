from Reference import *
from AirplaneParameters import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(chord, wingspan)
AR = aspectRatio(chord, wingspan)
maxCL = max(list(map(lambda row: row["Cl"], mainAirfoilData)))
Cl0 = liftCoefficientAtAngleOfAttack(mainAirfoilData, 0)
print(CL0)
VStall = stallSpeed(fullWeight, densityAtAltitude(convert(60000, "ft", "m")), S, maxCL)

################################################################################
# PERFORMANCE
################################################################################

# RANGE

Range = airplaneRange(densityAtAltitude(convert(60000, "ft", "m")), S, Cl, Cd, tsfc, fullWeight, emptyWeight)

# ENDURANCE

Endurance = airplaneEndurance(0.00008064, Cl, Cd, 32267, 30000)

# TIME TO CLIMB

Climb = timeToClimbToAltitude(maxAltitude, fullWeight, chord, wingspan)

# TAKEOFF DISTANCE

takeoffDist = liftoffDistance(0, fullWeight, VStall, Thrust, coefficientOfRF, wingspan, chord, Cl0, wingHeight, spanEF)

# LANDING DISTANCE

landingDist = landingDistance(0, fullWeight, VStall, Thrust, wingspan, chord, Cl0, wingHeight, spanEF)

################################################################################
# OUTPUT
################################################################################

# PERFORMANCE 

print("Range: {0} km".format(convert(Range, "m", "km")))
print("Endurance: {0} hrs".format(convert(Endurance, "s", "hrs")))
print("Time to Climb to {0} ft: {1} min".format(int(round(convert(maxAltitude, "m", "ft"), 0)), convert(Climb, "s", "min")))
print("Takeoff Distance: {0} ft".format(convert(takeoffDist, "m", "ft")))
print("Landing Distance: {0} ft".format(convert(landingDist, "m", "ft")))
