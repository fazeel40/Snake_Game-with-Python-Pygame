import random
import pygame
pygame.mixer.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen_height = 900
screen_width = 500
pygame.init()
clock = pygame.time.Clock()
gamewindow = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("SnakeGameWithFazeel")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
bgimg = pygame.image.load("Images\\bg.jpg")
bgimg = pygame.transform.scale(
    bgimg, (screen_height, screen_width)).convert_alpha()
bgimgw = pygame.image.load("Images\start.png")
bgimgw = pygame.transform.scale(
    bgimgw, (screen_height, screen_width)).convert_alpha()
bgimgg = pygame.image.load("Images\gameover.png")
bgimgg = pygame.transform.scale(
    bgimgg, (screen_height, screen_width)).convert_alpha()
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plotsnake(gamewindow, color, snk_list, snake_size):
    for snake_x, snake_y in snk_list:
        pygame.draw.rect(gamewindow, color, [
                         snake_x, snake_y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimgw, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load(
                        "Music\music.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():
    exit_game = False
    game_over = False

    score = 1
    snake_x = 45
    snake_y = 55
    snake_size = 30
    snk_list = []
    snk_len = 1
    fps = 90
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, 500/2)
    food_y = random.randint(20, 900/2)
    while not exit_game:
        with open("hiscore.txt", "w") as f:
            h = f.write(str(score*10))
            if(score*10 > h):
                f.write(str(score*10))
        if(game_over):
            gamewindow.fill(white)
            gamewindow.blit(bgimgg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -5
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 5
                    if(snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height):
                        pygame.mixer.music.load(
                            "Music\gameover.mp3")
                        pygame.mixer.music.play()
                        game_over = True

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x) < 30 and abs(snake_y-food_y) < 30:
                score += 1
                food_x = random.randint(20, 500/2)
                food_y = random.randint(20, 900/2)
                snk_len += 5
            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("Score: "+str(score*10), red, 5, 5)
            pygame.draw.rect(gamewindow, black,
                             (snake_x, snake_y, snake_size, snake_size))
            pygame.draw.rect(
                gamewindow, red, (food_x, food_y, snake_size, snake_size))

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_len:
                del snk_list[0]
            if head in snk_list[:-1]:
                pygame.mixer.music.load(
                    "Music\him.wav")
                pygame.mixer.music.play()
                game_over = True
            plotsnake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
