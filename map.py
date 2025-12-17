import tkiteasy as tki
NCASE=16
NFLEURS=4
TAILLE=30
NECTAR_INITIALE=10
NECTAR_MAX=45
COUT_PONTE=10
TIME_OUT=300
TIME_KO=5

map=tki.ouvrirFenetre(800,1080)

for a in range (0, 500, 30):
    map.dessinerLigne(a, 0, a, 479, "white")

for a in range (0, 500 , 30):
    map.dessinerLigne(0, a, 479, a, "white" )


map.attendreClic() 
map.fermerFenetre()