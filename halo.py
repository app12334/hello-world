import pygame
import random

pygame.init()

# Game Specific variables
width = 800
height = 600
run = True

# Game window and caption and icon
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")
pyimg = pygame.image.load("ufo.png")  # Load image
pygame.display.set_icon(pyimg)

# Player
playerImg = pygame.image.load("playerimg.png")
playerX = 370
playerY = 420
playerX_change = 0

# Enemy
enemyimg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(40, 70)
enemyX_change = 0.3
enemyY_change = 30

# Bullet
# ready - you cant see teh bullet
# fire - you can see the bullet

bulletimg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 420
bulletY_change = 0.8
bullet_state = "ready"


def player_img(x, y):
    screen.blit(playerImg, (x, y))


def enemy_img(a, b):
    screen.blit(enemyimg, (a, b))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_SPACE:

                if bullet_state is "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
                    pygame.display.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = 0

    # For player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerX += playerX_change

    # For enemy
    if enemyX <= 0:
        enemyX_change += 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change -= 0.3
        enemyY += enemyY_change
    enemyX += enemyX_change

    if bulletY <= 0:
        bulletY = 420
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    player_img(playerX, playerY)
    enemy_img(enemyX, enemyY)
    pygame.display.update()
quit()
