import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up the screen width and height
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for controlling game speed
CLOCK = pygame.time.Clock()

# Snake block size and speed
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Fonts
FONT = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = SCORE_FONT.render(f"Your Score: {score}", True, GREEN)
    SCREEN.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(SCREEN, BLUE, [block[0], block[1], block_size, block_size])

def game():
    # Initial position of the snake
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over:

        while game_close:
            SCREEN.fill(BLACK)
            msg = FONT.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            SCREEN.blit(msg, [WIDTH // 6, HEIGHT // 3])
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = BLOCK_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        SCREEN.fill(BLACK)
        pygame.draw.rect(SCREEN, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game()
