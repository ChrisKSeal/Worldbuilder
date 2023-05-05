A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25


DESERT, FOREST, HILLS, MOUNTAINS, PLAINS, SEACOAST, SWAMP = 0, 1, 2, 3, 4, 5, 6
YES,NO,SAME = 1,2,3
NONE, LGTSNOW, SNOW, HVYSNOW, LTSLEET, SLEET, HVYSLEET, DRIZZLE, RAIN, HVYRAIN, TROPSTORM, MONSOON = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
SHORT, MEDIUM, LONG = 1,2,3
LIGHT, HEAVY, PROLONGED, STORM = 1, 2, 3, 4
ARCTIC, SUBARCTIC, TEMPERATE, SUBTROPICAL, TROPICAL = 0, 1, 2, 3, 4

Temps = {}
Temps[A] = (-20, -40)
Temps[B] = (-15, -30)
Temps[C] = (-5, -20)
Temps[D] = (0, -10)
Temps[E] = (10, 0)
Temps[F] = (18, 10)
Temps[G] = (25, 10)
Temps[H] = (30, 15)
Temps[I] = (35, 15)
Temps[J] = (40, 20)
Temps[K] = (50, 30)
Temps[L] = (60, 40)
Temps[M] = (65, 45)
Temps[N] = (70, 50)
Temps[O] = (70, 55)
Temps[P] = (75, 55)
Temps[Q] = (80, 60)
Temps[R] = (80, 65)
Temps[S] = (85, 65)
Temps[T] = (85, 70)
Temps[U] = (90, 70)
Temps[V] = (90, 75)
Temps[W] = (95, 75)
Temps[X] = (100, 80)
Temps[Y] = (105, 80)
Temps[Z] = (115, 85)

