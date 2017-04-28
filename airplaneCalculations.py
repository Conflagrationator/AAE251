from Reference import *
from AirplaneParameters import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(chord, wingspan)
AR = aspectRatio(chord, wingspan)

wingClmax = max(list(map(lambda row: row["Cl"], airfoilData)))
wingCl0 = liftCoefficientAtAngleOfAttack(0)
wingCd = totalDragCoefficient(wingCl0, AR, spanEF)

################################################################################
# PERFORMANCE
################################################################################

# RANGE

airplaneRange = airplaneRange(densityAtAltitude(cruiseAltitude), S, wingCl0, wingCd, tsfc, fullWeight, emptyWeight)

# ENDURANCE



# TIME TO CLIMB



# TAKEOFF DISTANCE



# LANDING DISTANCE



################################################################################
# OUTPUT
################################################################################

# RANGE

print("Range: {0} m = {1} km = {2} mi".format(
    airplaneRange,
    convert(airplaneRange, "m", "km"),
    convert(airplaneRange, "m", "mi")))

# CRUISE SPEED for ALTITUDES

altitudes = range(0, int(convert(60000, "ft", "m")))

# cruiseSpeedAtAltitude(altitude, weight, c, b)
