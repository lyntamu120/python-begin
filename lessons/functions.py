def area(radius):
    return 3.14 * radius * radius

def vol(area, length):
    print(area * length)

radius = input('enter a radius: ')
length = input('enter a length: ')

radius = int(radius)
length = int(length)

area_calc = area(radius)
vol(area_calc, length)
