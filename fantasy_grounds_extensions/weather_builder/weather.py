import constants as CONST
import helper as hlp
import tables as tbl
import random

class Location:
    def __init__(self,
                 latitude,
                 longitude,
                 world_conf,
                 base_terrain=CONST.PLAINS,
                 rain_shadow=False):
        self.days_per_year = world_conf['days_per_year']
        self.location_seed = hlp.get_seed(latitude,
                                          longitude)
        random.seed(self.location_seed)
        self.climate = self.get_climate_zone(latitude)
        self.temps = {}
        if self.climate == CONST.ARCTIC:
            print('Arctic')
            self.temps = tbl.tables['ClimateArctic']
        elif self.climate == CONST.SUBARCTIC:
            print('Subarctic')
            self.temps = tbl.tables['ClimateSubarctic']
        elif self.climate == CONST.TEMPERATE:
            print('Temperate')
            self.temps = tbl.tables['ClimateTemperate']
        elif self.climate == CONST.SUBTROPICAL:
            print('Subtropical')
            self.temps = tbl.tables['ClimateSubtropical']
        else:
            print('Tropical')
            self.temps = tbl.tables['ClimateTropical']
        self.base_terrain = base_terrain
        self.rain_shadow = rain_shadow
        self.current_year = world_conf['current_year']
        self.days = {}

    def get_climate_zone(self,
                       latitude):
        if abs(latitude) > 65.5:
            climate = CONST.ARCTIC
        elif abs(latitude) > 50.5:
            climate = CONST.SUBARCTIC
        elif abs(latitude) > 30.5:
            climate = CONST.TEMPERATE
        elif abs(latitude) > 15.5:
            climate = CONST.SUBTROPICAL
        else:
            climate = CONST.TROPICAL
        return climate

    def get_var_table(self,
                      varclass):
        if varclass == 1:
            return tbl.tables['VarClass1']
        elif varclass == 2:
            return tbl.tables['VarClass2']
        elif varclass == 3:
            return tbl.tables['VarClass3']
        elif varclass == 4:
            return tbl.tables['VarClass4']
        else:
            return tbl.tables['VarClass5']
    
    def get_days_temps(self,
                       month,
                       roll_high,
                       roll_low):
        max_avg, max_var, min_avg, min_var = self.temps[month]
        direction = hlp.d6()
        mod_tbl = self.get_var_table(int(max_var))
        mod_val = hlp.lookup_dict(mod_tbl,
                                  roll_high)[0]
        max_plus = 0
        if mod_val[-1] == '*':
            max_plus = 25
            if mod_val[-2] == '**':
                max_plus = 50
                if mod_val[-3] == '***':
                    max_plus = 75
        if max_plus == 25:
            mod_val = mod_val[:-1]
        elif max_plus == 50:
            mod_val = mod_val[:-2]
        elif max_plus == 75:
            mod_val = mod_val[:-3]
        max_tmp = int(max_avg) + int(mod_val)
        mod_tbl = self.get_var_table(int(min_var))
        mod_val = hlp.lookup_dict(mod_tbl,
                                  roll_low)[0]
        min_plus = 0
        if mod_val[-1] == '*':
            min_plus = 25
            if mod_val[-2] == '**':
                min_plus = 50
                if mod_val[-3] == '***':
                    min_plus = 75
        if min_plus == 25:
            mod_val = mod_val[:-1]
        elif min_plus == 50:
            mod_val = mod_val[:-2]
        elif min_plus == 75:
            mod_val = mod_val[:-3]
        min_tmp = int(min_avg) - int(mod_val)
        return (max_tmp, max_plus, min_tmp, min_plus)

class Day:

    def __init__(self):
        self.min_temp = 0
        self.max_temp = 0
        self.hours = {}
