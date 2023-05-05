--[[ Utility functions to handle conversion from years to days

gcd - calculate the greatest common denominator

lcm - calculate the least common multiple

getDaysInCurrentYear - function to check if the current year is a leap year and if so,
		how many days are in it.
		NB: This function assumes that the largest year block is the one that applies and overwrites the number of leap days.
		For complex systems of leap years, such as where a lower exception takes precedence over a larger one, the lcm of the two exceptions
		should be calculated and an additional set of leap year data added.

getAbsoluteSolarYear - function to accumulate drift in the calendar years due to fractional days in the solar year

getCycles - function to accumulate the total number of years/days in a complete repetition of leap years. This can be used to speed the calculation
		of days that have ever accumulated as a function of years

getDaysFromYears - function to calculate the total number of days that have ever accumulated at the start of the current year. Used as a marker
		to hook different calendars together.

getAbsoluteDayForCalendarNewYear - Winter Solstice in the Northern hemisphere in year 1 has been arbitrarily defined as day 1. Winter solstice was
		chosen as this simplifies the sunset/sunrise calculations.
		This provides an absolute reference point for calendars with different lengths and differing new years days.
--]]

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

function getAbsoluteSolarYear(absoluteDay, physWorldProps)
	local solarYear = physWorldProps['daysInYear'] or 365.24255
	return math.floor(absoluteDay/solarYear)
end

function getDaysInCurrentYear(calendarYear, calendarProps)
	local calDaysInYear = calendarProps['daysInYear'] or 365
	local calLeapYears = calendarProps['leapYears'] or nil
	if calLeapYears == nil then
		return calDaysInYear
	end
	local yearkeys = {}
	local curadds = 0
	for k, v in pairs(calLeapYears) do
		table.insert(yearkeys, k)
	end
	table.sort(yearkeys)
	for _, k in ipairs(yearkeys) do
		if calendarYear % k == 0 then
			curadds = calLeapYears[k]
		end
	end
	return calDaysInYear + curadds
end

function convertSolarDayToCalendarDay(solarDay, physWorldProps, calendarProps)
	local solarYear = solarDay['year'] or 1
	local curSolarDay = solarDay['day'] or 1 -- relative to winter solstice in Northern hemisphere
	local solarHour = solarDay['hour'] or 0 -- relative to winter solstice in Northern hemisphere
	local solarMin = solarDay['min'] or 0 -- relative to winter solstice in Northern hemisphere
	local lenSolarYear = physWorldProps['daysInYear'] or 365.24255
	local hoursInDay = physWorldProps['hoursInDay'] or 24
	local minsInHour = physWorldProps['minsInHour'] or 60
	local minsInDay = minsInHour * hoursInDay
	local calDaysInYear = calendarProps['daysInYear'] or 365
	local calLeapYears = calendarProps['leapYears'] or nil
	local calOffset = calendarProps['offset'] or nil
	local timeInMins = solarHour * hoursInDay + solarMin
	local fracTimeInMins = timeInMins/minsInDay
	local absoluteDay = solarYear * lenSolarYear + curSolarDay + fracTimeInMins
	local absoluteIntegerDay = math.floor(absoluteDay)
	local cycles = getCycles(calLeapYears)
	local cycleDays = calcDaysPerCycle(calLeapYears, calDaysInYear)
	local yearkeys = {}
	for _, k in ipairs(cycles) do
		table.insert(yearkeys, k)
	end
	table.sort(yearkeys)
	table.sort(cycleDays)
	local years = 0
	local remainingDays = absoluteIntegerDay
	for i = #cycleDays, 1, -1 do
		cycles = math.floor(remainingDays/cycleDays[i])
		yearsInCycles = yearkeys[i]
		years = years + yearsInCycles * cycles
		remainingDays = remainingDays % cycleDays[i]
	end
	years = years + math.floor(remainingDays/calDaysInYear)
	remainingDays = remainingDays % calDaysInYear
	local currentDay = remainingDays
	local fracDay = absoluteDay - absoluteIntegerDay
	local curMins = math.floor(fracDay*minsInDay)
	local curHours = math.floor(curMins/minsInHour)
	retab = {years, currentDay, curHours, (curMins-(curHours*minsInHour))}
	return retab
end

function convertCalendarTimeToSolar(calendarTime, physWorldProps, calendarProps)
	local calYear = calendarTime['year'] or 0
	local calDay = calendarTime['day'] or 0
	local calHour = calendarTime['hour'] or 0
	local calMin = calendarTime['min'] or 0
	local lenSolarYear = physWorldProps['daysInYear'] or 365.24255
	local hoursInDay = physWorldProps['hoursInDay'] or 24
	local minsInHour = physWorldProps['minsInHour'] or 60
	local minsInDay = minsInHour * hoursInDay
	local calDaysInYear = calendarProps['daysInYear'] or 365
	local calLeapYears = calendarProps['leapYears'] or nil
end

function getCycles(leapYears)
	local tkeys = {}
	for k, v in pairs(leapYears) do
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
	for k, v in pairs(cycles) do
	end
	return cycles
end

function calcDaysPerCycle(leapYears, daysInYear)
	local cycles = getCycles(leapYears)
	for i, k in pairs(cycles) do
	end
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

function convertCalendarDayToSolarDay(calendarDay, calendarProps, physWorldProps)

end


local solarYear = 365.24255
local leapYears = {}
leapYears[4] = 1
leapYears[100] = 0
leapYears[400] = 1
local calendarProps = {}
calendarProps['daysInYear'] = 360
calendarProps['leapYears'] = leapYears
local physWorldProps = {}
physWorldProps['daysInYear'] = 365.24255
physWorldProps['hoursInDay'] = 24
physWorldProps['minsInHour'] = 60
local solarDay = {}
solarDay['year'] = 2000
solarDay['day'] = 87
local curDate = convertSolarDayToCalendarDay(solarDay, physWorldProps, calendarProps)
for _, k in ipairs(curDate) do
	print(k)
end
