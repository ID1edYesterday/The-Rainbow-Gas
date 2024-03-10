import pygame
from tensorflow import keras
import numpy as np

class Agent:
    
    def __init__(self):
        self.name = ""
        self.health = 100
        self.speed = 10
        self.has_gas = False
        self.loc_x = 0
        self.loc_y = 0
        self.sprite = None
        self.width = 50
        self.height = 50
        
        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(4,)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(4, activation='softmax')
        ])
    
    def logic(self, P):
        # Create a small neural network to decide where to move next using keras
        # Train the model using the data
        
        # Compile the model
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        
        # Prepare the input data
        player_location = np.array(P)
        input_data = np.expand_dims(player_location, axis=0)
        
        # Make predictions using the model
      
        player_data = [P.loc_x, P.loc_y, self.loc_x, self.loc_y]  # Assuming Player has x and y attributes
        player_location = np.array(player_data)
        input_data = np.expand_dims(player_location, axis=0)
        

        predictions = self.model.predict(input_data)
        
        # Get the index of the predicted action
        action_index = np.argmax(predictions)
        
        # Map the action index to the corresponding direction
        directions = ["up", "down", "left", "right"]
        direction = directions[action_index]
        
        # Move in the predicted direction
        self.move(direction)
        
        # train the model check if it actually moved towards the player or not 
        #and then train the model
        # Train the model using the data
        # Prepare the input data
        agent_data = [self.loc_x, self.loc_y]
        agent_location = np.array(agent_data)
        input_data = np.expand_dims(agent_location, axis=0)
        # use target data that would get us closer to the player
        
        
        distance_from_player = np.linalg.norm(target_data) # Calculate the distance from the player
        
        #check if the move of the neural network got us closer or further from the player
        
        
        
        target_location = np.array(target_data)
        target_data = np.expand_dims(target_location, axis=0)
        self.model.fit(input_data, target_data, epochs=2)
        
    

    def load_sprite(self, file_path):
        self.sprite = pygame.image.load(file_path)
        
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

    def render(self, screen):
         if self.sprite is not None:
            screen.blit(self.sprite, (self.loc_x, self.loc_y))
         
    def move(self, direction):
        if direction == "up":
            self.loc_y += 1
        elif direction == "down":
            self.loc_y -= 1
        elif direction == "left":
            self.loc_x -= 1
        elif direction == "right":
            self.loc_x += 1

    def generate_gas(self):
        self.has_gas = True

    def use_gas(self):
        if self.has_gas:
            # Code to use the gas
            self.has_gas = False
        

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You Won")

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Speed: {self.speed}")
        print(f"Location: ({self.loc_x}, {self.loc_y})")
        print(f"Has Gas: {self.has_gas}")
        print(f"Map: {self.map}")