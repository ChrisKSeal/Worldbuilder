local temps={{low=-40,high=-20},{low=-30,high=-15},{low=-20,high=-5},{low=-10,high=0},{low=0,high=10},{low=10,high=18},{low=10,high=25},{low=15,high=30},{low=15,high=35},{low=20,high=40},{low=30,high=50},{low=40,high=60},{low=45,high=65},{low=50,high=70},{low=55,high=70},{low=55,high=75},{low=60,high=80},{low=65,high=80},{low=65,high=85},{low=70,high=85},{low=70,high=90},{low=75,high=90},{low=75,high=95},{low=80,high=100},{low=80,high=105},{low=85,high=115}}
local climates={ARCTIC={DESERT={{low=1, mid=2, high=7},{low=1, mid=2, high=8},{low=1, mid=3, high=8},{low=1, mid=5, high=8},{low=3, mid=7, high=11},{low=6, mid=10, high=12},{low=10, mid=11, high=14},{low=10, mid=11, high=13},{low=6, mid=8, high=11},{low=4, mid=7, high=10},{low=1, mid=4, high=8},{low=1, mid=2, high=8}},FOREST={{low=1, mid=2, high=7},{low=1, mid=2, high=8},{low=1, mid=3, high=8},{low=1, mid=5, high=8},{low=3, mid=7, high=11},{low=6, mid=10, high=12},{low=10, mid=11, high=14},{low=10, mid=11, high=13},{low=6, mid=8, high=11},{low=4, mid=7, high=10},{low=1, mid=4, high=8},{low=1, mid=2, high=8}},HILLS={{low=1, mid=2, high=5},{low=1, mid=2, high=4},{low=1, mid=3, high=6},{low=1, mid=4, high=7},{low=2, mid=5, high=9},{low=3, mid=6, high=9},{low=4, mid=7, high=12},{low=4, mid=7, high=11},{low=3, mid=6, high=10},{low=3, mid=5, high=8},{low=2, mid=5, high=8},{low=1, mid=3, high=5}},MOUNTAINS={{low=1, mid=2, high=5},{low=1, mid=2, high=4},{low=1, mid=3, high=6},{low=1, mid=4, high=7},{low=2, mid=5, high=9},{low=3, mid=6, high=9},{low=4, mid=7, high=12},{low=4, mid=7, high=11},{low=3, mid=6, high=10},{low=3, mid=5, high=8},{low=2, mid=5, high=8},{low=1, mid=3, high=5}},PLAINS={{low=1, mid=2, high=7},{low=1, mid=2, high=8},{low=1, mid=3, high=8},{low=1, mid=5, high=8},{low=3, mid=7, high=11},{low=6, mid=10, high=12},{low=10, mid=11, high=14},{low=10, mid=11, high=13},{low=6, mid=8, high=11},{low=4, mid=7, high=10},{low=1, mid=4, high=8},{low=1, mid=2, high=8}},SEACOAST={{low=1, mid=3, high=8},{low=1, mid=2, high=8},{low=1, mid=3, high=8},{low=1, mid=5, high=10},{low=3, mid=7, high=11},{low=6, mid=10, high=14},{low=10, mid=11, high=16},{low=10, mid=11, high=14},{low=5, mid=9, high=12},{low=3, mid=7, high=10},{low=1, mid=5, high=9},{low=1, mid=3, high=9}},SWAMP={{low=1, mid=2, high=7},{low=1, mid=2, high=8},{low=1, mid=3, high=8},{low=1, mid=5, high=8},{low=3, mid=7, high=11},{low=6, mid=10, high=12},{low=10, mid=11, high=14},{low=10, mid=11, high=13},{low=6, mid=8, high=11},{low=4, mid=7, high=10},{low=1, mid=4, high=8},{low=1, mid=2, high=8}}},SUBARCTIC={DESERT={{low=1, mid=4, high=9},{low=1, mid=4, high=10},{low=2, mid=5, high=10},{low=3, mid=7, high=10},{low=6, mid=11, high=13},{low=10, mid=12, high=14},{low=11, mid=13, high=17},{low=10, mid=13, high=17},{low=7, mid=11, high=17},{low=6, mid=8, high=13},{low=3, mid=5, high=12},{low=1, mid=3, high=9}},FOREST={{low=1, mid=5, high=10},{low=1, mid=5, high=9},{low=2, mid=7, high=11},{low=4, mid=10, high=12},{low=8, mid=11, high=14},{low=10, mid=12, high=16},{low=11, mid=13, high=18},{low=10, mid=13, high=18},{low=9, mid=11, high=16},{low=5, mid=10, high=11},{low=2, mid=8, high=11},{low=1, mid=6, high=10}},HILLS={{low=1, mid=4, high=9},{low=1, mid=4, high=9},{low=2, mid=6, high=10},{low=3, mid=7, high=10},{low=6, mid=11, high=14},{low=10, mid=12, high=14},{low=10, mid=13, high=16},{low=9, mid=13, high=16},{low=7, mid=11, high=13},{low=4, mid=10, high=12},{low=2, mid=7, high=11},{low=1, mid=4, high=10}},MOUNTAINS={{low=1, mid=3, high=9},{low=1, mid=4, high=9},{low=1, mid=6, high=10},{low=2, mid=8, high=12},{low=5, mid=10, high=13},{low=9, mid=11, high=13},{low=10, mid=12, high=14},{low=9, mid=13, high=15},{low=7, mid=11, high=13},{low=4, mid=10, high=12},{low=2, mid=6, high=11},{low=1, mid=4, high=10}},PLAINS={{low=1, mid=4, high=9},{low=1, mid=4, high=10},{low=2, mid=5, high=10},{low=3, mid=7, high=10},{low=6, mid=11, high=13},{low=10, mid=12, high=14},{low=11, mid=13, high=17},{low=10, mid=13, high=17},{low=7, mid=11, high=17},{low=6, mid=8, high=13},{low=3, mid=5, high=12},{low=1, mid=3, high=9}},SEACOAST={{low=2, mid=6, high=11},{low=2, mid=7, high=11},{low=3, mid=8, high=11},{low=4, mid=10, high=13},{low=8, mid=11, high=14},{low=10, mid=12, high=18},{low=11, mid=13, high=18},{low=11, mid=13, high=18},{low=10, mid=12, high=16},{low=5, mid=11, high=13},{low=3, mid=8, high=12},{low=1, mid=6, high=11}},SWAMP={{low=1, mid=4, high=9},{low=1, mid=4, high=10},{low=2, mid=5, high=10},{low=3, mid=7, high=10},{low=6, mid=11, high=13},{low=10, mid=12, high=14},{low=11, mid=13, high=17},{low=10, mid=13, high=17},{low=7, mid=11, high=17},{low=6, mid=8, high=13},{low=3, mid=5, high=12},{low=1, mid=3, high=9}}},TEMPERATE={DESERT={{low=11, mid=13, high=19},{low=11, mid=13, high=20},{low=12, mid=13, high=20},{low=13, mid=14, high=23},{low=13, mid=16, high=24},{low=16, mid=16, high=26},{low=21, mid=25, high=26},{low=21, mid=25, high=26},{low=17, mid=23, high=25},{low=14, mid=19, high=24},{low=12, mid=18, high=24},{low=11, mid=13, high=18}},FOREST={{low=3, mid=6, high=12},{low=2, mid=6, high=11},{low=5, mid=11, high=16},{low=8, mid=12, high=16},{low=11, mid=14, high=21},{low=13, mid=16, high=22},{low=13, mid=19, high=24},{low=13, mid=19, high=24},{low=12, mid=16, high=22},{low=10, mid=14, high=18},{low=6, mid=10, high=12},{low=4, mid=10, high=12}},HILLS={{low=2, mid=9, high=12},{low=3, mid=10, high=13},{low=5, mid=11, high=16},{low=9, mid=12, high=18},{low=10, mid=15, high=20},{low=10, mid=17, high=24},{low=12, mid=20, high=25},{low=12, mid=20, high=25},{low=11, mid=17, high=23},{low=10, mid=14, high=20},{low=6, mid=11, high=16},{low=3, mid=10, high=13}},MOUNTAINS={{low=1, mid=9, high=12},{low=2, mid=9, high=13},{low=3, mid=10, high=13},{low=5, mid=11, high=16},{low=6, mid=12, high=19},{low=11, mid=15, high=22},{low=12, mid=17, high=24},{low=11, mid=17, high=23},{low=9, mid=14, high=21},{low=5, mid=12, high=19},{low=3, mid=11, high=18},{low=2, mid=10, high=12}},PLAINS={{low=2, mid=8, high=13},{low=3, mid=8, high=14},{low=4, mid=11, high=17},{low=7, mid=12, high=19},{low=11, mid=14, high=21},{low=12, mid=16, high=24},{low=13, mid=19, high=25},{low=13, mid=19, high=25},{low=11, mid=16, high=23},{low=7, mid=12, high=19},{low=5, mid=11, high=17},{low=3, mid=10, high=13}},SEACOAST={{low=5, mid=10, high=13},{low=6, mid=11, high=14},{low=9, mid=11, high=17},{low=11, mid=12, high=19},{low=11, mid=13, high=20},{low=12, mid=15, high=23},{low=13, mid=16, high=24},{low=13, mid=16, high=23},{low=12, mid=15, high=23},{low=11, mid=12, high=20},{low=7, mid=11, high=16},{low=5, mid=11, high=13}},SWAMP={{low=2, mid=8, high=13},{low=3, mid=8, high=14},{low=4, mid=11, high=17},{low=7, mid=12, high=19},{low=11, mid=14, high=21},{low=12, mid=16, high=24},{low=13, mid=19, high=25},{low=13, mid=19, high=25},{low=11, mid=16, high=23},{low=7, mid=12, high=19},{low=5, mid=11, high=17},{low=3, mid=10, high=13}}},SUBTROPICAL={DESERT={{low=12, mid=16, high=20},{low=12, mid=16, high=21},{low=13, mid=19, high=23},{low=14, mid=20, high=24},{low=15, mid=20, high=24},{low=18, mid=22, high=25},{low=20, mid=24, high=26},{low=20, mid=24, high=26},{low=18, mid=21, high=25},{low=16, mid=21, high=25},{low=14, mid=19, high=24},{low=13, mid=16, high=23}},FOREST={{low=12, mid=20, high=21},{low=12, mid=20, high=22},{low=13, mid=20, high=22},{low=14, mid=20, high=23},{low=14, mid=20, high=24},{low=16, mid=21, high=24},{low=16, mid=21, high=24},{low=16, mid=21, high=24},{low=15, mid=21, high=23},{low=14, mid=21, high=23},{low=13, mid=19, high=22},{low=12, mid=19, high=22}},HILLS={{low=11, mid=14, high=17},{low=11, mid=15, high=18},{low=12, mid=17, high=21},{low=13, mid=19, high=22},{low=14, mid=20, high=23},{low=15, mid=21, high=24},{low=16, mid=21, high=24},{low=16, mid=21, high=25},{low=14, mid=19, high=24},{low=13, mid=17, high=22},{low=12, mid=16, high=19},{low=11, mid=14, high=18}},MOUNTAINS={{low=11, mid=13, high=16},{low=11, mid=13, high=17},{low=12, mid=16, high=19},{low=12, mid=16, high=20},{low=13, mid=17, high=21},{low=14, mid=17, high=21},{low=14, mid=16, high=20},{low=14, mid=15, high=18},{low=12, mid=15, high=18},{low=12, mid=14, high=17},{low=12, mid=14, high=17},{low=11, mid=13, high=16}},PLAINS={{low=12, mid=14, high=18},{low=11, mid=15, high=19},{low=13, mid=18, high=21},{low=14, mid=19, high=24},{low=18, mid=22, high=24},{low=19, mid=23, high=25},{low=20, mid=23, high=26},{low=20, mid=23, high=26},{low=19, mid=22, high=25},{low=17, mid=22, high=25},{low=13, mid=18, high=21},{low=12, mid=16, high=19}},SEACOAST={{low=12, mid=13, high=21},{low=11, mid=13, high=22},{low=11, mid=15, high=23},{low=12, mid=16, high=24},{low=13, mid=17, high=24},{low=13, mid=19, high=25},{low=14, mid=19, high=25},{low=14, mid=19, high=25},{low=13, mid=18, high=24},{low=12, mid=17, high=23},{low=11, mid=15, high=21},{low=11, mid=13, high=21}},SWAMP={{low=12, mid=14, high=18},{low=11, mid=15, high=19},{low=13, mid=18, high=21},{low=14, mid=19, high=24},{low=18, mid=22, high=24},{low=19, mid=23, high=25},{low=20, mid=23, high=26},{low=20, mid=23, high=26},{low=19, mid=22, high=25},{low=17, mid=22, high=25},{low=13, mid=18, high=21},{low=12, mid=16, high=19}}},TROPICAL={DESERT={{low=16, mid=18, high=21},{low=16, mid=19, high=20},{low=16, mid=20, high=23},{low=16, mid=21, high=24},{low=17, mid=22, high=24},{low=20, mid=23, high=26},{low=22, mid=25, high=26},{low=22, mid=25, high=26},{low=21, mid=24, high=25},{low=21, mid=22, high=24},{low=18, mid=21, high=23},{low=17, mid=19, high=22}},FOREST={{low=13, mid=21, high=23},{low=12, mid=21, high=23},{low=13, mid=21, high=23},{low=15, mid=21, high=24},{low=15, mid=21, high=24},{low=17, mid=21, high=24},{low=17, mid=21, high=24},{low=17, mid=21, high=24},{low=17, mid=21, high=24},{low=16, mid=21, high=24},{low=15, mid=21, high=23},{low=13, mid=21, high=23}},HILLS={{low=13, mid=16, high=18},{low=14, mid=16, high=20},{low=14, mid=18, high=20},{low=16, mid=18, high=21},{low=16, mid=20, high=24},{low=17, mid=21, high=25},{low=19, mid=23, high=26},{low=19, mid=23, high=26},{low=19, mid=22, high=25},{low=17, mid=20, high=23},{low=15, mid=18, high=21},{low=14, mid=17, high=20}},MOUNTAINS={{low=13, mid=16, high=18},{low=14, mid=16, high=19},{low=14, mid=17, high=20},{low=15, mid=17, high=20},{low=15, mid=17, high=21},{low=15, mid=17, high=21},{low=14, mid=16, high=20},{low=14, mid=16, high=20},{low=14, mid=16, high=20},{low=14, mid=16, high=19},{low=13, mid=16, high=19},{low=13, mid=16, high=19}},PLAINS={{low=13, mid=16, high=18},{low=14, mid=17, high=20},{low=14, mid=18, high=21},{low=16, mid=18, high=21},{low=18, mid=23, high=20},{low=20, mid=23, high=25},{low=20, mid=23, high=26},{low=20, mid=23, high=26},{low=20, mid=23, high=25},{low=18, mid=22, high=25},{low=16, mid=19, high=23},{low=14, mid=18, high=21}},SEACOAST={{low=16, mid=19, high=21},{low=16, mid=19, high=22},{low=15, mid=20, high=23},{low=17, mid=20, high=24},{low=17, mid=20, high=24},{low=18, mid=20, high=25},{low=18, mid=20, high=24},{low=18, mid=20, high=24},{low=18, mid=20, high=23},{low=17, mid=19, high=22},{low=17, mid=19, high=22},{low=16, mid=18, high=22}},SWAMP={{low=13, mid=16, high=18},{low=14, mid=17, high=20},{low=14, mid=18, high=21},{low=16, mid=18, high=21},{low=18, mid=23, high=20},{low=20, mid=23, high=25},{low=20, mid=23, high=26},{low=20, mid=23, high=26},{low=20, mid=23, high=25},{low=18, mid=22, high=25},{low=16, mid=19, high=23},{low=14, mid=18, high=21}}}}

