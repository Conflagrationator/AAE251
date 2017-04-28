from Reference import *
from AirplaneParameters import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(c,b)
AR = aspectRatio(c, b)
maxCL = max(list(map(lambda row: row["Cl"], airfoilData)))
VStall = stallSpeed((emptyWeight+fuelWeight), densityAtAltitude(hCruise), S, maxCL)
VCruise = CruiseSpeedCalc(hCruise, (fuelWeight+emptyWeight), c, b)

################################################################################
# PERFORMANCE
################################################################################

# RANGE

airplaneRange = airplaneRange(densityAtAltitude(convert(25000,"ft","m")), S, Cl, Cd, tsfc, (emptyWeight+fuelWeight), emptyWeight)

# ENDURANCE

Endurance = airplaneEndurance(tsfc, Cl, Cd, 32267, 30000)

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
print("Stall Speed {0} m/s".format(VStall))
print("Range: {0} km".format(convert(airplaneRange, "m", "km")))
print("Endurance: {0} hrs".format(convert(Endurance, "s", "hrs")))
print("Time to Climb to {0} ft: {1} min".format(int(round(convert(maxAltitude, "m", "ft"), 0)), convert(Climb, "s", "min")))
print("Takeoff Distance: {0} ft".format(convert(takeoffDist, "m", "ft")))
print("Landing Distance: {0} ft".format(convert(landingDist, "m", "ft")))
