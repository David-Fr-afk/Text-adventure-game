import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a game window
window = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Lonely warrior")

# Initialize Pygame clock
clock = pygame.time.Clock()

# Set up fonts
font = pygame.font.Font(None, 18)

# Create a list to store console messages
console_messages = []

# Create a game text
game_text = "Welcome to my first game"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((0, 0, 0))  # Set the background color to black

    # Display console messages
    y_offset = 100  # Starting position for console messages
    for message in console_messages:
        message_rendered = font.render(message, True, (255, 255, 255))
        window.blit(message_rendered, (10, y_offset))
        y_offset += 20  # Adjust the spacing between messages

    # Display game text
    game_text_rendered = font.render(game_text, True, (255, 255, 255))
    window.blit(game_text_rendered, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
