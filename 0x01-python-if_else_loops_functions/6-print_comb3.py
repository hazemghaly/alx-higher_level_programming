#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a + 1, 10):
        if a != b and str(a) + str(b) != '89' : 
            print('{}{}'.format(a, b), end=", ")
print('98')
