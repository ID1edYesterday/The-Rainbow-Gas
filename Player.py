import pygame

class Player:
    
    def __init__(self):
        self.name = ""
        self.health = 100
        self.speed = 1
        self.has_bomb = False
        self.loc_x = 200
        self.loc_y = 0
        self.sprite = None
        self.left = 0
        
        self.width = 50
        self.height = 50
        
     
    def load_sprite(self, file_path):
        self.sprite = pygame.image.load(file_path)
        #update self.top width and height variables
        self.left = self.loc_x
        self.top = self.loc_y
        
        
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        

    def render(self, screen):
        if self.sprite is not None:
            screen.blit(self.sprite, (self.loc_x, self.loc_y))
         
    def move(self, direction):
        if direction == "up":
            self.loc_y -= self.speed
        elif direction == "down":
            self.loc_y += self.speed
        elif direction == "left":
            self.loc_x -= self.speed
        elif direction == "right":
            self.loc_x += self.speed

    def pick_up_bomb(self):
        self.has_bomb = True

    def use_bomb(self):
        if self.has_bomb:
            # Code to use the bomb
            self.has_bomb = False
        
    def get_sprite(self):
        return self.sprite
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Game Over")
            
    
    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Speed: {self.speed}")
        print(f"Location: ({self.loc_x}, {self.loc_y})")
        print(f"Has Bomb: {self.has_bomb}")