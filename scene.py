import pygame
import physicsObject
from constant import *

class Scene:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.objects = []
        self.objects.append(physicsObject.Circle(50, position=pygame.Vector2(100, 100)))
        self.objects.append(physicsObject.Circle(50, position=pygame.Vector2(250, 100)))
        self.objects.append(physicsObject.Circle(50, position=pygame.Vector2(500, 100)))
        self.objects.append(physicsObject.Circle(50, position=pygame.Vector2(200, 200)))
        self.objects[0].velocity = pygame.Vector2(500, 500)

    def update(self, deltaTime : float, events):
        for object in self.objects:
            object.update(deltaTime)
            if ((object.position.x < 0 and object.velocity.x < 0) or (object.position.x + object.radius * 2 >= self.width and object.velocity.x > 0)):
                object.velocity.x *= -1
            if ((object.position.y < 0 and object.velocity.y < 0) or (object.position.y + object.radius * 2 >= self.height and object.velocity.y > 0)):
                object.velocity.y *= -1
        self.collide()
    
    def render(self, screen : pygame.Surface):
        screen.fill((255, 255, 255))

        for object in self.objects:
            object.render(screen)

    def collide(self):
        for i in range(len(self.objects)-1):
            for j in range(i+1, len(self.objects)):
                object1 = self.objects[i]
                object2 = self.objects[j]
                if (object1.check_collision(object2)):
                    if (type(object1) == physicsObject.Circle and type(object2) == physicsObject.Circle):
                        self.physics_circle_and_circle(object1, object2)
    
    def physics_circle_and_circle(self, object1, object2):
        contact_normal = (object2.center_of_gravity() - object1.center_of_gravity()).normalize()
        
        normal_velocity1 = object1.velocity.dot(contact_normal) * contact_normal
        normal_velocity2 = object2.velocity.dot(contact_normal) * contact_normal

        j = - (normal_velocity1 - normal_velocity2) * (COR + 1) * (object1.mass * object2.mass / (object1.mass + object2.mass))

        object1.velocity += j / object1.mass
        object2.velocity += - j / object2.mass
        print(object1.position, object2.position)