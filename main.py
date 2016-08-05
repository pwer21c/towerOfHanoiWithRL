import pygame
import Tkinter as tk
from collections import namedtuple
import random
import math


pos_vit=[100,100,0.3,-0.5]
liste_points=[]

background_color = (255,255,255)
(width,height)=(500,400)
screen=pygame.display.set_mode((width,height))
number_of_disks=3

pygame.display.set_caption('Tower of hanoi')
Rod = namedtuple('Rod', ['rect', 'items'])
rods = (Rod(pygame.rect.Rect((100, 150, 25, 250)), [3, 2, 1]),
        Rod(pygame.rect.Rect((225, 150, 25, 250)), []),
        Rod(pygame.rect.Rect((350, 150, 25, 250)), []))
disks=[]

class Disk():
    def __init__(self, (x0, y0, x1, y1)):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colour = (0, 0, 255)
    
    def display(self):
        pygame.draw.rect(screen, self.colour, (int(self.x0), int(self.y0), int(self.x1), int(self.y1)))
    
    def move(self, dx, dy):
        self.x0=dx
        self.y0=dy
        if dx != 0:
            self.display()
        if dy != 0:
            self.display()

def displayRods(screen):
   for rod in rods:
       pygame.draw.rect(screen, pygame.color.Color('yellow'), rod.rect)


def disksValues():
    for rod in rods:
        for i, item in enumerate(rod.items):
            r = pygame.rect.Rect(rod.rect.x - item * 8, 375 - 25 * i, 25 + item * 16, 25)
            disk=Disk(r)
            disks.append(disk)


def animation(screen) :
    pygame.display.flip()


def main() :

    pygame.init()
    size=[500,400]
    
    screen.fill([0,0,0])
    
    displayRods(screen)
    disksValues()
    disks[0].display()
    disks[1].display()
    disks[2].display()
    
    print disks[0].x0, disks[0].y0
    print disks[1].x0, disks[1].y0
    print disks[2].x0, disks[2].y0
    

    while True :
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            #print(event.dict["key"])
            if event.dict["key"] == pygame.K_RIGHT :
                screen.fill([0,0,0])
                displayRods(screen)
                disks[2].move(disks[2].x0+125,disks[2].y0)
                print disks[2].x0, disks[2].y0
                disks[1].display()
                disks[0].display()
            if event.dict["key"] == pygame.K_LEFT :
                screen.fill([0,0,0])
                displayRods(screen)
                disks[2].move(disks[2].x0-125,disks[2].y0)
                print disks[2].x0, disks[2].y0
                disks[1].display()
                disks[0].display()
            if event.dict["key"] == pygame.K_ESCAPE : break
        animation(screen)
    pygame.quit()
        
main()