local rad = math.rad
local deg = math.deg
local floor = math.floor
local frac = function(n) return n - floor(n) end
local cos = function(r) return math.cos(r) end
local acos = function(r) return math.acos(r) end
local sin = function(r) return math.sin(r) end
local asin = function(r) return math.asin(r) end
local tan = function(r) return math.tan(r) end
local atan = function(r) return math.atan(r) end
local pi = math.pi
local nint = function(n) return floor(n+0.5) end

function adjust_angle(angle)
	local abs_magnitude = math.abs(angle)
	local adjusted = angle
	if abs_magnitude > 2 * pi then
		adjusted = abs_magnitude % (2*pi)
	end
	if angle < 0 then
		adjusted = - adjusted
	end
	return adjusted
end

function calc_solstice_offset_angle(world_table)
	local offset_days = world_table['solstice_offset_days']
	local mean_angular_velocity = (2*pi) / world_table['orbit_in_days']
	return offset_days * mean_angular_velocity
end

function equation_of_time(day_in_angle, world_table)
	local solstice_offset = calc_solstice_offset_angle(world_table)
	-- define A relative to the solstice, where A is the angle subtended by the current day and the solstice
	local A = adjust_angle(day_in_angle - solstice_offset)
	local B = A + (2 * world_table['orbital_eccentricity'] * sin(day_in_angle))
	local C = (A - atan((tan(B))/(cos(world_table['axial_tilt']))))/pi
	local EoT = 720 * (C - nint(C))
	return EoT
end

function calc_declination(day_in_angle, world_table)
	local solstice_offset = calc_solstice_offset_angle(world_table)
	-- define A relative to the solstice, where A is the angle subtended by the current day and the solstice
	local A = adjust_angle(day_in_angle - solstice_offset)
	local B = A + (2 * world_table['orbital_eccentricity'] * sin(day_in_angle))
	local declination = asin(sin(-1 * world_table['axial_tilt'])*cos(B))
	return declination
end

function calc_sunrise_sunset(lattitude, longitude, altitude, day_in_angle, world_table)
	local pos = lattitude or 0
	local alt = altitude or 0
	local long = longitude or 0
	local refraction = rad(-0.83)
	local angle_to_horizon = 0
	if alt > 0 then
		angle_to_horizon = acos(world_table['planet_radius']/(world_table['planet_radius'] + alt))
	end
	local declination = calc_declination(day_in_angle, world_table)
	refraction = refraction - angle_to_horizon
	local hour_angle = (sin(refraction)-(sin(pos)*sin(declination)))/(cos(pos)*cos(declination))
	if hour_angle < -1 then hour_angle = -1 end
	if hour_angle > 1 then hour_angle = 1 end
	if long == -pi then long = pi end
	hour_angle = acos(hour_angle)
	local retab = {}
	retab['hour_angle'] = hour_angle
	local half_day = (hour_angle/(2*pi)) * world_table['hours_in_day']
	if half_day == 12 then
		retab['sunrise'] = 0
		retab['sunset'] = 0
		retab['clock_sunrise'] = retab['sunrise']
		retab['clock_sunset'] = retab['sunset']
	elseif half_day == 0 then
		retab['sunrise'] = -1
		retab['sunset'] = -1
		retab['clock_sunrise'] = retab['sunrise']
		retab['clock_sunset'] = retab['sunset']
	else
		local noon_offset = equation_of_time(day_in_angle, world_table)
		if long ~= 0 then
			noon_offset = noon_offset + ((world_table['hours_in_day'] * world_table['mins_in_hour'])/(2*pi)) * long
		end
		local noon = floor(convert_hours_to_mins(world_table['hours_in_day'], world_table)/2)
		local half_day_mins = convert_hours_to_mins(half_day, world_table)
		retab['sunrise'] = noon - half_day_mins
		retab['sunset'] = noon + half_day_mins
		retab['clock_sunrise'] = retab['sunrise'] + noon_offset
		retab['clock_sunset'] = retab['sunset'] + noon_offset
	end
	return retab
end

function convert_mins_to_hours_mins(mins, world_table)
	local retab = {}
	mins = floor(mins+0.5)
	retab['hours'] = floor(mins/world_table['mins_in_hour'])
	retab['mins'] = mins % world_table['mins_in_hour']
	return retab
end

function convert_hours_to_hours_mins(hours, world_table)
	local mins = convert_hours_to_mins(hours, world_table)
	local retab = convert_mins_to_hours_mins(mins, world_table)
	return retab
end

function convert_hours_to_mins(hours, world_table)
	return floor((hours * world_table['mins_in_hour']) + 0.5)
end

-- Define world properties
phys_world_properties = {}
phys_world_properties['orbit_in_days'] = 365.24255
phys_world_properties['solstice_offset_days'] = -10 --days relative to perihelion
phys_world_properties['solstice_type'] = 1 -- -1 = winter in southern hemispere, 1 = winter in northern hemisphere
phys_world_properties['hours_in_day'] = 24
phys_world_properties['mins_in_hour'] = 60
phys_world_properties['axial_tilt'] = rad(23.4) -- degrees
phys_world_properties['orbital_eccentricity'] = 0.016 -- 0 to 1
phys_world_properties['planet_radius'] = 6371 * 1000 -- m

day_in_angle = rad(10*(360/365))
lattitude = rad(-40)
longitude = rad(174)
for k, v in pairs(calc_sunrise_sunset(lattitude, longitude, altitude, day_in_angle, phys_world_properties)) do
	print(k .. ': ' .. v)
	if k ~= 'hour_angle' then
		local timetab = convert_mins_to_hours_mins(v, phys_world_properties)
		print(k .. ': ' .. timetab['hours'] ..':' .. timetab['mins'])
	end
end
