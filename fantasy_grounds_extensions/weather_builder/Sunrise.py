import numpy as np
from matplotlib import pyplot as plt

axial_tilt = 23.44 # degrees for earth
axial_tilt_r = axial_tilt*(np.pi/180)
orbital_eccentricity = 0.167 # for earth
days_perihelion_after_winter_solstice = 12 # for earth
days_in_year = 365.24
length_of_day = 24 # hours for earth
planet_radius_m = 6371 * 1000 # 6,371 km earth in metres
planet_radius_ft = planet_radius_m * 3.28084
atmopheric_refraction = 0.6 # degrees

def calc_solar_declination(day_after_winter_solstice):
    eff_axial_tilt = np.sin(-axial_tilt_r)
    eff_orb_ecc = (2*np.pi/np.pi)* orbital_eccentricity * np.sin(((2*np.pi)/days_in_year)* (day_after_winter_solstice - days_perihelion_after_winter_solstice))
    eff_time = np.cos(((2*np.pi)/days_in_year)*day_after_winter_solstice)
    return np.arcsin(eff_axial_tilt * (eff_time + eff_orb_ecc))

def calc_sunrise_sunset(day_after_winter_solstice,
                        lattitude,
                        altitude = 0): # feet at sea-level
    lattitude_r = lattitude * (np.pi/180)
    angle_to_horizon_r = 0
    if altitude > 0:
        angle_to_horizon_r = np.arccos(planet_radius_ft/(planet_radius_ft + altitude))
        print('Angle:',angle_to_horizon_r)
    #eff_alt_sun = np.arctan(solar_radius_m/((planet_radius_m **2 + avg_orbital_distance_m **2)**0.5)) + atmopheric_refraction
    declination = calc_solar_declination(day_after_winter_solstice)
    print('Declination:',declination)
    #hour_angle = (np.sin(eff_alt_sun)-(np.sin(declination)*np.sin(lattitude_r)))/(np.cos(declination)*np.cos(lattitude_r))
    hour_angle = np.tan(declination)*np.tan(lattitude_r)
    #print((np.sin(eff_alt_sun)-(np.sin(declination)*np.sin(lattitude_r)))/(np.cos(declination)*np.cos(lattitude_r)))
    print(np.tan(declination)*np.tan(lattitude_r))
    if hour_angle < -1:
        hour_angle = -1
    elif hour_angle > 1:
        hour_angle = 1
    hour_angle_cos = np.arccos(hour_angle)
    hour_angle_cos += angle_to_horizon_r
    return (hour_angle_cos)

sun_dict = {}
days = []

for d in range(360):
    days.append(d)
    for l in [20,36.9,53.4,70]:
        if l not in sun_dict.keys():
            sun_dict[l] = []
        hour_a = calc_sunrise_sunset(d,l)
        hours = (length_of_day/(2*np.pi))*hour_a
        #sunrise = 12 - hours
        #sunset = 12 + hours
        sun_dict[l].append(2*hours)#(sunrise,sunset))

fig, ax = plt.subplots()
for l in [20,36.9,53.4,70]:
    ax.plot(days,
            sun_dict[l], marker = '.', ls = '', label=f'{l}')
ax.legend(loc=0)
plt.show()

