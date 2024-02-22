import pygame
import sys

def display_logo(image_path, max_display_duration_ms):
    # Initialize Pygame and the display
    pygame.init()

    # Set the display dimensions based on your actual display resolution
    display_width, display_height = 800, 480
    screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    
    
    # Load the logo image
    logo = pygame.image.load(image_path)
    

    # Resize the logo to fit the screen
    logo = pygame.transform.scale(logo, (display_width, display_height))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Blit the logo onto the screen
    screen.blit(logo, (0, 0))

    # Update the display
    pygame.display.flip()

    # Get the start time
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < max_display_duration_ms:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                # Exit the loop if there is any user input
                pygame.quit()
                sys.exit()

        # Add a small delay to reduce CPU usage
        pygame.time.delay(10)

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Specify the path to your logo image
    logo_path = "/home/akash/Desktop/sih8.png"

    # Set the maximum display duration in milliseconds
    max_display_duration_ms = 10000  # Adjust as needed

    # Call the display_logo function with the logo path and duration
    display_logo(logo_path, max_display_duration_ms)