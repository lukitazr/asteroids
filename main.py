import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    x: float = SCREEN_WIDTH / 2
    y: float = SCREEN_HEIGHT / 2
    player = Player(x, y)

    Shot.containers = (shots, updatable, drawable)

    dt: float = 0.0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for a in asteroids:
            if (a.collides_with(player)): 
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if (s.collides_with(a)):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000 
        
if __name__ == "__main__":
    main()
