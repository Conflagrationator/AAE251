################################################################################
# CONVERSION TABLE
################################################################################

# NOTE: all unit multipliers are related back to their SI base unit
#       essentially, all the values in the dictionary represent the same vlaue

length = {
    "m": 1,
    "km": 1e-3,
    "ft": 3.28084}

time = {
    "s": 1,
    "min": 1/60,
    "hr": 1/(60*60),
    "hrs": 1/(60*60)}

mass = {
    "kg": 1,
    "slug": 0.0685218,
    "slugs": 0.0685218,
    "metric ton": 1000,
    "metric tons": 1000,
    "ton": 907.185,
    "tons": 907.185,
    "metric butt ton": 420000}

speed = {
    "m/s": 1,
    "km/s": 1e-3,
    "ft/s": 3.28084,
    "mph": 2.23694,
    "kph": 3.6,
    "kts": 0.514444,
    "knots": 0.514444}

force = {
    "N": 1,
    "lb": 0.224809,
    "lbs": 0.224809,
    "lbf": 0.224809}

pressure = {
    "Pa": 1,
    "psi":  0.000145038, 
    "bar": 1e-5,
    "lb/ft^2": 0.0208854}

density = {
    "kg/m^3": 1,
    "slug/ft^3": 0.00194032,
    "slugs/ft^3": 0.00194032}

angle = {
    "rad": 1,
    "deg": 180/3.141592653589793}

dimensions = [
    length,
    time,
    mass,
    speed,
    force,
    pressure,
    density]
    # temperature is handled separately

################################################################################
# FUNCTION
################################################################################

def convert(value, fromUnit, toUnit):
    """input the value and strings of the unit you want to convert from and to
    as entered in the conversion table above"""
    
    # handle all other units
    
    conversionFactors = [(d[fromUnit], d[toUnit]) for d in dimensions if fromUnit in d and toUnit in d]
    
    if len(conversionFactors) == 1: # found 1 conversion
        return value / conversionFactors[0][0] * conversionFactors[0][1]
    elif len(conversionFactors) == 0: # didn't find a conversion
        # handle temperature case
        if fromUnit in ["K", "R", "C", "F"] and toUnit in ["K", "R", "C", "F"]:
            if fromUnit == "K" and toUnit == "R":
                return value * (9/5)
            elif fromUnit == "K" and toUnit == "C":
                return value - 273.15
            elif fromUnit == "K" and toUnit == "F":
                return value * (9/5) - 459.67
            elif fromUnit == "R" and toUnit == "K":
                return value * (5/9)
            elif fromUnit == "R" and toUnit == "C":
                return (value - 491.67) * (5/9)
            elif fromUnit == "R" and toUnit == "F":
                return value - 459.67
            elif fromUnit == "C" and toUnit == "K":
                return value + 273.15
            elif fromUnit == "C" and toUnit == "R":
                return (value + 273.15) * (9/5)
            elif fromUnit == "C" and toUnit == "F":
                return value * (9/5) + 32
            elif fromUnit == "F" and toUnit == "K":
                return (value + 459.67) * (9/5)
            elif fromUnit == "F" and toUnit == "R":
                return value + 459.67
            elif fromUnit == "F" and toUnit == "C":
                return (value - 32) * (5/9)
        else:
            raise Exception("Could not find a suitable conversion factor in tables for {0} and {1}".format(fromUnit, toUnit))
    else: # len(conversionFactors) > 1: # found too many conversion factors
        raise Exception("Found multiple conversions for {0} and {1}".format(fromUnit, toUnit))
