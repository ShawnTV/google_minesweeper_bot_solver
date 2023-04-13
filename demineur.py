import os
import pyautogui as gui
import time
import shutil
from PIL import Image
from PIL import ImageDraw
import numpy as np

N = 0.5
I = 0

def new_grille():
    grille = []
    for y in range(8):
        grille.append([])
    for x in range(8):
        for y in range(10):
            grille[x].append("-")
    return grille

def representer_grille(grille):
    for i in range(len(grille)):
        print(grille[i])

def couleur(X, Y, x, y, image2):


    rouge = [[211, 51, 51], [211, 50, 49], [211,  48,  48], [211,  47,  47], [211,  48,  47]]
    for i in range(len(rouge)):
        if image2[Y][X][0] == rouge[i][0] or image2[Y+5][X][0] == rouge[i][0] or image2[Y][X+5][0] == rouge[i][0] or image2[Y+5][X+5][0] == rouge[i][0]:
            if image2[Y][X][1] == rouge[i][1] or image2[Y+5][X][1] == rouge[i][1] or image2[Y][X+5][1] == rouge[i][1] or image2[Y+5][X+5][1] == rouge[i][1]:
                if image2[Y][X][2] == rouge[i][2] or image2[Y+5][X][2] == rouge[i][2] or image2[Y][X+5][2] == rouge[i][2] or image2[Y+5][X+5][2] == rouge[i][2]:
                    print((x,y), "rouge")
                    grille[y][x] = "3"
    rouge = [211]
    for i in range(len(rouge)):
        if image2[Y][X][0] == rouge[i] or image2[Y+5][X][0] == rouge[i] or image2[Y][X+5][0] == rouge[i] or image2[Y+5][X+5][0] == rouge[i]:

            print((x,y), "rouge")
            grille[y][x] = "3"




    vert = [[56, 142, 60], [59, 142, 61], [66, 144, 66], [77, 147, 72], [72, 146, 69], [77, 147, 72], [ 69, 146,  67], [108, 157,  89], [ 65, 144,  65], [64, 144, 65], [ 66,144,  65], [ 68 ,145  ,67], [ 64, 144,  64], [ 70, 145,  68], [ 63, 144,  64], [ 59, 142,  62], [ 62, 144,  63], [ 62, 143,  63], [ 58, 142,  61], [ 81, 149,  74]]
    for i in range(len(vert)):
        if image2[Y][X][0] == vert[i][0] or image2[Y+5][X][0] == vert[i][0] or image2[Y][X+5][0] == vert[i][0] or image2[Y+5][X+5][0] == vert[i][0]:
            if image2[Y][X][1] == vert[i][1] or image2[Y+5][X][1] == vert[i][1] or image2[Y][X+5][1] == vert[i][1] or image2[Y+5][X+5][1] == vert[i][1]:
                if image2[Y][X][2] == vert[i][2] or image2[Y+5][X][2] == vert[i][2] or image2[Y][X+5][2] == vert[i][2] or image2[Y+5][X+5][2] == vert[i][2]:
                    print((x,y), "vert")
                    grille[y][x] = "2"
    vert = [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]
    for i in range(len(vert)):
        if image2[Y][X][1] == vert[i] or image2[Y+5][X][1] == vert[i] or image2[Y][X+5][1] == vert[i] or image2[Y+5][X+5][1] == vert[i]:

            print((x,y), "vert")
            grille[y][x] = "2"


    violet = [[123,  31, 162]]
    for i in range(len(violet)):
        if image2[Y][X][0] == violet[i][0] or image2[Y+5][X][0] == violet[i][0] or image2[Y][X+5][0] == violet[i][0] or image2[Y+5][X+5][0] == violet[i][0]:
            if image2[Y][X][1] == violet[i][1] or image2[Y+5][X][1] == violet[i][1] or image2[Y][X+5][1] == violet[i][1] or image2[Y+5][X+5][1] == violet[i][1]:
                if image2[Y][X][2] == violet[i][2] or image2[Y+5][X][2] == violet[i][2] or image2[Y][X+5][2] == violet[i][2] or image2[Y+5][X+5][2] == violet[i][2]:
                    print((x,y), "violet")
                    grille[y][x] = "4"


    bleu = [[25,  118, 210]]
    for i in range(len(bleu)):
        if image2[Y][X][0] == bleu[i][0] or image2[Y+5][X][0] == bleu[i][0] or image2[Y][X+5][0] == bleu[i][0] or image2[Y+5][X+5][0] == bleu[i][0]:
            if image2[Y][X][1] == bleu[i][1] or image2[Y+5][X][1] == bleu[i][1] or image2[Y][X+5][1] == bleu[i][1] or image2[Y+5][X+5][1] == bleu[i][1]:
                if image2[Y][X][2] == bleu[i][2] or image2[Y+5][X][2] == bleu[i][2] or image2[Y][X+5][2] == bleu[i][2] or image2[Y+5][X+5][2] == bleu[i][2]:
                    print((x,y), "bleu")
                    grille[y][x] = "1"