Climate = {}
Climate[ARCTIC] = {}
Climate[SUBARCTIC] = {}
Climate[TEMPERATE] = {}
Climate[SUBTROPICAL] = {}
Climate[TROPICAL] = {}
Climate[ARCTIC][DESERT]=[(A,B,G),(A,B,H),(A,C,H),(A,E,H),(C,G,K),(F,J,L),(J,K,N),(J,K,M),(F,H,K),(D,G,J),(A,D,H),(A,B,H)]
Climate[ARCTIC][HILLS]=[(A,B,E),(A,B,D),(A,C,F),(A,D,G),(B,E,I),(C,F,I),(D,G,L),(D,G,K),(C,F,J),(C,E,H),(B,E,H),(A,C,E)]
Climate[ARCTIC][MOUNTAINS]=[(A,B,E),(A,B,D),(A,C,F),(A,D,G),(B,E,I),(C,F,I),(D,G,L),(D,G,K),(C,F,J),(C,E,H),(B,E,H),(A,C,E)]
Climate[ARCTIC][PLAINS]=[(A,B,G),(A,B,H),(A,C,H),(A,E,H),(C,G,K),(F,J,L),(J,K,N),(J,K,M),(F,H,K),(D,G,J),(A,D,H),(A,B,H)]
Climate[ARCTIC][SEACOAST]=[(A,C,H),(A,B,H),(A,C,H),(A,E,J),(C,G,K),(F,J,N),(J,K,P),(J,K,N),(E,I,L),(C,G,J),(A,E,I),(A,C,I)]
Climate[ARCTIC][FOREST] = Climate[ARCTIC][PLAINS]
Climate[ARCTIC][SWAMP] = Climate[ARCTIC][PLAINS]
Climate[SUBARCTIC][DESERT]=[(A,D,I),(A,D,J),(B,E,J),(C,G,J),(F,K,M),(J,L,N),(K,M,Q),(J,M,Q),(G,K,Q),(F,H,M),(C,E,L),(A,C,I)]
Climate[SUBARCTIC][FOREST]=[(A,E,J),(A,E,I),(B,G,K),(D,J,L),(H,K,N),(J,L,P),(K,M,R),(J,M,R),(I,K,P),(E,J,K),(B,H,K),(A,F,J)]
Climate[SUBARCTIC][HILLS]=[(A,D,I),(A,D,I),(B,F,J),(C,G,J),(F,K,N),(J,L,N),(J,M,P),(I,M,P),(G,K,M),(D,J,L),(B,G,K),(A,D,J)]
Climate[SUBARCTIC][MOUNTAINS]=[(A,C,I),(A,D,I),(A,F,J),(B,H,L),(E,J,M),(I,K,M),(J,L,N),(I,M,O),(G,K,M),(D,J,L),(B,F,K),(A,D,J)]
Climate[SUBARCTIC][PLAINS]=[(A,D,I),(A,D,J),(B,E,J),(C,G,J),(F,K,M),(J,L,N),(K,M,Q),(J,M,Q),(G,K,Q),(F,H,M),(C,E,L),(A,C,I)]
Climate[SUBARCTIC][SEACOAST]=[(B,F,K),(B,G,K),(C,H,K),(D,J,M),(H,K,N),(J,L,R),(K,M,R),(K,M,R),(J,L,P),(E,K,M),(C,H,L),(A,F,K)]
Climate[SUBARCTIC][SWAMP] = Climate[SUBARCTIC][PLAINS]
Climate[TEMPERATE][DESERT]=[(K,M,S),(K,M,T),(L,M,T),(M,N,W),(M,P,X),(P,P,Z),(U,Y,Z),(U,Y,Z),(Q,W,Y),(N,S,X),(L,R,X),(K,M,R)]
Climate[TEMPERATE][FOREST]=[(C,F,L),(B,F,K),(E,K,P),(H,L,P),(K,N,U),(M,P,V),(M,S,X),(M,S,X),(L,P,V),(J,N,R),(F,J,L),(D,J,L)]
Climate[TEMPERATE][HILLS]=[(B,I,L),(C,J,M),(E,K,P),(I,L,R),(J,O,T),(J,Q,X),(L,T,Y),(L,T,Y),(K,Q,W),(J,N,T),(F,K,P),(C,J,M)]
Climate[TEMPERATE][MOUNTAINS]=[(A,I,L),(B,I,M),(C,J,M),(E,K,P),(F,L,S),(K,O,V),(L,Q,X),(K,Q,W),(I,N,U),(E,L,S),(C,K,R),(B,J,L)]
Climate[TEMPERATE][PLAINS]=[(B,H,M),(C,H,N),(D,K,Q),(G,L,S),(K,N,U),(L,P,X),(M,S,Y),(M,S,Y),(K,P,W),(G,L,S),(E,K,Q),(C,J,M)]
Climate[TEMPERATE][SEACOAST]=[(E,J,M),(F,K,N),(I,K,Q),(K,L,S),(K,M,T),(L,O,W),(M,P,X),(M,P,W),(L,O,W),(K,L,T),(G,K,P),(E,K,M)]
Climate[TEMPERATE][SWAMP] = Climate[TEMPERATE][PLAINS]
Climate[SUBTROPICAL][DESERT]=[(L,P,T),(L,P,U),(M,S,W),(N,T,X),(O,T,X),(R,V,Y),(T,X,Z),(T,X,Z),(R,U,Y),(P,U,Y),(N,S,X),(M,P,W)]
Climate[SUBTROPICAL][FOREST]=[(L,T,U),(L,T,V),(M,T,V),(N,T,W),(N,T,X),(P,U,X),(P,U,X),(P,U,X),(O,U,W),(N,U,W),(M,S,V),(L,S,V)]
Climate[SUBTROPICAL][HILLS]=[(K,N,Q),(K,O,R),(L,Q,U),(M,S,V),(N,T,W),(O,U,X),(P,U,X),(P,U,Y),(N,S,X),(M,Q,V),(L,P,S),(K,N,R)]
Climate[SUBTROPICAL][MOUNTAINS]=[(K,M,P),(K,M,Q),(L,P,S),(L,P,T),(M,Q,U),(N,Q,U),(N,P,T),(N,O,R),(L,O,R),(L,N,Q),(L,N,Q),(K,M,P)]
Climate[SUBTROPICAL][PLAINS]=[(L,N,R),(K,O,S),(M,R,U),(N,S,X),(R,V,X),(S,W,Y),(T,W,Z),(T,W,Z),(S,V,Y),(Q,V,Y),(M,R,U),(L,P,S)]
Climate[SUBTROPICAL][SEACOAST]=[(L,M,U),(K,M,V),(K,O,W),(L,P,X),(M,Q,X),(M,S,Y),(N,S,Y),(N,S,Y),(M,R,X),(L,Q,W),(K,O,U),(K,M,U)]
Climate[SUBTROPICAL][SWAMP] = Climate[SUBTROPICAL][PLAINS]
Climate[TROPICAL][DESERT]=[(P,R,U),(P,S,T),(P,T,W),(P,U,X),(Q,V,X),(T,W,Z),(V,Y,Z),(V,Y,Z),(U,X,Y),(U,V,X),(R,U,W),(Q,S,V)]
Climate[TROPICAL][FOREST]=[(M,U,W),(L,U,W),(M,U,W),(O,U,X),(O,U,X),(Q,U,X),(Q,U,X),(Q,U,X),(Q,U,X),(P,U,X),(O,U,W),(M,U,W)]
Climate[TROPICAL][HILLS]=[(M,P,R),(N,P,T),(N,R,T),(P,R,U),(P,T,X),(Q,U,Y),(S,W,Z),(S,W,Z),(S,V,Y),(Q,T,W),(O,R,U),(N,Q,T)]
Climate[TROPICAL][MOUNTAINS]=[(M,P,R),(N,P,S),(N,Q,T),(O,Q,T),(O,Q,U),(O,Q,U),(N,P,T),(N,P,T),(N,P,T),(N,P,S),(M,P,S),(M,P,S)]
Climate[TROPICAL][PLAINS]=[(M,P,R),(N,Q,T),(N,R,U),(P,R,U),(R,W,T),(T,W,Y),(T,W,Z),(T,W,Z),(T,W,Y),(R,V,Y),(P,S,W),(N,R,U)]
Climate[TROPICAL][SEACOAST]=[(P,S,U),(P,S,V),(O,T,W),(Q,T,X),(Q,T,X),(R,T,Y),(R,T,X),(R,T,X),(R,T,W),(Q,S,V),(Q,S,V),(P,R,V)]
Climate[TROPICAL][SWAMP] = Climate[TROPICAL][PLAINS]

