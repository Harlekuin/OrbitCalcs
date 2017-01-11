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
        Average_Height = Average_Height * u.meter
    
    V = ((G * M) * ((2/CURRENT_HEIGHT) - (1/AVERAGE_HEIGHT)))**.5
    return V.to('m/s')

def DeltaV(ExhaustVelocity, FuelMassperc): # returns delta v
    #delta v given by the Tsiolkovsky rocket equation
    # dV = Exhaust Velocity * ln(total mass with fuel / total mass without fuel)
    # i.e. 20% fuel with exhaust velocity of 2100 m/s
    # dV = 2100 * ln(1/.8)m/s = 460 m/s
    return ExhaustVelocity * np.log(1/(1 - FuelMassperc))
    

class CelestialBody(object):
    
    def __init__(self, name):
        self.name = name
        self.Mass = 0e0 * u.kg
        self.Equatorial_radius = 0e0 * u.meter
        self.surface_gravity = 0e0 * u.meter / u.second / u.second
        self.Solar_Day = 0e0 * u.second
        self.Standard_Gravitational_Parameter = 0e0 * u.meter * u.meter * u.meter / u.second / u.second    
    
    def InitiateValues(self, Mass, Equatorial_radius, surface_gravity, Solar_Day, Standard_Gravitational_Parameter):
        self.Mass = Mass * u.kg
        self.Equatorial_radius = Equatorial_radius * u.meter
        self.surface_gravity = surface_gravity * u.meter / u.second / u.second
        self.Solar_Day = Solar_Day * u.second
        self.Standard_Gravitational_Parameter = Standard_Gravitational_Parameter * u.meter * u.meter * u.meter / u.second / u.second

    def OrbitalVelocity(self, Current_Height, Average_Height):
        #V^2 = GM(2/r - 1/a)
        #if type(Current_Height) is float:
        #   Current_Height = Current_Height * u.meter + self.Equatorial_radius
        #if type(Average_Height) is float:
        #    Current_Height = Current_Height * u.meter + self.Equatorial_radius
        
        Current_Height = Current_Height + self.Equatorial_radius
        Average_Height = Average_Height + self.Equatorial_radius
        
        V = (self.Standard_Gravitational_Parameter * ((2/Current_Height) - (1/Average_Height)))**.5
        return V.to('m/s')
        
        
KSP_CelestialBodies = {}

KSP_CelestialBodies['Kerbin'] = CelestialBody('Kerbin')
KSP_CelestialBodies.get('Kerbin').InitiateValues(5.2897088e22, 6e5, 9.81, 2.16e8, 3.5303940e12)

print('SGP of Kerbin: %s' % KSP_CelestialBodies.get('Kerbin').Standard_Gravitational_Parameter)
print('OV at 1.2e5m circular orbit of Kerbin: %s' % KSP_CelestialBodies.get('Kerbin').OrbitalVelocity(1.2e5 * u.meter, 1.2e5 * u.meter))
print('OV at 7e4m circular orbit of Kerbin: %s' % KSP_CelestialBodies.get('Kerbin').OrbitalVelocity(7e4 * u.meter, 7e4 * u.meter))
exit()


        
CURRENT_HEIGHT = AVERAGE_HEIGHT = 160 * u.kilometer + RADIUS_OF_EARTH
print(OrbitalVelocity(CURRENT_HEIGHT, CURRENT_HEIGHT, M, G))

Exhaust_Velocity = 2100 * u.meter / u.second
Fuel_Mass_perc = .2
print(DeltaV(Exhaust_Velocity, Fuel_Mass_perc))
