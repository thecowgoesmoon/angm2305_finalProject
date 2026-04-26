import pygame

class AdjectiveLoader:
    def __init__(self, path): 
        self.path = path

    def load(self):
        with open(self.path, encoding='utf-8') as file:
            return[l.strip() for l in file if l.strip()]
       

def main():
    human_personality = AdjectiveLoader('human_personality.txt').load()
    human_occupation = AdjectiveLoader('human_occupation.txt').load()
    human_size = AdjectiveLoader('human_height-size.txt').load()
    environment_mood = AdjectiveLoader('environment_mood.txt').load()
    environment_size = AdjectiveLoader('environment_size.txt').load()
    environment_setting = AdjectiveLoader('environment_setting.txt').load()

    print(human_personality)
    print(human_occupation)
    print(human_size)
    print(environment_mood)
    print(environment_size)
    print(environment_setting)

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