Precipitation = {}
Precipitation[ARCTIC] = {}
Precipitation[SUBARCTIC] = {}
Precipitation[TEMPERATE] = {}
Precipitation[SUBTROPICAL] = {}
Precipitation[TROPICAL] = {}
Precipitation[ARCTIC][DESERT]=[(0,T,0),(0,T,0),(0,T,0),(0,T,0)]
Precipitation[ARCTIC][HILLS]=[(0,0,T),(0,0,T),(0,0,T),(0,0,T)]
Precipitation[ARCTIC][MOUNTAINS]=[(0,0,T),(0,0,T),(0,0,T),(0,0,T)]
Precipitation[ARCTIC][PLAINS]=[(0,T,T),(0,L,T),(0,M,L),(0,T,T)]
Precipitation[ARCTIC][SEACOAST]=[(0,T,0),(0,L,T),(0,L,T),(0,L,T)]
Precipitation[SUBARCTIC][DESERT]=[(0,T,0),(0,0,T),(0,0,T),(0,T,0)]
Precipitation[SUBARCTIC][FOREST]=[(0,L,T),(T,M,L),(T,M,L),(T,L,T)]
Precipitation[SUBARCTIC][HILLS]=[(0,T,T),(0,L,T),(T,L,L),(0,L,T)]
Precipitation[SUBARCTIC][MOUNTAINS]=[(0,T,T),(T,M,L),(T,L,T),(0,L,T)]
Precipitation[SUBARCTIC][PLAINS]=[(0,L,T),(T,M,L),(T,M,L),(T,L,T)]
Precipitation[SUBARCTIC][SEACOAST]=[(0,T,T),(0,L,T),(T,M,L),(0,L,T)]
Precipitation[SUBARCTIC][SWAMP]=[(0,L,T),(T,M,L),(T,L,L),(T,L,L)]
Precipitation[TEMPERATE][DESERT]=[(0,T,0),(0,T,0),(0,T,0),(0,0,0)]
Precipitation[TEMPERATE][FOREST]=[(T,M,L),(L,H,M),(L,M,M),(L,M,M)]
Precipitation[TEMPERATE][HILLS]=[(T,M,L),(L,H,M),(L,H,M),(T,M,L)]
Precipitation[TEMPERATE][MOUNTAINS]=[(0,M,L),(0,M,L),(0,L,T),(0,M,L)]
Precipitation[TEMPERATE][PLAINS]=[(0,L,T),(L,H,M),(L,H,M),(T,M,L)]
Precipitation[TEMPERATE][SEACOAST]=[(L,H,M),(T,M,L),(0,L,T),(L,H,M)]
Precipitation[TEMPERATE][SWAMP]=[(T,M,L),(L,H,L),(L,H,M),(0,M,L)]
Precipitation[SUBTROPICAL][DESERT]=[(0,T,0),(0,T,0),(0,0,0),(0,T,0)]
Precipitation[SUBTROPICAL][FOREST]=[(M,H,H),(M,D,H),(M,D,H),(M,H,H)]
Precipitation[SUBTROPICAL][HILLS]=[(T,L,L),(L,H,M),(L,H,M),(T,M,L)]
Precipitation[SUBTROPICAL][MOUNTAINS]=[(T,M,L),(L,H,M),(L,M,M),(T,M,L)]
Precipitation[SUBTROPICAL][PLAINS]=[(0,L,T),(T,H,L),(T,M,L),(0,L,T)]
Precipitation[SUBTROPICAL][SEACOAST]=[(T,M,L),(L,H,M),(L,D,M),(0,L,T)]
Precipitation[SUBTROPICAL][SWAMP]=[(T,L,L),(T,M,L),(T,H,L),(T,L,L)]
Precipitation[TROPICAL][DESERT]=[(0,T,0),(0,L,T),(0,T,0),(0,T,0)]
Precipitation[TROPICAL][FOREST]=[(M,D,H),(M,D,H),(M,D,H),(M,D,H)]
Precipitation[TROPICAL][HILLS]=[(0,T,0),(0,L,T),(T,M,L),(0,T,0)]
Precipitation[TROPICAL][MOUNTAINS]=[(T,M,L),(M,H,H),(T,M,L),(M,H,H)]
Precipitation[TROPICAL][PLAINS]=[(0,T,0),(L,H,M),(M,H,M),(L,H,M)]
Precipitation[TROPICAL][SEACOAST]=[(0,T,0),(L,D,M),(H,D,D),(0,L,T)]
Precipitation[TROPICAL][SWAMP]=[(0,L,T),(M,H,H),(M,H,M),(L,M,M)]

