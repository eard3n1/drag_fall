from properties import Properties
from config import *
import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 30)
    clock = pygame.time.Clock()

    circle = Properties(GROUND, X, Y, MASS, ACCELERATION, VELOCITY, APPLY_FORCE, GROUND_ABSORPTION, WIND_RESISTANCE)

    run = True
    while run:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                circle.apply_upward_force()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                circle.apply_downward_force()

        circle.advance(dt)

        win.fill((219, 252, 255))
        pygame.draw.circle(win, (255, 100, 100), (int(circle.x), int(circle.y)), 50)
        pygame.draw.line(win, (100, 100, 100), (0, GROUND + 50), (WIDTH, GROUND + 50), 10)

        altitude = font.render(f"Altitude: {round((abs(circle.y - GROUND))/100)} m", True, (255, 255, 255), (0, 0, 0))
        win.blit(altitude, (10, 10))

        vel_text = font.render(f"Velocity: {round(abs(circle.velocity))} m/s", True, (255, 255, 255), (0, 0, 0))
        win.blit(vel_text, (10, 35))

        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()