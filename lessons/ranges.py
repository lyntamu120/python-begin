# for n in range(5): # from 0 to 5 not inclusive
#     print(n)

# for n in range(0, 10, 3):
#     print(n)

burgers = ['beef', 'tuna', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])
