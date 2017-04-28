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



# TIME TO CLIMB



# TAKEOFF DISTANCE



# LANDING DISTANCE



################################################################################
# PLOTS
################################################################################
