import pygame
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Replace these values with your integer data
sensor_values = [30, 50, 75]

def create_and_save_3d_bar_graph(values, output_path='bar_graph.png'):
    # Set the figure size based on your desired dimensions
    fig = plt.figure(figsize=(8, 4.8))
    ax = fig.add_subplot(111, projection='3d')

    # Define colors for each bar
    colors = ['red', 'blue', 'gray']

    # Create a 3D bar graph
    x = range(len(values))
    y = [0] * len(values)
    z = values
    dx = dy = 0.5  # Width of the bars
    dz = 0
    
    #coloring the bars individually
    for i in range(len(values)):
        ax.bar3d(x[i], y[i], dz, dx, dy, z[i], color=colors[i], edgecolor='black')

    # Set the viewing angle
    ax.view_init(elev=10, azim=80)

    # Set labels and title
    ax.set_xlabel('Sensor')
    #ax.set_ylabel('Status')
    ax.set_zlabel('Percentage Full')
    ax.set_title('Sub-bin Status')

    # Set the x-axis ticks and labels
    ax.set_xticks(x)
    ax.set_xticklabels([f'Sensor {i+1}' for i in x])

    # Save the plot as an image file
    plt.savefig(output_path)

    # Close the plot to release resources
    plt.close()

    # Return the path of the saved image
    return os.path.abspath(output_path)

# Call the function to create and save the 3D bar graph
saved_image_path = create_and_save_3d_bar_graph(sensor_values)

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
    logo_path = saved_image_path

    # Set the maximum display duration in milliseconds
    max_display_duration_ms = 1000000  # Adjust as needed

    # Call the display_logo function with the logo path and duration
    display_logo(logo_path, max_display_duration_ms)
