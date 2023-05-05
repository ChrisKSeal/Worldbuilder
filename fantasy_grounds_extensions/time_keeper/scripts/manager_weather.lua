CONTINENTAL = 1
COASTAL = 2
DESERT = 3

function calc_perhelion_angle(solstice_offset, orbit_in_days)
	return (solstice_offset/orbit_in_days) * (2*math.pi)
end

function calculate_distance_to_sun_solstice(perihelion_angle, eccentricity)
	local a = 1
	local b = math.sqrt(1-(eccentricity)^2)
	local x = a*math.cos(perihelion_angle)
	local y = b*math.sin(perihelion_angle)
	local r = math.sqrt((x-eccentricity)^2+y^2)
	return r
end

function calculate_average_annual_temp(lattitude, perihelion_angle, eccentricity, avg_slope, avg_intercept, avg_equatorial_temp, solstice_flg)
	local hemisphere = 0
	if lattitude < 0 then
		hemisphere = -1
	else
		hemisphere = 1
	end
	local solar_distance = calculate_distance_to_sun_solstice(perihelion_angle, eccentricity)
	if solstice_flg == -1 then
		if lattitude < 0 then
			slope = avg_slope + (1-solar_distance) * 20/3
		else
			slope = avg_slope - (1-solar_distance) * 20/3
		end
	else
		if lattitude < 0 then
			slope = avg_slope - (1-solar_distance) * 20/3
		else
			slope = avg_slope + (1-solar_distance) * 20/3
		end
	end
	local avg_temp = avg_intercept - (hemisphere*lattitude) * (slope)
	if avg_temp > avg_equatorial_temp then
		avg_temp = avg_equatorial_temp
	end
	return avg_temp
end

function calculate_annual_temp_range(lattitude, downwind_distance_to_sea)
	local hemisphere
	if lattitude < 0 then
		hemisphere = -1
	else
		hemisphere = 1
	end
	return 0.13 * (lattitude*hemisphere) * downwind_distance_to_sea^(0.2)
end

function calculate_summer_winter_temps(lattitude, perihelion_angle, eccentricity, avg_slope, avg_intercept, avg_equatorial_temp, solstice_flg, downwind_distance_to_sea)
	local avg_temp = calculate_average_annual_temp(lattitude, perihelion_angle, eccentricity, avg_slope, avg_intercept, avg_equatorial_temp, solstice_flg)
	local annual_temp_range = calculate_annual_temp_range(lattitude, downwind_distance_to_sea)
	local temp_table = {}
	temp_table['high'] = avg_temp + (annual_temp_range/2)
	temp_table['low'] = avg_temp - (annual_temp_range/2)
	return temp_table
end

function calculate_daily_avg(day_since_solstice, season_lag, days_in_year, temp_table, lattitude, solstice_flg)
	local days = day_since_solstice - season_lag
	if days < 0 then
		days = days + days_in_year
	end
	local day_angle =  (days/days_in_year) * (2*math.pi)
	local hemisphere
	if lattitude < 0 then
		hemisphere = -1
	else
		hemisphere = 1
	end
	local offset = 0
	if hemisphere * solstice_flg == 1 then
		offset = math.pi
	end
	day_angle = day_angle + offset
	if day_angle > 2* math.pi then
		day_angle = day_angle - 2 * math.pi
	end
	local amplitude = (temp_table['high'] - temp_table['low'])/2
	local mean = (temp_table['high'] + temp_table['low'])/2
	return math.cos(day_angle) * amplitude + mean
end

function summer_daily_range(lattitude)
	return 12.34 - 3.8*math.cos(math.pi*lattitude/35)
end

function winter_daily_range(lattitude)
	local Rdw = 0
	if math.abs(lattitude) > 40 then
		Rdw = 12.8-0.114 * math.abs(lattitude)
	else
		Rdw = 14.31 - 3.41 * math.cos(math.pi*lattitude/20)
	end
	return Rdw
