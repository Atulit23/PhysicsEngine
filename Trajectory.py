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
theta = 30 

theta_rad = np.radians(theta)

g = 10
v0 = 10
dt = 0.1
air_resistance_coefficient = 4
air_density = 8.225
drag_coefficient = 0.99
area_object = 10
wind_speed = 10

def trajectory(x, theta, g, v0):
    return x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta) ** 2)


def calculate_air_resistance(vx,vy,drag_coefficient,air_density,area_object):
    speed = np.sqrt(vx**2 + vy**2)
    drag_force = 0.5 * drag_coefficient * air_density * area_object * speed**2
    drag_x = drag_force * (vx / speed)
    drag_y = drag_force * (vy / speed)
    return drag_x,drag_y

start = False

clock = pygame.time.Clock()
index = 0
vx = v0 * np.cos(theta_rad)
vy = v0 * np.sin(theta_rad)
air_resistance = True

if air_resistance:
    drag_x, drag_y = calculate_air_resistance(vx,vy,drag_coefficient,air_density,area_object)
else:
    drag_x,drag_y = 0,0

vx += wind_speed - drag_x * dt
vy += g * dt - drag_y * dt

v0 = np.sqrt(vx**2 + vy**2)

y = trajectory(x_vals, theta_rad, g, v0)

x_inter = np.interp(x_vals, (x_vals.min(), x_vals.max()), (0, width - 50))
y_inter = np.interp(y, (y.min(), y.max()), (height - 50, 50))

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