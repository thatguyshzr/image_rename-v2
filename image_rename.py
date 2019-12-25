# Rename jpg and jpeg in a folder

import os
try:
    path = input('Destination location: ')
    os.listdir(path)
    name = input('Name: ')
    x = 0

    for i in os.listdir(path):
        if i.endswith('.jpg') | i.endswith('jpeg'):
            os.rename('{}/{}'.format(path, i),
                      '{}/{}_{}.jpg'.format(path, name, x))
            x = x+1

    print(x, ' files renamed')

except FileNotFoundError:
    print('Invalid file location.')
