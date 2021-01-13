import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

# Declare the colors
orangecolor = (255, 123, 7)
blackcolor = (0, 23, 23)
redcolor = (215, 50, 80)
greencolor = (0, 258, 0)
bluecolor = (50, 153, 213)
# Display Window

display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BATTLESNAKE GAME')  # fix the caption
snake_block = 10
snake_list = []
snake_speed = 15


# Defines the snake's structure
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolor, [x[0], x[1], snake_block, snake_block])


def pythongame():
    game_over = False
    game_end = False
    # co-ordinates of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    # When the snake moves
    x1_change = 0
    y1_change = 0

    # define the length of the snake
    snake_list = []
    length_of_snake = 1

    # the co-ordinates of food element

    foodx = round(random.randrange(0,display_width-snake_block)/10.0) * 10.0
    foody = round(random.randrange(0,display_height-snake_block)/10.0) * 10.0

    while not game_over:
        while game_end == True:
            # For displaying the score
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms",35)
            value = score_font.render("Your Score: " + str(score), True, greencolor)
            dis.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over =True
                    game_end = False # game has been ended

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True

        # updated the co-ordinates with the changed position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis,greencolor,[foodx,foody,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        # When the length of the snake exceeds, delete the snake_list which will end the game
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # When snake hits itself, game ends

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True

        snake(snake_block,snake_list)
        pygame.display.update()

        # when snake hits the food, the length of snake is incremented by 1

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width-snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block)/10.0)* 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

pythongame()
