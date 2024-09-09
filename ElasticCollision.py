import pygame
import sys
import math
import numpy as np
import random

pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Engine")

clock = pygame.time.Clock()

radius = 10

# Circle starting positions
c__x, c__y = width / 2, height / 2

# Velocity and angles
v1 = 5

a1 = -30
a2 = -30

radians_a1 = np.radians(a1)
radians_a2 = np.radians(a2)

x1, x2 = 20, width - 20

y1 = np.abs((height / 2) - (width / 2) * np.tan(radians_a1))
y2 = np.abs((height / 2) - (width / 2) * np.tan(radians_a2))

y1 = max(min(y1, height - radius), radius)
y2 = max(min(y2, height - radius), radius)

m1 = np.tan(radians_a1)
m2 = np.tan(radians_a2)

b1 = y1 - m1 * x1
b2 = y2 - m2 * x2

intersect_x = (b2 - b1) / (m1 - m2)
intersect_y = m1 * intersect_x + b1

d1 = math.sqrt((x1 - intersect_x)**2 + (y1 - intersect_y)**2)
d2 = math.sqrt((x2 - intersect_x)**2 + (y2 - intersect_y)**2)

v2 = v1

v1_x = v1 * np.cos(radians_a1)
v1_y = v1 * np.sin(radians_a1)

v2_x = -1 * v2 * np.cos(radians_a2)
v2_y = v2 * np.sin(radians_a2)

m1 = 5
m2 = 5




# print(v2_x)
# print(v2_y)

# x1__vals = np.linspace(0, c__x, 200)
# x2__vals = np.linspace(width, c__x, 200)

# def returnY1(x):
#     m =  (c__y - y1) / (c__x - x1)
#     return m * (x - x1) + y1

# y_vals = returnY1(x1__vals)

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((51, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (0, height / 2), (width,  height / 2), 1)

    x1 += v1_x
    x2 += v2_x

    y1 += v1_y
    y2 += v2_y

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y1) **2)
    if(d <= 6):
        v1_x = -v1_x 
        v2_x = -v2_x 
        v1_y = -v1_y
        v2_y = -v2_y
        print("collision")

    if x1 - radius <= 0 or x1 + radius >= width:  
        v1_x = -v1_x
    if y1 - radius <= 0 or y1 + radius >= height:  
        v1_y = -v1_y

    if x2 - radius <= 0 or x2 + radius >= width:  
        v2_x = -v2_x
    if y2 - radius <= 0 or y2 + radius >= height:  
        v2_y = -v2_y
    
    pygame.draw.circle(screen, (0, 0, 0), (x1, y1), radius)
    pygame.draw.circle(screen, (0, 0, 0), (x2, y2), radius)

    pygame.display.flip()