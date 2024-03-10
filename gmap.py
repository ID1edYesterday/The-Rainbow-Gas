import pygame


class gmap:
    
    def __init__(self):
        #load wall.jfif image 
        self.wall = pygame.image.load("wall.jfif")
        
        self.wall = pygame.transform.scale(self.wall, (50, 50))
        
        #initialize original locations on map
        self.levels = [[100,100,100,700,700,100,700,700] , [100,100,200,300,400,500]]
        
        self.level = self.levels[0]
        
    #check collision function
    def check_collision(self,P, direction):
        #needs to be implemented
        pass   
    

    def next_level(self):
        self.level = levels[1]
        
    def render(self,screen):
        for i in range(0, len(self.level)):
            screen.blit(self.wall, (self.level[i], self.level[i]))
            