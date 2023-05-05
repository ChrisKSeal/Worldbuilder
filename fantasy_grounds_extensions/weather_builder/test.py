import helper as hlp
from weather import Location
import tables as tbl

world_conf = {'days_per_year': 360,
              'current_year': 20000}
latitude = 43
longitude = 89

loc = Location(latitude,
               longitude,
               world_conf)

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for month in months:
    month = str(month)
    roll_high = hlp.rollOE()
    roll_low = hlp.rollOE()
    print(roll_high)
    print(roll_low)
    print(loc.get_days_temps(month,
                         roll_high,
                         roll_low))








