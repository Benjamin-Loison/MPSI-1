# -*- coding: utf-8 -*-
"""
                       TP 11 : Traitement d'images PGM
            @author: Sébastien RÉAU - sebastien.reau@ac-paris.fr
"""




#------------------------------------------------------------------------------
# O. Définition du répertoire de travail
#------------------------------------------------------------------------------

from os import chdir as cd, getcwd as dir

""" Observer la syntaxe d'import et de renommage des fonctions chdir et
    getcwd ; prévoir le résultat de l'exécution des 3 lignes suivantes.
"""

print(dir())
cd('C:\\Users\\Benjamin LOISON\\Desktop\\')
print(dir())

""" Définir le bureau comme espace de travail par défaut. Y placer le fichier
    logo.pgm à télécharger depuis l'adresse Internet habituelle
"""


#------------------------------------------------------------------------------
# I. Visualisation des images PGM
#------------------------------------------------------------------------------


""" Double-cliquer sur l'icône du fichier logo.pgm : OpenOffice permet
    la visualisation des images enregistrées en ce format "exotique".
"""
   
    
#------------------------------------------------------------------------------
# II. Lecture pas à pas et mise en mémoire de l'image logo.pgm
#------------------------------------------------------------------------------
    
#print(list(file.readline())) # nice

file = open("logo.pgm", "rb")
print(file.readline())
print(file.readline())
sizeLine = file.readline().decode("UTF-8")
sizeLine
sizes = sizeLine.split()
width = int(sizes[0])
height = int(sizes[1])
print(width, height)
print(file.readline())
pix = [[0] * width for i in range(height)]
for heightIndex in range(height):
    for widthIndex in range(width):
        pix[heightIndex][widthIndex] = file.read(1)[0]
# print(pix)
print(pix[0][width - 1])
file.close()


""" Quelle est la taille de l'image lue ?
    Quelle est l'intensité de gris du pixel en haut à droite ?
"""


#------------------------------------------------------------------------------
# III. Lecture et mise en mémoire d'une image PGM quelconque
#------------------------------------------------------------------------------

def lire(path) :
    file = open(path, "rb")
    file.readline()
    file.readline()
    sizeLine = file.readline().decode("UTF-8")
    sizeLine
    sizes = sizeLine.split()
    width = int(sizes[0])
    height = int(sizes[1])
    file.readline()
    pix = [[0] * width for i in range(height)]
    for heightIndex in range(height):
        for widthIndex in range(width):
            pix[heightIndex][widthIndex] = file.read(1)[0]
    # print(pix)
    file.close()
    return pix
  
#------------------------------------------------------------------------------
# IV. Enregistrement d'une image au format PGM
#------------------------------------------------------------------------------

# 1. Détection de la taille d'une matrice
    
def taille(pix):
    return (len(pix), len(pix[0]))

# 2. Ecriture sur disque de l'image au format PGM
           
def enregistrer(pix, path) :
    (H, L) = taille(pix)
    file = open(path, 'wb')
    entete  = 'P5\n'
    entete += '# MPSI Fénelon\n'
    entete += str(L) + ' ' + str(H) + '\n'
    entete += '255\n'
    file.write(entete.encode('utf-8'))
    for heightIndex in range(H):
        for widthIndex in range(L):
            #print(pix[heightIndex][widthIndex])
            #print([pix[heightIndex][widthIndex]])
            #print(bytes([pix[heightIndex][widthIndex]]))
            file.write(bytes([pix[heightIndex][widthIndex]]))
    file.close()   
   
# 3. Tests à la console

image = [[0]*300 for i in range(200)]
enregistrer(image, 'test.pgm')
image = [[(i+j)%256 for j in range(256)] for i in range(256)]
enregistrer(image, 'test.pgm')

#------------------------------------------------------------------------------
# V. Traitement élémentaire d'image
#------------------------------------------------------------------------------

def inverse(pix):
    (H, L) = taille(pix)
    for heightIndex in range(H):
        for widthIndex in range(L):
            pix[heightIndex][widthIndex] = 255 - pix[heightIndex][widthIndex]
    return pix
    
def inverse(pix):
    return [[ 255 - pix[i][j] for j in range(len(pix[0]))] for i in range(len(pix))]

# 1. Inversion des niveaux de gris

def convertBlackWhite(pix): # one line ? list par comprehension (for)
    (H, L) = taille(pix)
    for heightIndex in range(H):
        for widthIndex in range(L):
            pix[heightIndex][widthIndex] = int(pix[heightIndex][widthIndex] < 50) * 255
    return pix

# 2. Conversion noir et blanc

def rotate(pix): # respond to exercice
    (H, L) = taille(pix)
    newPix = [[0] * H for i in range(L)]
    for heightIndex in range(L):
        for widthIndex in range(H):
            newPix[heightIndex][widthIndex] = pix[widthIndex][L - 1 - heightIndex]
    return newPix

