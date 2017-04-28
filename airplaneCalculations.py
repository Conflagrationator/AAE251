from Reference import *
from AirplaneParameters import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(chord, wingspan)
AR = aspectRatio(chord, wingspan)
maxCL = max(list(map(lambda row: row["Cl"], mainAirfoilData)))
Cl0 = liftCoefficientAtAngleOfAttack(mainAirfoilData, 0)

################################################################################
# PERFORMANCE
################################################################################

# SPEEDS

VStall = stallSpeed(emptyWeight + fullWeight, densityAtAltitude(convert(60000, "ft", "m")), S, maxCL)
VCruise = cruiseSpeedAtAltitude(cruiseAltitude, emptyWeight + fullWeight, chord, wingspan)

# RANGE

Range = airplaneRange(densityAtAltitude(convert(60000, "ft", "m")), S, Cl, Cd, tsfc, fullWeight, emptyWeight)

# ENDURANCE

Endurance = airplaneEndurance(0.00008064, Cl, Cd, 32267, 30000)

# TIME TO CLIMB

Climb = timeToClimbToAltitude(maxAltitude, emptyWeight + fuelWeight, chord, wingspan)

# TAKEOFF DISTANCE

takeoffDist = liftoffDistance(0, emptyWeight + fuelWeight, VStall, Thrust, coefficientOfRF, wingspan, chord, Cl0, wingHeight, spanEF)

# LANDING DISTANCE

landingDist = landingDistance(0, emptyWeight + fuelWeight, VStall, Thrust, wingspan, chord, Cl0, wingHeight, spanEF)

################################################################################
# OUTPUT
################################################################################

# PERFORMANCE 

print("Stall Speed: {0} kts".format(VStall, "m/s", "kts"))
print("Cruise Speed: {0} kts".format(VCruise, "m/s", "kts"))
print("Range: {0} km".format(convert(Range, "m", "km")))
print("Endurance: {0} hrs".format(convert(Endurance, "s", "hrs")))
print("Time to Climb to {0} ft: {1} min".format(int(round(convert(maxAltitude, "m", "ft"), 0)), convert(Climb, "s", "min")))
print("Takeoff Distance: {0} ft".format(convert(takeoffDist, "m", "ft")))
print("Landing Distance: {0} ft".format(convert(landingDist, "m", "ft")))
