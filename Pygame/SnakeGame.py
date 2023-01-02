import pygame,random

ScreenWidth = 800
ScreenHeight = 400
GameWindow = pygame.display.set_mode((ScreenWidth,ScreenHeight))

pygame.display.set_caption("Snake Game")

ExitGame = False 
GameOver = False
SnakeX = 45
SnakeY = 65
SnakeSize = 10
Black = (0)
Red = (255,0,0)
fps = 30
Score = 0
VelocityX = 0
VelocityY = 0

FoodX = random.randint(20,ScreenWidth/2)
FoodY = random.randint(20,ScreenHeight/2)
InitalVal = 5

Clock = pygame.time.Clock()
while not ExitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ExitGame = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                VelocityX = InitalVal
                VelocityY = 0
            elif event.key == pygame.K_DOWN:
                VelocityY = InitalVal
                VelocityX = 0
            elif event.key == pygame.K_LEFT:
                VelocityX = -InitalVal
                VelocityY = 0
            elif event.key == pygame.K_UP:
                VelocityY = -InitalVal
                VelocityX = 0

    SnakeX += VelocityX
    SnakeY += VelocityY

    if abs(SnakeX - FoodX)<4 and abs(SnakeY - SnakeY)<4:
        Score += 1
        print("Score : ",Score)
        FoodX = random.randint(20,ScreenWidth*3/4)
        FoodY = random.randint(20,ScreenHeight*3/4)

    GameWindow.fill(color="White")
    pygame.draw.rect(GameWindow,Red,[FoodX,FoodY,SnakeSize,SnakeSize])
    pygame.draw.rect(GameWindow,Black,[SnakeX ,SnakeY ,SnakeSize ,SnakeSize])
    pygame.display.update()
    Clock.tick(fps)
        
        

pygame.quit()
quit()