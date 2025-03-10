from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position ,self.radius)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_offset = random.uniform(20,50)
        angle1 = self.velocity.rotate(angle_offset)
        angle2 = self.velocity.rotate(-angle_offset)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid1.velocity = angle1*1.2
        asteroid2.velocity = angle2*1.2

        