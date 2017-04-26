"""
Students can put comments in this main docstring. Such comments will be
 important for you (and your teammates in the group project) to remember
 what your definition block does.
"""
from scipy import *
import sys

def orbital_properties(a = 15000, e = 0.3, mu_earth = 3.986*10**5):
    """
    {'username':'cnilsen','assignment':'Conic Sections Intermediate Mastery','course':'spring-2017-aae-251','variables':
    {'a':'semi-major axis, km',
     'e':'orbital eccentricity, nondimensional',
     'rp':'periapsis radius, km',
     'vp':'periapsis velocity, km/s',
     'ra':'apoapsis radius, km',
     'va':'apoapsis velocity, km/s'}}
    """

    ########
    # Student's code and comments go here.
    ########
    
    rp = a*(1-e)
    ra = a*(1+e)
   
    
    energy = -mu_earth/(2*a)
    
    va = sqrt(2*(energy + (mu_earth/ra)))
    vp = sqrt(2*(energy + (mu_earth/rp)))
    return rp, vp, ra, va

# The following allows you to run the script directly from the command line
if __name__ == '__main__':
    orbital_properties(*[float(val) for val in sys.argv[1:]])