def probleme_grille(grille):
    k = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == "-":
                k = 1
    if k==0:
        print("scan validé")
    else:
        print("erreur dans le scan")


def scan(grille):
    import pyscreenshot
    #time.sleep(3)
    time.sleep(1.5)

    image = pyscreenshot.grab()
    image.save("etat3.png")

    image = Image.open("etat3.png")
    image2 = np.copy(image)

    largeur, hauteur = image.size




    dict = {}

    Y =430

    for y in range(8):
        Y = 432 + 56*y
        for x in range(10):
            X = 707 + 56*x


            #dict[(x, y)] = [(b0, a), (b0+5, a), (b0, a+5), (b0+5, a+5)], [image2[b0, a], image2[b0+5, a], image2[b0, a+5], image2[b0+5, a+5]]
            #print((x, y), image2[Y][X])
            # image2[Y][X] = np.array([ 255, 0,  0])
            # image2[Y+5][X] = np.array([ 255, 0,  0])
            # image2[Y][X+5] = np.array([ 255, 0,  0])
            # image2[Y+5][X+5] = np.array([ 255, 0,  0])

            compteur = 0

            for i in range(3):
                if image2[Y][X][i] == image2[Y+5][X][i] and image2[Y][X][i] == image2[Y][X+5][i] and image2[Y][X][i] == image2[Y+5][X+5][i]:
                    compteur +=1
            if compteur == 3:
                #print("tout les pixels de", (x, y), "sont identiques et", image2[Y][X])
                if image2[Y][X][0] == 229 and image2[Y][X][1] == 194 and image2[Y][X][2] == 159:
                    grille[y][x] = "0"
                if image2[Y][X][0] == 215 and image2[Y][X][1] == 184 and image2[Y][X][2] == 153:
                    grille[y][x] = "0"
                if image2[Y][X][0] == 170 and image2[Y][X][1] == 215 and image2[Y][X][2] == 81:
                    grille[y][x] = "?"
                if image2[Y][X][0] == 162 and image2[Y][X][1] == 209 and image2[Y][X][2] == 73:
                    grille[y][x] = "?"
            else:
                print("pas la meme couleur")
                print((x, y), image2[Y][X], image2[Y+5][X] , image2[Y][X] , image2[Y][X+5])

                couleur(X, Y, x, y, image2) #Modifie la grille avec les valeurs des couleurs des pixels


    #representer_grille(grille)
    probleme_grille(grille)

    return grille



def lancer_partie():
    os.system("start firefox") #os.system(cmd) exécute cmd
    time.sleep(N)
    gui.moveTo(366, 78)
    gui.leftClick()
    gui.write("demineur")
    time.sleep(N)
    gui.press("enter")
    time.sleep(N)
    gui.moveTo(636, 751)
    gui.leftClick()
    time.sleep(N+1)
    gui.moveTo(679, 326)
    gui.leftClick()
    time.sleep(N)
    gui.moveTo(691, 356)
    gui.leftClick()
    time.sleep(N)
    gui.moveTo(713, 415)
    gui.leftClick()

###A reprendre
# def jouer(grille):
#     for x in range(10):
#         for y in range(8):
#             if grille[y][x] == 0:
#                 if y!=0 and y!=ç and x!=0 and x!=9:
#                     if grille[y-1][x-1] + ==0
#
# #


lancer_partie()
grille = new_grille()
grille = scan(grille)

#time.sleep(1)
#grille = scan(grille)
#time.sleep(0.5)

representer_grille(grille)























