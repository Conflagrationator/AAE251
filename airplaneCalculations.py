from Reference import *
from AirplaneParameters import *
from matplotlib.pyplot import *
from numpy import *

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
# PRICING
################################################################################
Cost = costOfFuel(fuelWeight) + costOfInertMass(emptyWeight)

################################################################################
# OUTPUT
################################################################################

# PARAMETERS
print("---- PRICE ----")

print("Price of Airplane: ${0}".format(Cost))

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
print("Range: {0} km".format(convert(Range, "m", "km")))
print("Endurance: {0} hrs".format(convert(Endurance, "s", "hrs")))
print("Time to Climb to Capture Altitude: {0} min".format(convert(Climb, "s", "min")))
print("Takeoff Distance: {0} ft".format(convert(takeoffDist, "m", "ft")))
print("Landing Distance: {0} ft".format(convert(landingDist, "m", "ft")))

# Thrust Available & Thrust Required vs. Velocity for Sea Level, cruise altitude, capture altitude

def safeThrustRequired(captureAltitude, speed, takeoffWeight, chord, wingspan, spanEF):
    """returns not a number if fails"""
    try:
        return thrustRequired(captureAltitude, speed, takeoffWeight, chord, wingspan, spanEF)
    except Exception:
        return float("nan")

speeds = list(range(0, 500)) # m/s
thrustsRequiredSea = list(map(lambda speed: safeThrustRequired(0, speed, takeoffWeight, chord, wingspan, spanEF), speeds))
thrustsRequiredCruise = list(map(lambda speed: safeThrustRequired(cruiseAltitude, speed, takeoffWeight, chord, wingspan, spanEF), speeds))
thrustsRequiredCapture = list(map(lambda speed: safeThrustRequired(captureAltitude, speed, takeoffWeight, chord, wingspan, spanEF), speeds))
thrustAvailableSea = repeat(Thrust * (densityAtAltitude(0)/densityAtAltitude(0)), len(speeds))
thrustAvailableCruise = repeat(Thrust * (densityAtAltitude(cruiseAltitude)/densityAtAltitude(0)), len(speeds))
thrustAvailableCapture = repeat(Thrust * (densityAtAltitude(captureAltitude)/densityAtAltitude(0)), len(speeds))

figure(1)
plot(speeds, thrustAvailableSea, label="TA Sea", color="blue")
plot(speeds, thrustsRequiredSea, label="TR Sea", color="red")
title("Thrust vs. Speed at Sea Level")
xlabel("Speed (m/s)")
ylabel("Thrust (N)")
legend()

figure(2)
plot(speeds, thrustAvailableCruise, label="TA Cruise", color="blue")
plot(speeds, thrustsRequiredCruise, label="TR Cruise", color="red")
title("Thrust vs. Speed at Cruise Altitude")
xlabel("Speed (m/s)")
ylabel("Thrust (N)")
legend()

figure(3)
plot(speeds, thrustAvailableCapture, label="TA Capture", color="blue")
plot(speeds, thrustsRequiredCapture, label="TR Capture", color="red")
title("Thrust vs. Speed at Capture Altitude")
xlabel("Speed (m/s)")
ylabel("Thrust (N)")
legend()

# Show all Plots
show()
