import numpy as np
import scipy.constants
import astropy.constants
from astropy import units as u

GRAVITATIONAL_CONSTANT = G = astropy.constants.G
MASS_OF_EARTH = M = astropy.constants.M_earth

RADIUS_OF_EARTH = astropy.constants.R_earth

def OrbitalVelocity(Current_Height, Average_Height, M, G): #returns orbital velocity of a given orbit
    #V^2 = GM(2/r - 1/a)
    if type(Current_Height) is float:
        Current_Height = Current_Height * u.meter
    if type(Average_Height) is float:
        Current_Height = Current_Height * u.meter
    
    V = ((G * M) * ((2/CURRENT_HEIGHT) - (1/AVERAGE_HEIGHT)))**.5
    return V.to('m/s')

def DeltaV(ExhaustVelocity, FuelMassperc): # returns delta v
    #delta v given by the Tsiolkovsky rocket equation
    # dV = Exhaust Velocity * ln(total mass with fuel / total mass without fuel)
    # i.e. 20% fuel with exhaust velocity of 2100 m/s
    # dV = 2100 * ln(1/.8)m/s = 460 m/s
    return ExhaustVelocity * np.log(1/(1 - FuelMassperc))
    

    
CURRENT_HEIGHT = AVERAGE_HEIGHT = 160 * u.kilometer + RADIUS_OF_EARTH
print(OrbitalVelocity(CURRENT_HEIGHT, CURRENT_HEIGHT, M, G))

Exhaust_Velocity = 2100 * u.meter / u.second
Fuel_Mass_perc = .2
print(DeltaV(Exhaust_Velocity, Fuel_Mass_perc))
