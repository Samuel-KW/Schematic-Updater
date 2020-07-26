import os

from os import system
from nbt.nbt import *

folder = 'Schematics/'
files = [f for f in os.listdir(folder) if os.path.isfile(folder + f)]

print('Schematic Fixed Upper\n')

print('Found ' + str(len(files)) + ' files(s) that will be parsed as schematics\n')

for f in files:

    if os.name == 'nt':
        system('title Current File: ' + f)

    try:
        data = NBTFile(folder + f)        

        if not 'TileEntities' in data:
            print('Missing NBT tags, fixing', f)

            data.tags.append(TAG_List(name='Entities', type=TAG_Long))
            data.tags.append(TAG_List(name='TileEntities', type=TAG_Long))
            data.write_file(folder + f)

        print('Parsed schematic file', f)
    except Exception as e:
        print(e)
        print('Unable to read file ', f)

print('\nDone.')
