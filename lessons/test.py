from classes import Planet

naboo = Planet('Naboo', 30000, 8, 'Naboo System')
print(f'Name is {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(naboo.orbit())
print(Planet.spin('a very high speed'))
print(naboo.spin())
