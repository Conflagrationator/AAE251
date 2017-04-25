from scipy import *
from Reference import*
################################################################################
# ROCKET PARAMETER FUNCTIONS
################################################################################

def inert_mass(m_inert, m_prop): # inert mass fraction
    return m_inert / (m_inert + m_prop)

def inertMass(m_pay, dV, Isp, f_inert): # kg
    return (m_pay * f_inert * (exp(dV / (g0 * Isp)) - 1)) / (1 - f_inert * exp(dV / (g0 * Isp)))

def propellantMass(m_pay, dV, Isp): # kg
    return (m_pay * (exp(dV / (g0 * Isp)) - 1) * (1 - f_inert)) / (1 - f_inert * exp(dV / (g0 * Isp)))

def initialMass(m_pay, f_inert, dV, Isp): # kg
    return (m_pay * exp(dV / (g0 * Isp)) * (1 - f_inert)) / (1 - f_inert * exp(dV / (g0 * Isp)))

def rocketdV(mi, mf, Isp): # total ΔV rocket provides
    return -log(mf / mi) * g0 * Isp

