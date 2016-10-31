import numpy
import scipy.constants
import astropy.constants

GRAVITATIONAL_CONSTANT = G = scipy.constants.G
MASS_OF_EARTH = M = astropy.constants.M_earth

print(G)
print(M)
print(M.to('kg'))

RADIUS_OF_EARTH = astropy.constants.R_earth
print(RADIUS_OF_EARTH)

#details of a circular orbit
orbit_km = 200
total_height = orbit_km + RADIUS_OF_EARTH.to('km')

#V^2 = GM(2/r - 1/a)
r = total_height