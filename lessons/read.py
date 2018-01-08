# test = open('files/test.txt')
#
# # for line in test:
# #     print(line.rstrip())
# #
# #
# # test.seek(0)
# #
# # lines = test.readlines()
# # print(lines)
#
# test.seek(50)
# file_text = test.read(100)
# print(file_text)
#
# test.close()

def sequence_filter(line):
    return '>' not in line

with open('files/test2.txt') as t2_file:
    lines = t2_file.readlines()
    print(list(filter(sequence_filter, lines)))
