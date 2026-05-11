import pygame
import random
import os
class Foundations:
    adj_files = {"human_personality": ('human_personality.txt'),
                "human_occupation": ('human_occupation.txt'), 
                "human_height-size": ('human_height-size.txt'),
                "environment_mood": ('environment_mood.txt'), 
                "environment_size": ('environment_size.txt'), 
                "environment_setting": ('environment_setting.txt')}

class AdjectiveLoader:
    def __init__(self, path): 
        self.path = path
        self.data = {key: self._load(value[0], value[1]) for key, value in path.items()}

    def _load(self, path, set):
        try:
            if not os.path.exists(path):
                return [set]
            with open(path, encoding="utf-8") as file:
                items = [line.strip() for line in file if line.strip()]
            return items or [set]
        except Exception as error:
            print(f"There was an error with {self.path}: {error}")
    
    def get(self, key, set=None):
        return self.data.get(key, set or [])

class Palette:
   def __init__(self, n_colors=3):
       self.count = int(n_colors)

   def _random_hex(self):
       return "#{:02x}{:02x}{:02x}".format(random.randint(0,255), random.randint(0,255)
                                           , random.randint(0,255))
   
   def generate(self):
       return [self._random_hex() for _ in range(self.count)]

   def palette_amount():
       sizes = {"3":3, "4":4,"5":5}
       while True:
           choice = input("Choose a palette size between 3 and 5!: ").strip()
           if choice in sizes:
               return sizes[choice]
           print("Sorry! Please choose a number between 3 and 5!")
                         
class HumanPrompt:
    def __init__(self, human_personality, human_occupation, human_size):
        self.human_personality = human_personality or []
        self.human_occupation = human_occupation or []
        self.human_size = human_size or []
    
    def random_prompt(self, palette):
        h_persona = random.choice(self.human_personality)
        h_occupation = random.choice(self.human_occupation)
        h_size = random.choice(self.human_size)
        colors = ",".join(palette)
        return f"Human: {h_size} {h_persona} {h_occupation}; Palette: {colors}\n"
    
class EnvironmentPrompt:
    def __init__(self, environment_mood, environment_size, environment_setting):
        self.environment_mood = environment_mood or []
        self.environment_size = environment_size or []
        self.environment_setting = environment_setting or []

    def random_prompt(self, palette):
        e_mood = random.choice(self.environment_mood)
        e_size = random.choice(self.environment_size) 
        e_setting = random.choice(self.environment_setting)
        colors = ",".join(palette)
        return f"Environment: {e_size} {e_mood} {e_setting}; Palette: {colors}\n"

class PromptGenerator:
    def __init__(self, human_prompt, environment_prompt, palette_gen):
        self.human_prompt = human_prompt
        self.environment_prompt = environment_prompt
        self.palette_gen = palette_gen

    def generate(self, prompt):
        palette = self.palette_gen.generate()
        if prompt.lower().startswith("h"):
            return self.human_prompt.random_prompt(palette)
        return self.environment_prompt.random_prompt(palette)

    def safe_load(path):
        return AdjectiveLoader(path)


def main():
    pygame.init()
    pygame.display.set_caption("Art Idea Generator")
    resolution = (1000, 800)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color (0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()