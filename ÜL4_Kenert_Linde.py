import pygame
import random

# Mängu akna suurus
WIDTH = 640
HEIGHT = 480

# Värvid
WHITE = (255, 255, 255)

# Autode kiirus
CAR_SPEED = 5

# Funktsioon autode loomiseks
def create_car(image_path):
    car = pygame.image.load(image_path).convert_alpha()
    car = pygame.transform.scale(car, (30, 50))
    return car, car.get_rect()

# Funktsioon teksti joonistamiseks ekraanile
def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Mängufunktsioon
def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Game")
    clock = pygame.time.Clock()

    # Hinnanguline skoor
    score = 0

    # Teksti font
    font = pygame.font.Font(None, 36)

    # Taustapilt
    background = pygame.image.load("bg_rally.jpg").convert()

    # Punane auto
    red_car, red_car_rect = create_car("f1_red.png")
    red_car_rect.midbottom = (WIDTH // 2, HEIGHT - 10)

    # Siniste autode loomine
    blue_cars = []
    for _ in range(5):
        blue_car, blue_car_rect = create_car("f1_blue.png")
        blue_car_rect.left = random.randint(180, 460)  # Tee laius: 460 - 180 = 280
        blue_car_rect.top = random.randint(-HEIGHT, 0)
        blue_cars.append((blue_car, blue_car_rect))

    # Mängutsükkel
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Liiguta siniseid autosid ja uuenda skoori
        for i, (blue_car, blue_car_rect) in enumerate(blue_cars):
            blue_car_rect.y += CAR_SPEED
            if blue_car_rect.top > HEIGHT:
                blue_car_rect.top = random.randint(-HEIGHT, 0)
                score += 1
            if blue_car_rect.colliderect(red_car_rect):
                score -= 1
            blue_cars[i] = (blue_car, blue_car_rect)

        # Joonista kõik elemendid ekraanile
        screen.blit(background, (0, 0))
        screen.blit(red_car, red_car_rect)
        for blue_car, blue_car_rect in blue_cars:
            screen.blit(blue_car, blue_car_rect)

        # Joonista skoor
        draw_text(screen, f"Score: {score}", font, WHITE, WIDTH // 2, 10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Alusta mängu
game()
