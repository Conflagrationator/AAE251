################################################################################
# LOSS CALCULATIONS
################################################################################

def dragLossUpToAltitude(altitude):
    """gives the drag loss up to the given altitude"""
    if 0 <= altitude and altitude <= 20000:
        return 150 - 0.0075*altitude # m/s
    else:
        raise Exception("Invalid at given altitude: {0}".format(altitude))

def gravityLossUpToAltitude(altitude):
    """gives the gravity loss up to a given altitude"""
    if 0 <= altitude and altitude <= 20000:
        return 1500 - 0.075*altitude # m/s
    else:
        raise Exception("Invalid at given altitude: {0}".format(altitude))

def steeringLoss():
    """gives the steering loss for a flight"""
    return 200 # m/s
