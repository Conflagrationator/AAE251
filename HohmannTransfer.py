from scipy import *
import sys   
from Reference import*

def hohmann_transfer(delta ,h1, h2, r_earth, mu_earth ):
    r1 = h1 + r_earth    
    r2 = h2 + r_earth    
    delta = delta * pi/180
    at = (r1 + r2)/2    
    
    v_c1 = (mu_earth/r1)**.5
    energy = -mu_earth/(2*at)
    v_pt = (2 * (energy + (mu_earth / r1)))**.5    
    
    dV1 = v_pt - v_c1

    v_c2 = (mu_earth/r2)**.5
    v_at = (2 * (energy + (mu_earth / r2)))**.5

    dV2 = v_c2 - v_at
    
    dV = dV1 + dV2
    
    Period = 24*60*60
    r2 = (Period * (mu_earth**.5) / (2 * pi))**(2/3)
    at = (r1 + r2)/2    
    
    v_c1 = (mu_earth/r1)**.5
    energy = -mu_earth/(2*at)
    v_pt = (2 * (energy + (mu_earth / r1)))**.5    
    
    dV1 = v_pt - v_c1 #Geostationary TRANSFER Orbit

    
    v_c2 = (mu_earth/r2)**.5
    v_at = (2 * (energy + (mu_earth / r2)))**.5

    dV2 = ((v_at*cos(delta) - v_c2)**2 + (v_at - sin(delta))**2)**.5
    
    dV = dV1 + dV2

    return (dV*1000, v_at*1000)