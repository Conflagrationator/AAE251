from Reference import *
from AirplaneParameters import *

################################################################################
# CALCULATED PARAMETERS
################################################################################

S = wingReferenceArea(averageChord, averageWingspan)
AR = aspectRatio(averageChord, averageWingspan)

################################################################################
# PERFORMANCE VALUES
################################################################################

# RANGE

airplaneRange = turbojetRange(freestreamDensity, S, CL, CD, tsfc, fullWeight, emptyWeight)

# ENDURANCE

Endurance = airplaneEndurance(.00008064, Cl, Cd, 32267, 30000)
convert(Endurance, "s", "hr")

# TIME TO CLIMB



# TAKEOFF DISTANCE



# LANDING DISTANCE



################################################################################
# PLOTS
################################################################################
