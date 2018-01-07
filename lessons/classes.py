from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 30000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has the mass of {naboo_mass} and the volume of {naboo_vol}')
