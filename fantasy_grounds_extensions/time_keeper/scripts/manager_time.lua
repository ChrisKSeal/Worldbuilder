local minInHour = 60;
local hourInDay = 24;
local daysInYear = 365;
local leapYears = {}
leapYears[4] = 1
leapYears[100] = 0
leapYears[300] = 1
local worldTable = {}

function onInit()
	Debug.console('OnInit()')
	local minDB = DB.createChild('timekeeper.time.current', 'minute', 'number')
	local hourDB = DB.createChild('timekeeper.time.current', 'hour', 'number')
	local dayDB = DB.createChild('timekeeper.time.current', 'abs_day', 'number')
	current_mins = minDB.getValue(minDB, 0) 
	current_hours = minDB.getValue(hourDB, 0) 
	current_days = minDB.getValue(dayDB, 0) 
	for _, v in ipairs(Module.getModules()) do
		local info = Module.getModuleInfo(v)	
		Debug.console(info['name'])
		Debug.console(info['category'])
	end
	local oNode = DB.findNode('timekeeper.world.time')
	Debug.console(oNode)
	Debug.console(DB.getChildCategories('timekeeper.world.time'))
end

function select(nodeSource)
	for _,v in pairs(DB.getChildren("calendar.data")) do
		v.delete();
	end
	DB.copyNode(nodeSource, "calendar.data");
	DB.setValue("calendar.data.complete", "number", 1);
end

function addTimes(curTime, addTime)
	local addMins = addTime['mins'] or 0
	local addHours = addTime['hours'] or 0
	local addDays = addTime['days'] or 0
	--local mins =  + addMins
	--local hours = + addHours
	--local days = + addDays
	--while mins >= minInHour do
	--	hours = hours + 1
	--	mins = mins - minInHour
	--end
	--while hours >= hourInDay do
	--	days = days + 1
	--	hours = hours - hourInDay
	--end
	--local retab = {}
	--retab['mins'] = mins
	--retab['hours'] = hours
	--retab['days'] = days
	--return retab
end

function gcd( m, n )
    while n ~= 0 do
        local q = m
        m = n
        n = q % n
    end
    return m
end

function lcm( m, n )
    return ( m ~= 0 and n ~= 0 ) and m * n / gcd( m, n ) or 0
end

function getCycles(leapYears)
	local tkeys = {}
	for k,v in pairs(leapYears) do
		table.insert(tkeys, k)
	end
	table.sort(tkeys)
	local cycles = {}
	if #tkeys == 1 then
		for k,v in pairs(leapYears) do
			table.insert(cycles, k)
		end
	else
		local curCycle = nil
		for _, k in ipairs(tkeys) do
			if curCycle == nil then
				curCycle = k
			else
				curCycle = lcm(curCycle, k)
			end
			table.insert(cycles, curCycle)
		end
	end
	return cycles
end

function calcDaysPerCycle(leapYears, dayInYear)
	local cycles = getCycles(leapYears)
	local yearkeys = {}
	local cycleDays = {}
	for k,v in pairs(leapYears) do
		table.insert(yearkeys, k)
	end
	table.sort(yearkeys)
	for i = 1, #cycles do
		local totalAddDays = 0
		local prevAdd = 0
		for j = 1, i do
			local curAdd = leapYears[yearkeys[j]]
			local numberAdds = cycles[i] / yearkeys[j]
			if curAdd == 0 then
				totalAddDays = totalAddDays - numberAdds * prevAdd
			else
				totalAddDays = totalAddDays + numberAdds * curAdd
			end
			prevAdd = curAdd
		end
		table.insert(cycleDays, cycles[i]*daysInYear + totalAddDays)
	end
	return cycleDays
end

function getYear(days, leapYears, daysInYear)
	local cycleYears = getCycles(leapYears)
	local cycleDays = calcDaysPerCycle(leapYears, daysInYear)
	print(cycleDays[1])
	print(cycleDays[2])
	print(cycleDays[3])
	local yearkeys = {}
	for k, v in pairs(leapYears) do
		table.insert(yearkeys, k)
	end
	table.sort(yearkeys)
	local years = 0
	local remainingDays = days
	for i = #cycleDays, 1, -1 do
		cycles = math.floor(remainingDays/cycleDays[i])
		yearsInCycles = yearkeys[i]
		years = years + yearsInCycles * cycles
		remainingDays = remainingDays % cycleDays[i]
	end
	years = years + math.floor(remainingDays/daysInYear)
	remainingDays = remainingDays % daysInYear
	retab = {years, remainingDays}
	return retab
end

function addTurn(curTime)
	local turn = {}
	turn['mins'] = 10
	curTime = addTimes(curTime, turn)
end

function calc_mean_anomaly(day_in_angle)
	return day_in_angle
end

function calc_eccentric_anomaly(day_in_angle, world_table)
	local eccentricity = world_table['orbital_eccentricity']
	local M = calc_mean_anomaly(day_in_angle)

	local E = M

	repeat
		local LastE = E
		E = E + (M + eccentricity * math.sin(E) - E) / (1 - eccentricity * math.cos(E))
	until math.abs (E - LastE) < 0.0000000001

	E = E
	return E
end

function calc_true_anomaly(day_in_angle, world_table)
	local rad = math.rad
	local deg = math.deg
	local tan = function(r) return math.tan(r) end
	local atan = function(r) return math.atan(r) end
	local e = world_table['orbital_eccentricity']
	local E = calc_eccentric_anomaly(day_in_angle, world_table)
	if E == math.pi then
		return E
	elseif E > math.pi then
		return 2 * atan(math.sqrt((1+e)/(1-e))*(tan(E/2))) + 2 * math.pi
	else
		return 2 * atan(math.sqrt((1+e)/(1-e))*(tan(E/2)))
	end
end

print('Year: ' .. getYear(146097, leapYears, 365)[1])
print('Days: ' .. getYear(146097, leapYears, 365)[2])
