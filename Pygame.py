import pygame
pygame.init()

# Set up the game window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pacman Game")

# Pacman properties
pacman_pos = [200, 200]
pacman_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_pos[1] -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_pos[1] += pacman_speed
    if keys[pygame.K_LEFT]:
        pacman_pos[0] -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_pos[0] += pacman_speed

    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.circle(screen, (255, 255, 0), pacman_pos, 20)  # Draw Pacman
    pygame.display.flip()  # Update the display

pygame.quit()
