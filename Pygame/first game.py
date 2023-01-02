import pygame

GameWindow = pygame.display.set_mode((1200,500))
# x = pygame.init()
# print(x)

pygame.display.set_caption("MY First Game")

# Game Spacific Variable
ExitGame = False
GameOver = False

while not ExitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ExitGame = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right Arrow key")


pygame.quit()
quit()