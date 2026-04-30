import pygame
import random
import os

class AdjectiveLoader:
    def __init__(self, path): 
        self.path = path
        self.load()

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Missing file: {self.path}")
        with open(self.path, encoding="utf-8") as file:
                  self._items = [line.strip() for line in file if line.strip()]
    
    
def main():
    human_personality = AdjectiveLoader('human_personality.txt').load()
    human_occupation = AdjectiveLoader('human_occupation.txt').load()
    human_size = AdjectiveLoader('human_height-size.txt').load()
    environment_mood = AdjectiveLoader('environment_mood.txt').load()
    environment_size = AdjectiveLoader('environment_size.txt').load()
    environment_setting = AdjectiveLoader('environment_setting.txt').load()

  
    #initialized window code below
    #pygame.init()
    #pygame.display.set_caption("Art Idea Generator")
    #resolution = (1000, 800)
    #screen = pygame.display.set_mode(resolution)
    #running = True
    #while running:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            running = False
    #    black = pygame.Color (0, 0, 0)
    #    screen.fill(black)
    #    pygame.display.flip()
    #pygame.quit()

if __name__ == "__main__":
    main()