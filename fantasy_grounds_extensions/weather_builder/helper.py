# -*- coding: utf-8 -*-
"""

@author: Chris
"""

import random

def d6():
	roll = random.randint(1,6)
	return roll

def rollOE():
    roll = random.randint(1,100)
    retval = roll
    while roll > 95:
        roll = random.randint(1,100)
        retval += roll
    return retval

def convertFtoC(F):
    return (F-32)*(5/9)

def get_seed(latitude,
            longitude):
    flg = True
    if latitude < 0:
        flg = not flg
    if longitude < 0:
        flg = not flg
    latstr = str(abs(int(round(latitude,0))))
    longstr = str(abs(int(round(longitude,0))))
    seedstr = longstr + latstr
    if flg:
        seed = int(seedstr)
    else:
        seed = -1*(int(seedstr))
    return seed

def lookup_dict(dictionary,
                roll):
    bounds = []
    for key in dictionary.keys():
        # Build list of low bounds and high bounds
        bounds.append(key)
    # Hard to imagine a case where the bounds are greater than -999 to +999 so user
    # these as hard limits
    if roll < -999:
        roll = -999
    if roll > 999:
        roll = 999
    bounds = sorted(bounds)
    for bound in bounds:
        low = bound[0]
        high = bound[1]
        if roll >= low and roll <= high:
            key = bound
            return dictionary[key]
    return False

def parse_tables(table_file='Tables.csv'):
        tables = {}
        table_flg = False
        roll_flg = False
        table_name = ''
        with open(table_file, 'r') as f:
                for line in f:
                        if line.startswith('TABLE:'):
                                data = line.split(',')
                                table_name = data[0][7:]
                                table_flg = True
                                tables[table_name] = {}
                        elif line.startswith('ROLLTABLE:'):
                                data = line.split(',')
                                table_name = data[0][11:]
                                roll_flg = True
                                tables[table_name] = {}
                        elif line.startswith('END'):
                                table_flg = False
                                roll_flg = False
                                table_name = ''
                        elif table_flg:
                                data = line.rstrip('\n').split(',')
                                key = data[0]
                                values = []
                                for datum in range(len(data)-1):
                                        index = datum+1
                                        value = data[index]
                                        if value == '':
                                                pass
                                        else:
                                                values.append(value)
                                tables[table_name][key] = values
                        elif roll_flg:
                                data = line.rstrip('\n').split(',')
                                key = (int(data[0]),int(data[1]))
                                values = []
                                for datum in range(len(data)-2):
                                        index = datum + 2
                                        value = data[index]
                                        if value == '':
                                                pass
                                        else:
                                                values.append(value)
                                tables[table_name][key] = values
        return tables
