import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector")

# Define the colors we will use in RGB format
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Set up the player and coin
player_size = 50
player_pos = [screen_width/2, screen_height-2*player_size]
coin_size = 30
coin_pos = [random.randint(0, screen_width-coin_size), 0]
coin_list = [coin_pos]

# Set up the game clock
clock = pygame.time.Clock()

# Set up the score
score = 0
font = pygame.font.SysFont(None, 40)

# Define functions to draw the player, coin, and score
def draw_player():
    pygame.draw.rect(screen, white, [player_pos[0], player_pos[1], player_size, player_size])

def draw_coin(coin_list):
    for coin_pos in coin_list:
        pygame.draw.rect(screen, yellow, [coin_pos[0], coin_pos[1], coin_size, coin_size])

def update_coin_positions(coin_list):
    for idx, coin_pos in enumerate(coin_list):
        if coin_pos[1] >= 0 and coin_pos[1] < screen_height:
            coin_pos[1] += 10
        else:
            coin_list.pop(idx)

def add_coin(coin_list):
    coin_pos = [random.randint(0, screen_width-coin_size), 0]
    coin_list.append(coin_pos)

def collision_detection(player_pos, coin_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    
    c_x = coin_pos[0]
    c_y = coin_pos[1]
    
    if (c_x >= p_x and c_x < (p_x + player_size)) or (p_x >= c_x and p_x < (c_x + coin_size)):
        if (c_y >= p_y and c_y < (p_y + player_size)) or (p_y >= c_y and p_y < (c_y + coin_size)):
            return True
    return False

def display_score(score):
    score_text = "Score: " + str(score)
    score_display = font.render(score_text, True, white)
    screen.blit(score_display, [0, 0])

# Main game loop
game_over = False

while not game_over:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # Move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size

    # Update the positions of the coins
    update_coin_positions(coin_list)

    # Add a
