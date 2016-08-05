import pygame
import Tkinter as tk
from collections import namedtuple
import random
import math
import world


pos_vit=[100,100,0.3,-0.5]
liste_points=[]
checkauto=True

background_color = (255,255,255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
(width,height)=(500,400)
screen=pygame.display.set_mode((width,height))
number_of_disks=3

pygame.display.set_caption('Tower of hanoi')
Rod = namedtuple('Rod', ['rect', 'items'])
rods = (Rod(pygame.rect.Rect((100, 150, 25, 250)), [3, 2, 1]),
        Rod(pygame.rect.Rect((225, 150, 25, 250)), [3,2,1]),
        Rod(pygame.rect.Rect((350, 150, 25, 250)), [3,2,1]))
disks=[]

world2 ={
         1:{'name':2, 'rodname':'rod1','occupy':True, 'canMove':True, 'canPut':False, 'dx':100,'dy':325},
         2:{'name':1, 'rodname':'rod1','occupy':True, 'canMove':False, 'canPut':False,'dx':100,'dy':350},
         3:{'name':0, 'rodname':'rod1','occupy':True, 'canMove':False, 'canPut':False,'dx':100,'dy':375},
         
         4:{'name':'vide', 'rodname':'rod2','occupy':False, 'canMove':False, 'canPut':False,'dx':225,'dy':325},
         5:{'name':'vide', 'rodname':'rod2','occupy':False, 'canMove':False, 'canPut':False,'dx':225,'dy':350},
         6:{'name':'vide', 'rodname':'rod2','occupy':False, 'canMove':False, 'canPut':True,'dx':225,'dy':375},
         
         7:{'name':'vide', 'rodname':'rod3','occupy':False, 'canMove':False, 'canPut':False,'dx':350,'dy':325},
         8:{'name':'vide', 'rodname':'rod3','occupy':False, 'canMove':False, 'canPut':False,'dx':350,'dy':350},
         9:{'name':'vide', 'rodname':'rod3','occupy':False, 'canMove':False, 'canPut':True,'dx':350,'dy':375}
}




class Disk():
    def __init__(self, colour, (x0, y0, x1, y1)):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colour = colour
    
    def display(self):
        pygame.draw.rect(screen, self.colour, (int(self.x0), int(self.y0), int(self.x1), int(self.y1)))
    
    def move(self, dx, dy):
        self.x0=dx
        self.y0=dy
        if dx != 0:
            self.display()
        if dy != 0:
            self.display()

def modifyOrigin(ckey,cposition):
    world2[ckey]['occupy']=False
    transit=world2[ckey]['name']
    
    world2[cposition]['occupy']=True
    world2[cposition]['name']=transit
    world2[ckey]['name']='vide'
    
    rodlists=['rod1','rod2','rod3']
    
    for rdlist in rodlists:
      listprod=[]
      listprod_sub=[]
      for key,value in world2.iteritems():
          
          if value['rodname']== rdlist :
              world2[key]['canMove']=False
              world2[key]['canPut']=False
              listprod_sub.append(key)
              if world2[key]['occupy']:
                 listprod.append(key)
    
    
      if listprod:
         world2[listprod[0]]['canMove']=True

      if len(listprod)==0:
         world2[listprod_sub[2]]['canPut']=True
      elif len(listprod)==1:
         world2[listprod_sub[1]]['canPut']=True
      elif len(listprod)==2:
         world2[listprod_sub[0]]['canPut']=True


    return True



def modifyCanPut():
    return True

def modifyCanMove():
    return True

def chooseDisk():
    choiceGroup=[]
    for key,value in world2.iteritems():
        if value['canMove']:
            choiceGroup.append(key)
    key=random.choice(choiceGroup)
    return world2[key]['name']

def chooseDiskGetKey():
    choiceGroup=[]
    for key,value in world2.iteritems():
        if value['canMove']:
            choiceGroup.append(key)
    key=random.choice(choiceGroup)
    return key



def unChooseDisk():
    choices=[]
    for key,value in world2.iteritems():
        if not value['canMove']:
            if value['occupy']:
                choices.append(key)
    return choices


def choosePosition(ckey):
    choiceGroup=[]
    for key,value in world2.iteritems():
        if value['canPut']:
            if world2[ckey]['rodname'] != world2[key]['rodname']:
              choiceGroup.append(key)
    return random.choice(choiceGroup)


def displayRods(screen):
   for rod in rods:
       pygame.draw.rect(screen, pygame.color.Color('yellow'), rod.rect)


def disksValues():
    colortable=[BLUE,GREEN,RED]
    for rod in rods:
        for i, item in enumerate(rod.items):
            r = pygame.rect.Rect(rod.rect.x - item * 8, 375 - 25 * i, 25 + item * 16, 25)
            disk=Disk(colortable[i],r)
            disks.append(disk)

def isTrue():
    returnvalue=False
    if world2[7]['name']==2 and world2[8]['name']==1 and world2[9]['name']==0:
       returnvalue=True
    return returnvalue


def animation(screen) :
    pygame.display.flip()
    pygame.time.wait(100)


def main() :

    pygame.init()
    size=[500,400]
    
    screen.fill([0,0,0])
    
    displayRods(screen)
    disksValues()
    disks[0].display()
    disks[1].display()
    disks[2].display()
    
 
    number=0
    while True :
        
        event = pygame.event.poll()
        if checkauto :
            
            screen.fill([0,0,0])
            displayRods(screen)
            cdisk=chooseDisk()
            ckey=chooseDiskGetKey()
            cposition=choosePosition(ckey)
        
            remain=[2,1,0]
            remain.remove(world2[ckey]['name'])
            if world2[ckey]['name']==0:
                calcul=24
            elif world2[ckey]['name']==1:
                calcul=16
            else:
                calcul=8
            disks[world2[ckey]['name']].move(world2[cposition]['dx']-calcul,world2[cposition]['dy'])
        
            for keyy in remain:
                disks[keyy].display()
        
            modifyOrigin(ckey,cposition)

            if isTrue():
                print world2
                break
            
            white = (255, 255, 255)
            number+=1
            message=str(number)
            font = pygame.font.Font(None, 40)
            text = font.render(message, 1, white)
            screen.blit(text,(10,10))
            animation(screen)
        

        if event.type == pygame.KEYDOWN:
            #print(event.dict["key"])
            if event.dict["key"] == pygame.K_LEFT :
                screen.fill([0,0,0])
                displayRods(screen)
                
                cdisk=chooseDisk()
                ckey=chooseDiskGetKey()
                cposition=choosePosition(ckey)
                
                remain=[2,1,0]
                remain.remove(world2[ckey]['name'])
                if world2[ckey]['name']==0:
                      calcul=24
                elif world2[ckey]['name']==1:
                      calcul=16
                else:
                      calcul=8
                disks[world2[ckey]['name']].move(world2[cposition]['dx']-calcul,world2[cposition]['dy'])
                for keyy in remain:
                    disks[keyy].display()
                modifyOrigin(ckey,cposition)
                #print world2
            if event.dict["key"] == pygame.K_ESCAPE : break
        animation(screen)
    pygame.quit()
        
main()