def rotate(pix):
    (H, L) = taille(pix)
    newPix = [[0] * H for i in range(L)]
    for heightIndex in range(L):
        for widthIndex in range(H):
            newPix[heightIndex][widthIndex] = pix[H - 1 - widthIndex][heightIndex]
    return newPix

# 3. Rotation de 90 ° dans le sens horaire

# 4. Doublement de la taille de l'image
    
def enlarge(pix):
    (H, L) = taille(pix)
    H *= 2
    L *= 2
    newPix = [[0] * L for i in range(H)]
    for heightIndex in range(H):
        for widthIndex in range(L):
            newPix[heightIndex][widthIndex] = pix[heightIndex // 2][widthIndex // 2]
    return newPix
    
def contour(p):
    s = 1
    p = convertBlackWhite(p)
    (H, L) = taille(p)
    nP = [[0] * L for i in range(H)]
    for i in range(1, H - 1):
        for j in range(1, L - 1):
            hori = abs(p[i][j - 1] - p[i][j]) < s and abs(p[i][j + 1] - p[i][j]) < s
            vert = abs(p[i - 1][j] - p[i][j]) < s and abs(p[i + 1][j] - p[i][j]) < s
            # print(hori, vert)
            if hori and vert:
                nP[i][j] = 0
            else: nP[i][j] = 255
    return nP
    
enregistrer(contour(lire("logo.pgm")), "contour.pgm")
    
# 03/04/19 + faire en compréhension si on s'ennuie


import math

def rondBlancFondNoir(size = 100, ray = 25, points = 1000):
    center = size // 2
    image = [[0]*size for i in range(size)]
    for point in range(points):
        x = int(rayon * math.cos(2 * math.pi * point / points))
        y = center + int(rayon * math.sin(2 * math.pi * point / points))
        for i in range(2 * x):
            image[y][center - x + i] = 255;
    return image

def rondBlancFondNoir(size = 100, ray = 25, points = 1000):
    return [list(reversed(p[i])) for i in range(taille(p)[0])]

def sattelite(size = 100, points = 1000, raySpace = 3):
    center = size // 2
    image = [[0]*size for i in range(size)]
    for ray in range(0, center, raySpace):
        for point in range(points):
            x = center + int(ray * math.cos(2 * math.pi * point / points))
            y = center + int(ray * math.sin(2 * math.pi * point / points))
            image[y][x] = 255
    return image

def horiMirror(p):
    (H, L) = taille(p)
    for i in range(H):
        p[i] = list(reversed(p[i]))
    return p

def horiMirror(p):
    return [list(reversed(p[i])) for i in range(taille(p)[0])]

def sumList(l0, l1): # assume same size
    return [min(l0[i] + l1[i], 255) for i in range(len(l0))]
    
def sumList(l0, l1): # assume same size
    return [min(l0[i], l1[i]) for i in range(len(l0))]

def superpose(p0, p1): # assume same sizes
    return [sumList(p0[i], p1[i])  for i in range(taille(p0)[0])]

original = lire("logo.pgm")
one = horiMirror(original)
enregistrer(one, "1.pgm")
two = rotate(rotate(original))
enregistrer(two, "2.pgm")
three = horiMirror(rotate(rotate(original)))
enregistrer(three, "3.pgm")

oriOne = superpose(original, one)
#enregistrer(oriOne, "superpose.pgm")
twoThree = superpose(two, three)
all = superpose(oriOne, twoThree)
enregistrer(all, "superpose.pgm")
enregistrer(convertBlackWhite(all), "superposeBW.pgm")

def collage(p0, p1, p2, p3): # assume all same sizes
    return [p0[i] + p1[i] for i in range(taille(p0)[0])] + [p2[i] + p3[i] for i in range(taille(p0)[0])]
    
enregistrer(collage(original, one, three, two), "collage.pgm")

def flou(p, size = 125): # ou tampon qui fais des combinaisons linéaires des pixels environnants
    (H, L) = taille(p)
    nP = [[0]*size for i in range(size)]
    for lineIndex in range(size):
        for widthIndex in range(size):  
            sizeX = L / size
            sizeY = H / size
            count = 0
            for i in range(int(lineIndex * sizeY), int((lineIndex + 1) * sizeY)):
                for j in range(int(widthIndex * sizeX), int((widthIndex + 1) * sizeX)):
                    nP[lineIndex][widthIndex] += p[i][j]
                    count += 1
            nP[lineIndex][widthIndex] /= count
            nP[lineIndex][widthIndex] = int(nP[lineIndex][widthIndex])
            #print(lineIndex, widthIndex, nP[lineIndex][widthIndex], count, sizeX * sizeY)
    
    while taille(nP)[0] < H or taille(nP)[1] < L:
        nP = enlarge(nP)
    return nP
    
enregistrer(flou(lire("logo.pgm")), "flou.pgm")