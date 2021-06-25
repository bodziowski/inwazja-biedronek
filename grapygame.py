import pygame
import os 
import random

from pygame.event import wait
dotyka = 0
pygame.init()
szerokosc = 500
wysokosc = 500
punkty = 0
ekran = pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption("biedronki")
def napisz(tekst, x, y, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, 1, (255,100,100))
    ekran.blit(rend, (x,y))
class Odbicie:
    def __init__(self,x,y,szer,wys):
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.ksztaltt = pygame.Rect(self.x,self.y,self.szer,self.wys)
        self.kolor = (255,255,255)
    def Ksztalt(self):
        return self.ksztaltt
    def rysuj(self):
        pygame.draw.rect(ekran,self.kolor,self.ksztaltt,0)
class biedronka():
    def __init__(self):
        self.x = random.randint(30,450)
        self.y = random.randint(30,450)
        self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        self.grafika = pygame.image.load(os.path.join("biedronka.png"))
        self.kierunek = random.randint(1,4)
    def rysuj(self):
        ekran.blit(self.grafika,(self.x,self.y))
    def ksztalt(self):
        self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        return self.ksztalt
    def kordynaty(self):
        print("oś x: ",self.x," oś y: ",self.y)
    def szer(self):
        return self.y
    def wys(self):
        return self.y
    def ruch(self,prędkość):
            self.prędkość = prędkość
            if self.kierunek == 1:
                self.x = self.x+self.prędkość 
                self.ksztalt = pygame.Rect(self.x,self.y,25,25)
            elif self.kierunek == 2:
                self.x = self.x-self.prędkość
                self.ksztalt = pygame.Rect(self.x,self.y,25,25)
            elif self.kierunek == 3:
                self.y = self.y + self.prędkość
                self.ksztalt = pygame.Rect(self.x,self.y,25,25)
            elif self.kierunek ==4:
                self.y = self.y-self.prędkość
                self.ksztalt = pygame.Rect(self.x,self.y,25,25)
    def koolizja(self,obiekt):
        self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        if self.ksztalt.colliderect(obiekt):
            print("dotyka")
            return True
        else:
            return False
    def Obicie(self,prędkość):
        self.prędkość = prędkość
        if self.kierunek == 1:
            self.x = self.x-self.prędkość
        elif self.kierunek == 2:
            self.x = self.x+self.prędkość
        elif self.kierunek == 3:
            self.y = self.y - self.prędkość
        elif self.kierunek ==4:
            self.y = self.y+self.prędkość
    def zmienkierunek(self):
        self.kierunek = random.randint(1,4)
class gracz():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        self.kolor = (255,255,255)
    def rysuj(self):
        pygame.draw.rect(ekran,self.kolor,self.ksztalt,0)
    def ruch(self,prędkość,kierunek):
        self.kierunek = kierunek
        self.prędkość = prędkość
        if self.kierunek == 1:
            self.x = self.x-self.prędkość
            self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        elif self.kierunek == 2:
            self.x = self.x+self.prędkość
            self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        elif self.kierunek == 3:
            self.y = self.y - self.prędkość
            self.ksztalt = pygame.Rect(self.x,self.y,25,25)
        elif self.kierunek ==4:
            self.y = self.y+self.prędkość
            self.ksztalt = pygame.Rect(self.x,self.y,25,25)
    def KKsztalt(self):
        return self.ksztalt

oobiecie = []
lol = []
odbicie = 0
graczz = gracz(250,250)
for i in range(1):
    lol.append(Odbicie(0,0,1,1000))
    lol.append(Odbicie(0,0,1000,1))
    lol.append(Odbicie(499,0,1,1000))
    lol.append(Odbicie(0,499,1000,1))
biedra = biedronka()
biedronki = []
biedronkakolizja = []
for i in range(20):
    biedronki.append(biedronka())
conaekranie = "gra"
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                odbicie = 3
            if event.key == pygame.K_LEFT:
                odbicie = 1
            if event.key == pygame.K_RIGHT:
                odbicie = 2
            if event.key == pygame.K_DOWN:
                odbicie = 4
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space")
                if conaekranie == "przegrana":
                    print("space2")
                    punkty = 0
                    conaekranie = "gra"
                    del biedronki
                    biedronki = []
                    for i in range(20):
                        biedronki.append(biedronka())
                    graczz = gracz(250,250)
                    del biedronkakolizja
                    biedronkakolizja = []
    ekran.fill((0,0,0))
    if conaekranie == "przegrana":
        napisz("twój wynik to: "+str(punkty),50,50,25)
        napisz("przegrałeś",50,250,100)
        napisz("naciśnij space aby zagrać ponownie",50,150,25)
    if conaekranie == "gra":
        if True:
            punkty+=1
            napisz(str(punkty),50,50,25)
        graczz.rysuj()
        if odbicie == 1:
            graczz.rysuj()
            graczz.ruch(0.10,1)
        if odbicie == 2:
            graczz.rysuj()
            graczz.ruch(0.10,2)
        if odbicie == 3:
            graczz.rysuj()
            graczz.ruch(0.10,3)
        if odbicie == 4:
            graczz.rysuj()
            graczz.ruch(0.10,4)
        for i in biedronki:
            i.rysuj()
            i.ruch(0.09)
            if random.randint(0,500)==50:
                i.zmienkierunek()
            if i.koolizja(graczz.KKsztalt()):
                conaekranie = "przegrana"
            for x in lol:
                if i.koolizja(x.Ksztalt()):
                    print("biedra",len(biedronki))
                    print("biedrakol:",len(biedronkakolizja))
                    biedronkakolizja.append(i)
                    biedronki.remove(i)
                    i.kordynaty()
        for x in biedronkakolizja:
            x.rysuj()
            x.Obicie(0.09)
            if x.koolizja(graczz.KKsztalt()):
                conaekranie = "przegrana"
            if random.randint(0,500)==50:
                x.zmienkierunek()
            for i in lol:
                if x.koolizja(i.Ksztalt()):
                    print("biedra",len(biedronki))
                    print("biedrakol:",len(biedronkakolizja))
                    biedronki.append(x)
                    biedronkakolizja.remove(x)
                    dotyka = 1
    pygame.display.update()