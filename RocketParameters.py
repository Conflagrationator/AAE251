from scipy import *
from Reference import *

################################################################################
# Rocket Parameter Functions
################################################################################

def f_inert(inertMass, propellantMass): # inert mass fraction
    return inertMass / (inertMass + propellantMass)

def inertMass(payloadMass, dV, Isp, f_inert): # kg
    return (payloadMass * f_inert * (exp(dV / (g0 * Isp)) - 1))/(1 - f_inert * exp(dV / (g0 * Isp)))

def propellantMass(payloadMass, dV, Isp): # kg
    return (payloadMass * (exp(dV / (g0 * Isp) - 1) * (1 - f_inert)) / (1 - f_inert * exp(dV / (g0 * Isp))

def initialMass(payloadMass, f_inert, dV, Isp): # kg
    return ((payloadMass * exp(dV / (g0 * Isp)) * (1 - f_inert))/(1 - f_inert * exp(dV / (g0 * Isp))

def dV(initialMass, finalMass, Isp): # total ΔV rocket provides
    return -log(finalMass / initialMass) * g0 * Isp
