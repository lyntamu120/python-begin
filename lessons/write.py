with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey there ninjas, python is awesome')

with open('files/write.txt', 'a') as write_file:
    write_file.write('\nI love it so much, I dream in python')

quotes = [
    '\nI love it so much, I dream in python',
    '\nI love it so much, I dream in python',
    '\nI love it so much, I dream in python'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
