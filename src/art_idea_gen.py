import pygame
import random
import os

class AdjectiveLoader:
    def __init__(self, path): 
        self.path = path
        self.items = []
        self.load()

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Missing file: {self.path}")
        with open(self.path, encoding="utf-8") as file:
                  self._items = [line.strip() for line in file if line.strip()]
    
       
class Palette:
   def __init__(self, n_colors=3):
       self.count = max(1, int(n_colors))

   def _random_hex(self):
       return "#{:02x}{:02x}{:02x}".format(random.randint(0,255), random.randint(0,255)
                                           , random.randint(0,255))
   
   def generate(self):
       return [self._random_hex() for _ in range(self.count)]
   
   def print_palette(self):
       palette = self.generate()
       print(f"Color palette: {palette}")
      
       

def main():
    human_personality = AdjectiveLoader('human_personality.txt').load()
    human_occupation = AdjectiveLoader('human_occupation.txt').load()
    human_size = AdjectiveLoader('human_height-size.txt').load()
    environment_mood = AdjectiveLoader('environment_mood.txt').load()
    environment_size = AdjectiveLoader('environment_size.txt').load()
    environment_setting = AdjectiveLoader('environment_setting.txt').load()

    palette_test = Palette(n_colors=3)
    for i in range(1):
        palette = palette_test.print_palette()
        return palette


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