Special = {}
Special[ARCTIC] = {}
Special[SUBARCTIC] = {}
Special[TEMPERATE] = {}
Special[SUBTROPICAL] = {}
Special[TROPICAL] = {}
Special[ARCTIC][DESERT]=[(G,A,D,D),(G,A,D,D),(G,A,D,D),(G,A,D,D)]
Special[ARCTIC][HILLS]=[(G,A,D,D),(G,A,D,M),(G,A,D,Z),(G,A,D,D)]
Special[ARCTIC][MOUNTAINS]=[(G,A,D,D),(G,A,D,M),(G,A,M,Z),(G,A,D,M)]
Special[ARCTIC][PLAINS]=[(G,A,D,D),(A,G,D,M),(X,A,D,Z),(G,A,D,Z)]
Special[ARCTIC][SEACOAST]=[(G,A,D,D),(A,G,M,Z),(G,A,M,Z),(G,A,M,Z)]
Special[SUBARCTIC][DESERT]=[(G,A,D,D),(G,A,D,D),(A,S,D,D),(G,A,D,D)]
Special[SUBARCTIC][FOREST]=[(G,A,D,Z),(A,X,D,Z),(X,A,Z,D),(A,X,M,D)]
Special[SUBARCTIC][HILLS]=[(G,A,M,D),(A,G,D,Z),(A,X,Z,D),(G,A,M,D)]
Special[SUBARCTIC][MOUNTAINS]=[(G,A,D,M),(A,X,M,Z),(A,X,Z,D),(G,A,M,D)]
Special[SUBARCTIC][PLAINS]=[(G,A,M,D),(A,X,D,Z),(Z,A,Z,D),(G,A,D,Z)]
Special[SUBARCTIC][SEACOAST]=[(G,A,M,Z),(G,A,M,Z),(X,A,Z,M),(A,G,M,Z)]
Special[SUBARCTIC][SWAMP]=[(A,X,M,Z),(A,X,M,Z),(X,A,Z,M),(A,X,M,Z)]
Special[TEMPERATE][DESERT]=[(A,S,D,Z),(G,S,D,Z),(G,S,D,Z),(S,G,D,Z)]
Special[TEMPERATE][FOREST]=[(A,X,M,Z),(G,X,M,Z),(G,X,M,Z),(A,X,M,Z)]
Special[TEMPERATE][HILLS]=[(A,X,M,Z),(A,X,Z,T),(A,X,D,Z),(A,X,D,Z)]
Special[TEMPERATE][MOUNTAINS]=[(A,X,M,D),(A,X,M,Z),(A,X,D,Z),(X,A,D,Z)]
Special[TEMPERATE][PLAINS]=[(A,G,D,Z),(A,X,T,Z),(X,G,D,Z),(X,A,D,Z)]
Special[TEMPERATE][SEACOAST]=[(A,X,M,Z),(C,X,M,Z),(C,X,M,Z),(A,X,M,Z)]
Special[TEMPERATE][SWAMP]=[(A,X,M,Z),(G,X,M,Z),(G,X,M,Z),(A,X,M,Z)]
Special[SUBTROPICAL][DESERT]=[(A,S,D,Z),(G,S,D,Z),(G,S,D,Z),(G,S,D,Z)]
Special[SUBTROPICAL][FOREST]=[(X,A,M,Z),(X,G,Z,M),(X,X,Z,M),(A,X,M,Z)]
Special[SUBTROPICAL][HILLS]=[(A,X,D,Z),(A,X,D,T),(X,G,D,Z),(A,X,Z,M)]
Special[SUBTROPICAL][MOUNTAINS]=[(A,X,D,Z),(A,X,Z,M),(X,G,Z,D),(X,A,Z,M)]
Special[SUBTROPICAL][PLAINS]=[(A,X,D,Z),(X,G,Z,T),(X,G,D,Z),(G,A,D,Z)]
Special[SUBTROPICAL][SEACOAST]=[(A,X,D,Z),(C,X,M,Z),(C,X,M,Z),(C,X,D,Z)]
Special[SUBTROPICAL][SWAMP]=[(A,X,D,Z),(C,X,M,Z),(C,X,M,Z),(C,X,D,Z)]
Special[TROPICAL][DESERT]=[(A,S,D,Z),(G,S,D,Z),(G,S,D,Z),(G,S,D,Z)]
Special[TROPICAL][FOREST]=[(X,X,M,Z),(X,X,Z,M),(X,X,Z,M),(X,X,M,Z)]
Special[TROPICAL][HILLS]=[(A,G,D,Z),(G,X,D,Z),(G,X,D,Z),(G,G,Z,D)]
Special[TROPICAL][MOUNTAINS]=[(A,X,M,Z),(A,X,M,Z),(X,G,Z,M),(A,G,M,Z)]
Special[TROPICAL][PLAINS]=[(G,X,D,Z),(G,X,D,Z),(S,X,Z,D),(G,X,Z,D)]
Special[TROPICAL][SEACOAST]=[(X,A,D,Z),(A,X,M,Z),(C,X,M,Z),(X,A,Z,M)]
Special[TROPICAL][SWAMP]=[(A,X,Z,D),(G,X,Z,M),(X,G,M,Z),(X,A,M,Z)]

