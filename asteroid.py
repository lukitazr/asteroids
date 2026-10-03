from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS): return

        log_event("asteroid_split")

        angle: float = random.uniform(20, 50)

        mini1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        mini2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)

        mini1.velocity = self.velocity.rotate(angle) * 1.2
        mini2.velocity = self.velocity.rotate(-angle) * 1.2
        
