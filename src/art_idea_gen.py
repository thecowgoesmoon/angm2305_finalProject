import pygame
import random
import os

class AdjectiveLoader:
    def __init__(self, path): 
        self.path = path
        self._items = self.load()

    def load(self):
        try:
            with open(self.path, encoding="utf-8") as file:
                  self._items = [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"error w/ {self.path}: {e}")

    def randomize(self):
        if not self._items:
            return None
        return random.choice(self._items)
    
       
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
      
class HumanPrompt:
    def __init__(self, human_personality, human_occupation, human_size):
        self.human_personality = human_personality or []
        self.human_occupation = human_occupation or []
        self.human_size = human_size or []
    
    def random_prompt(self, palette):
        p = random.choice(self.human_personality) if self.human_personality else "blank" 
        o = random.choice(self.human_occupation) if self.human_occupation else "blank"
        hs = random.choice(self.human_size) if self.human_size else "blank"
        colors = ",".join(palette)
        return f"Human: {hs} {p} {o}; Palette: {colors}"
    
class EnvironmentPrompt:
    def __init__(self, environment_mood, environment_size, environment_setting):
        self.environment_mood = environment_mood or []
        self.environment_size = environment_size or []
        self.environment_setting = environment_setting or []

    def random_prompt(self, palette):
        m = random.choice(self.environment_mood) if self.environment_mood else "blank"
        es = random.choice(self.environment_size) if self.environment_size else "blank"
        s = random.choice(self.environment_setting) if self.environment_setting else "blank"
        colors = ",".join(palette)
        return f"Environment: {es} {m} {s}; Palette: {colors}"

class PromptGenerator:
    def __init__(self, human_prompt, environment_prompt, palette_gen):
        self.human_prompt = human_prompt
        self.environment_prompt = environment_prompt
        self.palette_gen = palette_gen

    def generate(self, prompt):
        palette = self.palette_gen.generate() 
        if prompt.lower().startswith("h"):
            return self.human_prompt.random_prompt(palette)
        else: 
            return self.environment_prompt.random_prompt(palette)

    def safe_load(path):
        return AdjectiveLoader(path)._items

def main():
    human_personality = PromptGenerator.safe_load('human_personality.txt')
    human_occupation = PromptGenerator.safe_load('human_occupation.txt')
    human_size = PromptGenerator.safe_load('human_height-size.txt')
    environment_mood = PromptGenerator.safe_load('environment_mood.txt')
    environment_size = PromptGenerator.safe_load('environment_size.txt')
    environment_setting = PromptGenerator.safe_load('environment_setting.txt')

    human_prompt = HumanPrompt(human_personality, human_occupation, human_size)
    environment_prompt = EnvironmentPrompt(environment_mood, environment_size, environment_setting)
    palette_test = Palette(n_colors=3)
    generator = PromptGenerator(human_prompt, environment_prompt, palette_test)

    human_result = generator.generate("human")
    env_result = generator.generate("env")
    print("Generated prompts:")
    print(human_result)
    print(env_result)

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