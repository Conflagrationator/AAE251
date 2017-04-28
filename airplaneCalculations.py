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
VStall = stallSpeed(W, densityAtAltitude(hf), S, maxCL)
VCruise = CruiseSpeedCalc(hCruise, (fuelWeight+emptyWeight), c, b)

################################################################################
# PERFORMANCE VALUES
################################################################################

# CRUISE SPEED

VCruise = CruiseSpeedCalc(hCruise, (fuelWeight+emptyWeight), c, b)
print('Cruise Speed(m/s):   ',VCruise)

# RANGE

airplaneRange = turbojetRange(densityAtAltitude(convert(25000,"ft","m")), S, Cl, Cd, tsfc, (emptyWeight+fuelWeight), emptyWeight)
print('Range(km):           ', convert(airplaneRange, "m", "km"))

# ENDURANCE

Endurance = airplaneEndurance(tsfc, Cl, Cd, (emptyWeight+fuelWeight), emptyWeight)
print('Endurance(hr):       ', convert(Endurance, "s", "hr"))

# INITIAL RATE OF CLIMB 

RC0 = initialRoC(emptyWeight + fuelWeight)
print('Rate of Climb(km/hr):', convert(RC0, "m/s","km/hr"))

# TIME TO CLIMB

Climb = timeToClimb(emptyWeight + fuelWeight)
print('Time to Climb(hr):   ', convert(Climb,"s","hr"))

# TAKEOFF DISTANCE

LiftD = liftoffDistance(0, (emptyWeight+fuelWeight), VStall, Thrust, coefficientOfRF, b, c, Cl0, wingHeight, spanEF)
print('Liftoff Distance(m): ', LiftD)

# LANDING DISTANCE

LandD = landingDistance(0, (emptyWeight+fuelWeight), VStall, Thrust, b, c, Cl0, wingHeight, spanEF)
print('Landing Distance(m): ', LandD)

################################################################################
# PLOTS
################################################################################
