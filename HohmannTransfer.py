from scipy import *
import sys   
from Reference import*

def HohmannTransfer(delta ,h1, h2, rEarth, muEarth, Calculate500):
    r1 = h1 + rEarth
    if (Calculate500 == True):
        #FOR 500km ORBIT
        r2 = h2 + rEarth    
        delta = delta * pi/180
        at = (r1 + r2)/2    
        
        v_c1 = (muEarth/r1)**.5
        energy = -muEarth/(2*at)
        v_pt = (2 * (energy + (muEarth / r1)))**.5    
        dV1 = v_pt - v_c1
    
        v_c2 = (muEarth/r2)**.5
        v_at = (2 * (energy + (muEarth / r2)))**.5
        dV2 = ((v_at*cos(delta) - v_c2)**2 + (v_at - sin(delta))**2)**.5
        
        dV = dV1 + dV2
    
    elif (Calculate500 == False):
        #FOR GEOSTATIONARY ORBIT
        Period = 24*60*60
        r2 = (Period * (muEarth**.5) / (2 * pi))**(2/3)
        at = (r1 + r2)/2    
        
        v_c1 = (muEarth/r1)**.5
        energy = -muEarth/(2*at)
        v_pt = (2 * (energy + (muEarth / r1)))**.5    
        dV1 = v_pt - v_c1 #Geostationary TRANSFER Orbit
    
        v_at = (2 * (energy + (muEarth / r2)))**.5
        dV2 = v_at*sin(delta/2)
        
        dV = dV1 + dV2

    return (dV, v_pt)

