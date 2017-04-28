from scipy import *
from Atmosphere import*
from AirplaneParameters import*

def CruiseSpeedCalc(altitude, mass, c, b):
    """
    altitude, or altitude of the airplane, should be given in m; test value is 18288 (60,000ft)
    mass, or weight of the airplane, should be given in kg; test value is 666780.24 (150,000pounds)
    c, or chord, should be given in m; test value is 2
    b, or span, should be given in m; test value is 20
    """
    #constants
    rho_infty = densityAtAltitude(altitude) #air density at altitude 'altitude'
    S = wingReferenceArea(c, b)
    Cl0 = liftCoefficientAtAngleOfAttack(0)
    weight = mass * g0 #in N

    #where is Lift equal to weight?
    V_cruise = sqrt(7/8*weight / (0.5 * Cl0 * rho_infty * S))
    return V_cruise