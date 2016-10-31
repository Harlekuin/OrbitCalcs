import numpy
import scipy.constants
import astropy.constants
from astropy import units as u

GRAVITATIONAL_CONSTANT = G = astropy.constants.G
MASS_OF_EARTH = M = astropy.constants.M_earth

RADIUS_OF_EARTH = astropy.constants.R_earth

#details of a circular orbit
#AVERAGE_HEIGHT = 1.496e11 * u.meter + RADIUS_OF_EARTH.to('m')
#CURRENT_HEIGHT = 1 * u.meter + RADIUS_OF_EARTH.to('m')
CURRENT_HEIGHT = AVERAGE_HEIGHT = 8400 * u.kilometer


#V^2 = GM(2/r - 1/a)

V = ((G * M) * ((2/CURRENT_HEIGHT) - (1/AVERAGE_HEIGHT)))**.5

print(V.to('m/s'))


#delta v given by the Tsiolkovsky rocket equation
# dV = Exhaust Velocity * ln(total mass with fuel / total mass without fuel)
# i.e. 20% fuel with exhaust velocity of 2100 m/s
# dV = 2100 * ln(1/.8)m/s = 460 m/s