Humidity = {}
Humidity[ARCTIC] = {}
Humidity[SUBARCTIC] = {}
Humidity[TEMPERATE] = {}
Humidity[SUBTROPICAL] = {}
Humidity[TROPICAL] = {}
Humidity[ARCTIC][DESERT]=[L,L,L,L]
Humidity[ARCTIC][HILLS]=[L,L,L,L]
Humidity[ARCTIC][MOUNTAINS]=[L,L,L,L]
Humidity[ARCTIC][PLAINS]=[L,L,L,L]
Humidity[ARCTIC][SEACOAST]=[L,L,L,L]
Humidity[SUBARCTIC][DESERT]=[L,L,L,L]
Humidity[SUBARCTIC][FOREST]=[L,M,M,L]
Humidity[SUBARCTIC][HILLS]=[L,L,L,L]
Humidity[SUBARCTIC][MOUNTAINS]=[L,M,L,L]
Humidity[SUBARCTIC][PLAINS]=[L,M,M,L]
Humidity[SUBARCTIC][SEACOAST]=[L,M,M,L]
Humidity[SUBARCTIC][SWAMP]=[L,M,M,L]
Humidity[TEMPERATE][DESERT]=[L,L,L,L]
Humidity[TEMPERATE][FOREST]=[M,H,M,M]
Humidity[TEMPERATE][HILLS]=[M,H,H,M]
Humidity[TEMPERATE][MOUNTAINS]=[L,M,L,M]
Humidity[TEMPERATE][PLAINS]=[M,H,H,M]
Humidity[TEMPERATE][SEACOAST]=[H,M,M,H]
Humidity[TEMPERATE][SWAMP]=[M,H,H,M]
Humidity[SUBTROPICAL][DESERT]=[L,L,L,L]
Humidity[SUBTROPICAL][FOREST]=[H,H,H,H]
Humidity[SUBTROPICAL][HILLS]=[M,H,H,H]
Humidity[SUBTROPICAL][MOUNTAINS]=[M,H,H,H]
Humidity[SUBTROPICAL][PLAINS]=[M,H,M,L]
Humidity[SUBTROPICAL][SEACOAST]=[M,H,H,M]
Humidity[SUBTROPICAL][SWAMP]=[M,H,H,M]
Humidity[TROPICAL][DESERT]=[L,L,L,L]
Humidity[TROPICAL][FOREST]=[H,H,H,H]
Humidity[TROPICAL][HILLS]=[M,M,H,M]
Humidity[TROPICAL][MOUNTAINS]=[M,H,H,H]
Humidity[TROPICAL][PLAINS]=[M,H,H,H]
Humidity[TROPICAL][SEACOAST]=[M,H,H,M]
Humidity[TROPICAL][SWAMP]=[M,H,H,H]

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
climates = ['ARCTIC','SUBARCTIC','TEMPERATE','SUBTROPICAL','TROPICAL']
biomes = ['DESERT', 'FOREST', 'HILLS', 'MOUNTAINS', 'PLAINS', 'SEACOAST', 'SWAMP']
months = ['W1', 'W2', 'W3', 'SP1', 'SP2', 'SP3', 'A1', 'A2', 'A3', 'SU1', 'SU2', 'SU3']
f = open('outfile.txt', 'w')
writestring = 'local temps={'
for temp in range(len(letters)):
    writestring = writestring + f'{{low={Temps[temp][1]},high={Temps[temp][0]}}},'
writestring = writestring[:-1]+'}\n'
f.write(writestring)
writestring = 'local climates={'
for climate in range(len(climates)):
    writestring = writestring + f'{climates[climate]}={{'
    for terrain in range(7):
        writestring = writestring + f'{biomes[terrain]}={{'
        for month in range(12):
            writestring = writestring + f'{{low={Climate[climate][terrain][month][0]+1}'
            writestring = writestring + f', mid={Climate[climate][terrain][month][1]+1}'
            writestring = writestring + f', high={Climate[climate][terrain][month][2]+1}}},'
        writestring = writestring[:-1]
        writestring += '},'
    writestring = writestring[:-1]
    writestring += '},'
writestring = writestring[:-1]+'}'
f.write(writestring)
f.close()
