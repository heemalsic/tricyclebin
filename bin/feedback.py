import pygame
import sys
import subprocess
from pygame.locals import *


def display_options(screen):
    # Display bio-degradable and non-bio-degradable options as rectangles with text on the screen
    pygame.draw.rect(screen, (0, 128, 0), (50, 200, 330, 60))  # Green rectangle for bio-degradable
    pygame.draw.rect(screen, (0, 0, 255), (400, 200, 370, 60))  # Blue rectangle for non-bio-degradable

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    # Render text for bio-degradable option
    bio_text = font.render("Bio-degradable", True, (255, 255, 255))
    screen.blit(bio_text, (75, 215))

    # Render text for non-bio-degradable option
    non_bio_text = font.render("Non Bio-degradable", True, (255, 255, 255))
    screen.blit(non_bio_text, (410, 215))

    pygame.display.flip()

def trash_identification_game():
    pygame.init()

    # Initialize the touchscreen
    pygame.mouse.set_visible(True)
    pygame.mouse.set_pos((0, 0))

    # Initialize the display
    screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

    display_options(screen)

    # Wait for user input
    selected_option = None

    while not selected_option:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Check if the user tapped on the bio or non-bio option
                if 50 < x < 330 and 200 < y < 250:
                    selected_option = "Bio-degradable"
                elif 400 < x < 770 and 200 < y < 250:
                    selected_option = "Non Bio-degradable"

    # Provide feedback based on the selected option
    if selected_option == "Bio-degradable":
        subprocess.Popen(["python3", "/home/akash/Desktop/bin/script1.py"])
        print("Correct! It's a bio-degradable trash.")
        # Add logic for rewarding the user (e.g., display coupons)
    else:
        subprocess.Popen(["python3", "/home/akash/Desktop/bin/script2.py"])
        print("Oops! It's a non-bio-degradable trash. The correct answer is Bio-degradable.")

    # Display a thank you message for a brief moment before closing
    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    # Change the font color to "sky deep blue"
    thank_you_text = font.render("Thanks for your feedback!", True, (135, 206, 250))

    screen.blit(thank_you_text, (200, 300))

    # Update the display to show the text
    pygame.display.update()

    # Control the frame rate to update the display consistently
    clock = pygame.time.Clock()
    clock.tick(30)  # Adjust the frame rate if needed (e.g., 30 frames per second)

    # Wait for a short duration (e.g., 2000 milliseconds) before closing
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Run the trash identification game
    trash_identification_game()
