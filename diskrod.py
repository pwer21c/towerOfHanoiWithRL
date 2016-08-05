

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

def defaultCreation(screen):
    
    temps=[]
    Rod = namedtuple('Rod', ['rect', 'items'])
            
    rods = (Rod(pygame.rect.Rect((100, 150, 25, 250)), [3, 2, 1]),
                    Rod(pygame.rect.Rect((225, 150, 25, 250)), []),
                    Rod(pygame.rect.Rect((350, 150, 25, 250)), []))
                
    for rod in rods:
        pygame.draw.rect(screen, pygame.color.Color('yellow'), rod.rect)
        for i, item in enumerate(rod.items):
            r = pygame.rect.Rect(rod.rect.x - item * 8, 375 - 25 * i, 25 + item * 16, 25)
            disk=Disk(r)
            pygame.draw.rect(screen, pygame.color.Color('green'), r)
            temps.append(disk)
                
    return temps



def animation(screen,disks) :
    #pos_vit[0]+=pos_vit[2]
    #pos_vit[1]+=pos_vit[3]
    #if pos_vit[0]<0 or pos_vit[0]>=screen.get_width() :
    #    pos_vit[2]*=-1
    #if pos_vit[1]<0 or pos_vit[1]>=screen.get_height() :
    #    pos_vit[3]*=-1
    # create a named tuple to keep track of the size/location of the rods and their blocks
    
    pygame.display.flip()
