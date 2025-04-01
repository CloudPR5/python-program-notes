import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowstorm Effect")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Snowflake class
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-100, HEIGHT)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-100, -10)  # Reset to top of screen
            self.x = random.randint(0, WIDTH)
        
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# Create a list of snowflakes
snowflakes = [Snowflake() for _ in range(200)]  # You can adjust the number of snowflakes

# Main loop
running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw each snowflake
    for snowflake in snowflakes:
        snowflake.fall()

    # Update the display
    pygame.display.flip()
    
    # Set frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
