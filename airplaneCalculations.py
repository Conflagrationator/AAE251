from Reference import *
from AirplaneParameters import *

print("--------------------------------------------------------------------------------")

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(chord, wingspan)
AR = aspectRatio(chord, wingspan)
maxCl = max(list(map(lambda row: row["Cl"], mainAirfoilData)))
Cl0 = liftCoefficientAtAngleOfAttack(mainAirfoilData, 0)
Cd0 = totalDragCoefficient(Cl0, AR, spanEF, mainAirfoilData)
takeoffWeight = emptyWeight + fuelWeight

################################################################################
# PERFORMANCE
################################################################################

# SPEEDS

VStall0 = stallSpeed(takeoffWeight, densityAtAltitude(0), S, maxCl)
VStallCapture = stallSpeed(takeoffWeight, densityAtAltitude(captureAltitude), S, maxCl)
VCruise = cruiseSpeedAtAltitude(cruiseAltitude, takeoffWeight, chord, wingspan)

# RANGE

Range = airplaneRange(densityAtAltitude(cruiseAltitude), S, Cl0, Cd0, tsfc, fullWeight, emptyWeight)

# ENDURANCE

Endurance = airplaneEndurance(tsfc, Cl0, Cd0, fullWeight, emptyWeight)

# TIME TO CLIMB

Climb = timeToClimbToAltitude(captureAltitude, takeoffWeight, chord, wingspan, maxCl)

# TAKEOFF DISTANCE

takeoffDist = liftoffDistance(0, takeoffWeight, VStall0, Thrust, coefficientOfRF, wingspan, chord, Cl0, wingHeight, spanEF)

# LANDING DISTANCE

landingDist = landingDistance(0, takeoffWeight, VStall0, Thrust, wingspan, chord, Cl0, wingHeight, spanEF)

################################################################################
# OUTPUT
################################################################################

# PARAMETERS
print("---- PARAMETERS ----")

print("Wingspan: {0} m".format(wingspan))
print("Mean Chord Length: {0} m".format(chord))
print("Wing Reference Area: {0} m^2".format(S))
print("Aspect Ratio: {0}".format(AR))
print("Airplane Empty Weight: {0} lbs".format(convert(emptyWeight, "N", "lbs")))
print("Airplane Full Weight: {0} lbs".format(convert(fullWeight, "N", "lbs")))
print("Airplane Fuel Capacity: {0} lbs".format(convert(fuelWeight, "N", "lbs")))
print("Total Engine Weight: {0} lbs".format(convert(engineWeight, "N", "lbs")))
print("Cruising Altitude: {0} ft".format(int(round(convert(cruiseAltitude, "m", "ft"), 0))))
print("Capture Altitude: {0} ft".format(int(round(convert(captureAltitude, "m", "ft"), 0))))
print("Engine Thrust Specific Fuel Consumption: {0} lbm/hr/lbf".format(convert(tsfc, "kg/N/s", "lbm/hr/lbf")))
print("Engine Thrust Specific Fuel Consumption: {0} kg/N/s".format(tsfc))

# PERFORMANCE 
print("---- PERFORMANCE ----")

print("Stall Speed at Sea Level: {0} kts".format(convert(VStall0, "m/s", "kts")))
print("Stall Speed at Capture Altitude: {0} kts".format(convert(VStallCapture, "m/s", "kts")))
print("Cruise Speed: {0} kts".format(convert(VCruise, "m/s", "kts")))
print("Range: {0} mi".format(convert(Range, "m", "mi")))
print("Endurance: {0} hrs".format(convert(Endurance, "s", "hrs")))
print("Time to Climb to Capture Altitude: {0} min".format(convert(Climb, "s", "min")))
print("Takeoff Distance: {0} ft".format(convert(takeoffDist, "m", "ft")))
print("Landing Distance: {0} ft".format(convert(landingDist, "m", "ft")))
