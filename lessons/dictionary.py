def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(dictionary.items())
        print(f'I am {key} and I am a {val} belt')

def belt_count(distionary):
    belts = list(distionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name: ')
    ninja_belt = input('enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another>(y/n)')
    if another == 'n':
        break





belt_count(ninja_belts)