function getClimateTab(climate)
if climate == 'ARCTIC' then
	return climates.ARCTIC
elseif climate =='SUBARCTIC' then
	return climates.SUBARCTIC
elseif climate == 'TROPICAL' then
	return climates.TROPICAL
elseif climate == 'SUBTROPICAL' then
	return climates.SUBTROPICAL
else
	return climates.TEMPERATE
end
end

function getBiomeTab(biome, climateTab)
if biome == 'DESERT' then
	return climateTab.DESERT
elseif biome == 'FOREST' then
return climateTab.FOREST
elseif biome == 'HILLS' then
return climateTab.HILLS
elseif biome == 'MOUNTAINS' then
return climateTab.MOUNTAINS
elseif biome == 'SEACOAST' then
return climateTab.SEACOAST
elseif biome == 'SWAMP'then
return climateTab.SWAMP
else
return climateTab.PLAINS
end
end

function getDayTemps(daydate, roll1, roll2, low, mid, high, PrvDay, PrvDayMax, PrvDayMin)
-- Define table of results
local day2day = {-3,-2,-2,-1,-1,0,1,1,2,2,3,}
-- Set default values if no previous day defined
PrvDay = PrvDay or mid
PrvDayMax = PrvDayMax or 0
PrvDayMin = PrvDayMin or 0
local sum = roll1 + roll2
sum = sum - PrvDayMax + PrvDayMin
if sum < 2 then
sum = 2
end
if sum > 12 then
sum = 12
end
local tempMod = day2day[sum-1]
local daytemp = PrvDay + tempMod
if daytemp <= low then
daytemp = low
todaylow = PrvDayMin + 1
todayhigh = 0
elseif daytemp >= high then
daytemp = high
todayhigh = PrvDayMax + 1
todaylow = 0
else
todayhigh = 0
todaylow = 0
end
day = {daydate, temps[daytemp].low, temps[daytemp].high, daytemp, todayhigh, todaylow}
return day
end