end

function calc_mean_daily_range(lattitude, season_lag, days_since_solstice, days_in_year, solstice_flg)
	local days = days_since_solstice - season_lag
	if days < 0 then
		days = days + days_in_year
	end
	local day_angle =  (days/days_in_year) * (2*math.pi)
	local hemisphere
	if lattitude < 0 then
		hemisphere = -1
	else
		hemisphere = 1
	end
	local offset = 0
	if hemisphere * solstice_flg == -1 then
		offset = math.pi
	end
	day_angle = day_angle + offset
	if day_angle > 2* math.pi then
		day_angle = day_angle - 2 * math.pi
	end
	local summer = summer_daily_range(lattitude)
	local winter = winter_daily_range(lattitude)
	local amplitude = (summer-winter)/2
	local mean = (summer+winter)/2
	return amplitude * math.cos(day_angle) + mean
end

function gaussian(mean, variance)
    return  math.sqrt(-2 * variance * math.log(math.random())) *
            math.cos(2 * math.pi * math.random()) + mean
end

function lognormal(mean, variance)
	return math.exp(gaussian(mean,variance))
end

function day_min_max(daily_avg, daily_range_avg, altitude, terrain)
	local mean = 0
	local variance = 0
	if terrain == DESERT then
		mean = 0.5
		variance = 0.35
	elseif terrain == COASTAL then
		mean = -0.25
		variance = 0.2
	else
		mean = -0.15
		variance = 0.1
	end
	local fraction = gaussian(0, 0.04)
	local daily_range = lognormal(mean, variance) * daily_range_avg
	local mean = daily_avg - (altitude/100)
	local temps_table = {}
	temps_table['min'] = mean - daily_range/2
	temps_table['max'] = mean + daily_range/2
	return temps_table
end


-- Define world properties
phys_world_properties = {}
phys_world_properties['orbit_in_days'] = 365.24255
phys_world_properties['solstice_offset_days'] = -10 --days relative to perihelion
phys_world_properties['solstice_type'] = 1 -- -1 = winter in southern hemispere, 1 = winter in northern hemisphere
phys_world_properties['hours_in_day'] = 24
phys_world_properties['mins_in_hour'] = 60
phys_world_properties['axial_tilt'] = math.rad(23.4) -- degrees
phys_world_properties['orbital_eccentricity'] = 0.016 -- 0 to 1
phys_world_properties['avg_equatorial_temp'] = 27 -- C
phys_world_properties['season_lag'] = 25 --days
phys_world_properties['perihelion_angle'] = calc_perhelion_angle(phys_world_properties['solstice_offset_days'],phys_world_properties['orbit_in_days'])
local lattitude = -40
local downwind_distance_to_sea = 1500
local avg_slope = 0.74
local avg_intercept = 40
local altitude = 100
local terrain = CONTINENTAL
for i=1,365, 10 do
	temps_table = calculate_summer_winter_temps(lattitude, phys_world_properties['perihelion_angle'], phys_world_properties['orbital_eccentricity'], avg_slope, avg_intercept, phys_world_properties['avg_equatorial_temp'], phys_world_properties['solstice_type'], downwind_distance_to_sea)
	daily_avg = calculate_daily_avg(i, phys_world_properties['season_lag'], phys_world_properties['orbit_in_days'], temps_table, lattitude, phys_world_properties['solstice_type'])
	daily_range = calc_mean_daily_range(lattitude, phys_world_properties['season_lag'], i, phys_world_properties['orbit_in_days'], phys_world_properties['solstice_type'])
	day_temps = day_min_max(daily_avg, daily_range, altitude, terrain)
	print('Day: ' .. i)
	print('Daily Avg: ' .. daily_avg)
	print('Daily range: ' .. daily_range)
	print('Min: ' .. day_temps['min'])
	print('Max: ' .. day_temps['max'])
end
