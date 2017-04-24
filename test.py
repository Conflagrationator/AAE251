import sys
from scipy import *

from Conversions import *
from Reference import *
from StandardAtmosphere import *
from RocketParameters import *
from Launch import *

################################################################################
# TESTING FUNCTION
################################################################################

def main():
    # put test code outputs & stuff here
    
################################################################################
# COMMAND LINE INTERFACE
################################################################################

if __name__ == "__main__":
    main(*[float(val) for val in sys.argv[1:]])
