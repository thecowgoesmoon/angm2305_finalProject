import pygame
import random
import os
class Foundations():
    active_button = (204, 255, 204)
    button_color = (92, 147, 255)
    text_color = (255, 255, 255)
   
adj_files = {"human_personality": ('human_personality.txt'),
                "human_occupation": ('human_occupation.txt'), 
                "human_height-size": ('human_height-size.txt'),
                "environment_mood": ('environment_mood.txt'), 
                "environment_size": ('environment_size.txt'), 
                "environment_setting": ('environment_setting.txt')}

class AdjectiveLoader():
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

class Palette():
   def __init__(self, n_colors=3):
       self.count = max(1, int(n_colors))

   def random_hex(self):
       return "#{:02x}{:02x}{:02x}".format(random.randint(0,255), random.randint(0,255), random.randint(0,255))
   
   def generate(self):
       return [self.random_hex() for _ in range(self.count)]

   def palette_amount():
       sizes = {"3":3, "4":4,"5":5}
       while True:
           choice = input("Choose a palette size between 3 and 5!: ").strip()
           if choice in sizes:
               return sizes[choice]
           print("Sorry! Please choose a number between 3 and 5!")
   def hex_to_rgb(hex):
       hex = hex.lstrip("#")
       return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
class Prompts():   
    class HumanPrompt:
        def __init__(self, human_personality, human_occupation, human_size):
            self.human_personality = human_personality or []
            self.human_occupation = human_occupation or []
            self.human_size = human_size or []
    
        def random_prompt(self, palette):
            h_persona = random.choice(self.human_personality)
            h_occupation = random.choice(self.human_occupation)
            h_size = random.choice(self.human_size)
            colors = ", ".join(palette)
            return f"Character: {h_size} {h_persona} {h_occupation}\n Color Palette: {colors}\n"
    
    class EnvironmentPrompt:
        def __init__(self, environment_mood, environment_size, environment_setting):
            self.environment_mood = environment_mood or []
            self.environment_size = environment_size or []
            self.environment_setting = environment_setting or []

        def random_prompt(self, palette):
            e_mood = random.choice(self.environment_mood)
            e_size = random.choice(self.environment_size) 
            e_setting = random.choice(self.environment_setting)
            colors = ", ".join(palette)
            return f"Environment: {e_size} {e_mood} {e_setting}\n Color Palette: {colors}\n"

class PromptGenerator():
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
class UILayout():
    class Button:
        def __init__(self, rect, text, callback=None, font=None):
            self.rect = pygame.Rect(rect)
            self.text = text
            self.callback = callback
            self.active = False
            self.font = font

        def draw(self, surf):
            active_button = Foundations.active_button
            button_color = Foundations.button_color
            text_color = Foundations.text_color

            color = active_button if self.active else button_color
            pygame.draw.rect(surf, color, self.rect, border_radius=6)
            text = self.font.render(self.text, True, text_color)
            text_shape = text.get_rect(center=self.rect.center)
            surf.blit(text, text_shape)

        def mouse(self, event):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.rect.collidepoint(event.pos):
                        if self.callback:
                            self.callback()
                        return True
                    return False
                
    class IdeaGenerator():
        def __init__(self):
           self.loader = AdjectiveLoader(adj_files)
           self.palette_gen = Palette()
           self.prompts = Prompts

           self.palette_size = 3
           self.current_palette = self.palette_gen.palette_amount(self.palette_size)
           self.current_prompt = "prompt"
           self.base_text = "Choose between a character or environment prompt!"

           self.human_prompt = self.prompts.HumanPrompt(self.loader.get("human_personality"),
                                                        self.loader.get("human_height-size"),
                                                        self.loader.get("human_occupation"))
           
           self.environment_prompt = self.prompts.EnvironmentPrompt(self.loader.get("environment_mood"),
                                                                    self.loader.get("environment_size"),
                                                                    self.loader.get("environment_setting"))
           self.running = True

        def set_palette_size(self, n_colors):
            self.palette_size = n_colors
            self.generate_palette()

        def set_prompt_human(self):
            self.current_prompt = "human"

        def set_prompt_environment(self):
            self.current_prompt = "environment"

        def generate_palette(self):
            self.current_palette = self.palette_gen.palette_amount(self.palette_size)

        def generate_prompt(self):
            self.generate_palette()
            if self.current_prompt == "human":
                self.base_text = self.human_prompt.random_prompt(self.current_palette)
            else:
                self.base_text = self.environment_prompt.random_prompt(self.current_palette)

        def _create_buttons(self):
            font = self.font
            self.but_3 = UILayout.Button((20, 20, 80, 36), "3 Colors", lambda:
                                         self.set_palette_size(3), font=font)
            self.but_4 = UILayout.Button((110, 20, 80, 36), "4 Colors", lambda:
                                         self.set_palette_size(4), font=font)
            self.but_5 = UILayout.Button((200, 20, 80, 36), "5 Colors", lambda: 
                                         self.set_palette_size(5), font=font)
            self.but_human = UILayout.Button((320, 20, 100, 36), "Human", self.set_prompt_human,
                                             font=font)
            self.but_environment = UILayout.Button((430, 20, 100, 36), "Environment", 
                                                   self.set_prompt_environment, font=font)
            self.but_pal_gen = UILayout.Button((550, 20, 100, 36), "Generate Palette?", self.generate_palette, font=font)
            self.but_prompt_gen = UILayout.Button((660, 20, 120, 36), "Generate Prompt?", self.generate_prompt, font=font)
            self.buttons.extends([self.but_3, self.but_4, self.but_5,
                                  self.but_human, self.but_environment,
                                  self.but_pal_gen, self.but_prompt_gen])
        def update_button_states(self):
            self.but_3.active = (self.palette_size == 3)
            self.but_4.active = (self.palette_size == 4)
            self.but_5.active = (self.palette_size == 5)
            self.but_human.active = (self.current_prompt == "human")
            self.but_environment.active = (self.current_prompt == "environment")

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