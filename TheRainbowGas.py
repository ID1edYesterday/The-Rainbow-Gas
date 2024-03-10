import pygame
import sys
import os
sys.path.append(os.getcwd())
from gmap import gmap
from Player import Player
from Agent import Agent

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
PLAYER_SIZE = 50
WHITE = (255, 255, 255)
FPS = 60
#test map

Mymap = gmap()

P = Player()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")



# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Load the player image
P.load_sprite("player.jfif")


# Load the agent image
A = Agent()
A.load_sprite("agent.jfif")




# Main game loop
while True:
    # Handle events
    
    A.logic(P)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    keys = pygame.key.get_pressed()
    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and P.loc_x > 0 and not Mymap.check_collision(P, "left"):
        P.move("left")
    if keys[pygame.K_RIGHT] and P.loc_x + P.width < WIDTH and not Mymap.check_collision(P, "right"):
        P.move("right")
    if keys[pygame.K_UP] and P.loc_y < HEIGHT and not Mymap.check_collision(P, "up"):
        print("up")
        P.move("up")
    if keys[pygame.K_DOWN] and P.loc_y + P.height < HEIGHT and not Mymap.check_collision(P, "down"):
        P.move("down")
    

    # Update the game logic here (if any)

    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the player character
    A.render(screen)

    # Draw the player character
    P.render(screen)

    # Draw the map
    Mymap.render(screen)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)
    
