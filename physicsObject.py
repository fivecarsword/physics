import pygame

class Circle:
    def __init__(self, radius : float, color = (100, 100, 100), position = pygame.Vector2(), mass = 10) -> None:
        self.radius = radius
        self.color = color
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.mass = mass
    
    def update(self, deltaTime : float):
        self.velocity += pygame.Vector2(0, 1000) * deltaTime
        self.position += self.velocity * deltaTime

    def render(self, screen : pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position + pygame.Vector2(self.radius, self.radius), self.radius)

    def center_of_gravity(self) -> pygame.Vector2:
        return self.position + pygame.Vector2(self.radius, self.radius)

    def check_collision(self, other) -> bool:
        if (type(other) == Circle):
            if ((self.center_of_gravity() - other.center_of_gravity()).length() <= self.radius + other.radius):
                return True
            else:
                return False