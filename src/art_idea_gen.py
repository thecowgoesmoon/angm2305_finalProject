import pygame
import random
import os

class AdjectiveLoader:
    def __init__(self, path): 
        self.path = path
        self._items = self.load()

    def load(self):
        items = []
        try:
            if os.path.exists(self.path):
                with open(self.path, encoding="utf-8") as file:
                  items = [line.strip() for line in file if line.strip()]
            else:
                items = []
        except Exception as e:
            print(f"There was an error with {self.path}: {e}")
            items = []
        return items

    def randomize(self):
        if not self._items:
            return None
        return random.choice(self._items)
    
       
class Palette:
   def __init__(self, n_colors=3):
       self.count = int(n_colors)

   def _random_hex(self):
       return "#{:02x}{:02x}{:02x}".format(random.randint(0,255), random.randint(0,255)
                                           , random.randint(0,255))
   
   def generate(self):
       return [self._random_hex() for _ in range(self.count)]
   
   def print_palette(self):
       palette = self.generate()
       print(f"Color palette: {palette}")


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
    palette_gen = Palette(n_colors=3)
    generator = PromptGenerator(human_prompt, environment_prompt, palette_gen)

    while True:
        choice = input("Click 'h' (human) or 'e' (environment) for a prompt, and 'p' to set your palette size! (Press 'q' to quit!): ").strip().lower()
        if choice == "q":
            break
        if choice == "p":
            new_size = Palette.palette_amount()
            palette_gen = Palette(n_colors=new_size)
            generator.palette_gen = palette_gen
            print(f"Palette size set to {palette_gen.count}!")
            continue
        if choice == "h":
                print(generator.generate("human_prompt"))
                continue
        if choice == "e":
            print(generator.generate("environment_prompt"))
            continue
        print("Sorry! Please hit 'h' (human), 'e' (environment), or 'q' (quit) to continue!")

    #initialized window code below
   # pygame.init()
   # pygame.display.set_caption("Art Idea Generator")
   # resolution = (1000, 800)
   # screen = pygame.display.set_mode(resolution)
   # running = True
   # while running:
   #     for event in pygame.event.get():
   #         if event.type == pygame.QUIT:
   #             running = False
   #     black = pygame.Color (0, 0, 0)
   #     screen.fill(black)
   #     pygame.display.flip()
   # pygame.quit()

if __name__ == "__main__":
    main()