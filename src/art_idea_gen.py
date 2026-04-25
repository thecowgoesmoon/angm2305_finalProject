import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Art Idea Generator")
    resolution = (1000, 800)
    screen = pygame.display.set_mode(resolution)
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