function getPrecipitation(daydate, roll1, roll2, prevDay)
	prevDay = prevDay or 0
	local rain = 0
	local sum = roll1 + roll2
	if sum == 7 then
		rain = prevDay
	elseif sum % 2 == 0 then
		rain = 1
	else
		rain = 0
	end

end

function getSpecialWeather()
end

function getWindChill()
end

function getHumidity()
end

function getWindSpeedAndDirection()
end

function getDaylightHours()
end

--function getBiomeSubTab(biome, climateTab)
print(getBiomeTab('HILLS',getClimateTab('ARCTIC'))[6].mid)
local tab = getBiomeTab('HILLS',getClimateTab('ARCTIC'))[6]
local roll1 = math.random(1,6)
local roll2 = math.random(1,6)
local dayold = getDayTemps(1, roll1, roll2, tab.low, tab.mid, tab.high)
print('Day: ' .. dayold[1] .. ', Low: ' .. dayold[2] .. ', High: ' .. dayold[3])
-- Not needed for FG
math.randomseed(os.clock()*100000000000)
for i=2,30 do
	roll1 = math.random(1,6)
	roll2 = math.random(1,6)
    local day = getDayTemps(i, roll1, roll2, tab.low, tab.mid, tab.high, dayold[4], dayold[5], dayold[6])
	print('Day: ' .. day[1] .. ', Low: ' .. day[2] .. ', High: ' .. day[3])
	print(day[4])
	print(day[5])
	print(day[6])
	dayold = day
end

