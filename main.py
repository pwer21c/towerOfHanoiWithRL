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
pygame.display.set_caption('Tower of hanoi')




def animation(screen,disks) :
    
    pygame.display.flip()

class Alarm(tk.Frame):
    def __init__(self, msecs=1000):
        tk.Frame.__init__(self)
        self.msecs = msecs
        self.pack()
        stopper = tk.Button(self, text='Je suis un vrai bouton!')
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8)
        self.stopper = stopper
        self.repeater()

    def repeater(self):
        self.bell()
        self.stopper.flash()
        self.after(self.msecs, self.repeater)
        
def main() :

    pygame.init()
    size=[500,400]
    screen.fill([0,0,0])
    #creation(screen)
    number_of_disks=3
    disks=defaultCreation(screen)
    disks[0].display()
    disks[1].display()
    disks[2].display()

    while True :
        
        event = pygame.event.poll()  
        if event.type == pygame.QUIT: break 
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.dict["button"])
            if event.dict["button"] == 1 :
                screen.fill([0,0,0])
                for rod in rods:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), rod.rect)
                disks[2].move(disks[2].x0+125,disks[2].y0)
                disks[1].display()
                disks[0].display()
                liste_points.append(event.dict["pos"])
            if event.dict["button"] == 3 :
                Alarm().mainloop()
        animation(screen,disks)
    pygame.quit()
        
main()