
import pygame 
import sys
import math
import numpy as np
import pygame.draw_py

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Engine")

# Setting up font
font = pygame.font.Font(None, 21)
color = (0, 0, 0)

running = True

# Equation of Trajectory
x_vals = np.linspace(0, 300, 200)
theta = 60 

theta_rad = np.radians(theta)

g = 10
v0 = 80

def trajectory(x, theta, g, v0):
    return x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta) ** 2)

y = trajectory(x_vals, theta_rad, g, v0)

x_inter = np.interp(x_vals, (x_vals.min(), x_vals.max()), (0, width - 50))
y_inter = np.interp(y, (y.min(), y.max()), (height - 50, 50))

print(x_inter)
print(y_inter)

start = False

clock = pygame.time.Clock()
index = 0

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True

    screen.fill((51, 255, 255))

    if start == True:
        if index < len(x_vals) - 1:
            x = x_inter[index]
            y1 = y_inter[index]

            pygame.draw.circle(screen, (0, 0, 0), (x, y1), 10)
            
            text_surface_x = font.render(f"X: {x}", True, color)
            text_surface_y = font.render(f"Y: {y1}", True, color)

            text_rect_x = text_surface_x.get_rect(center=(650, 40))
            text_rect_y = text_surface_y.get_rect(center=(650, 60))

            screen.blit(text_surface_x, text_rect_x)
            screen.blit(text_surface_y, text_rect_y)

            index += 1
        else:
            start = False

    pygame.display.flip()

pygame.quit()