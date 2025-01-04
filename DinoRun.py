import pygame
import random

# Inicializa o pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configuração da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dino Run')

# FPS
clock = pygame.time.Clock()
FPS = 60

# Classe Dino
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 70
        self.velocity = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == SCREEN_HEIGHT:
            self.velocity = -15

        self.velocity += 1  # Gravidade
        self.rect.y += self.velocity

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0


# Classe Obstáculo
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 40

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH


# Função principal do jogo
def game_loop():
    dino = Dino()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(dino)

    obstacles = pygame.sprite.Group()
    for _ in range(3):
        obstacle = Obstacle()
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    score = 0
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        if pygame.sprite.spritecollideany(dino, obstacles):
            running = False  # Finaliza o jogo em caso de colisão

        score += 1

        screen.fill(WHITE)
        all_sprites.draw(screen)

        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()


# Inicia o jogo
game_loop()
