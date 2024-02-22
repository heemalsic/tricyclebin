import pygame
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import firebase_admin
from firebase_admin import credentials, firestore


# Initialize Firebase with your credentials
cred = credentials.Certificate("/home/akash/Desktop/firebase.json")
firebase_admin.initialize_app(cred)

# Replace these values with your actual Firestore collection and document names
collection_name = 'distance_data' 
document_prefix = 'sensor_data_'

def get_sensor_values():
    db = firestore.client()
    sensor_values = []

    for sensor_num in range(1, 4):  # Assuming you have 3 sensors
        document_name = f'{document_prefix}{sensor_num}'
        doc_ref = db.collection(collection_name).document(document_name)
        data = doc_ref.get().to_dict()
        sensor_data = data.get('distance', 0)
        sensor_values.append(sensor_data)

    return sensor_values

# Replace these values with your integer data
# sensor_values = [30, 50, 75]
total_capacity = 100  # Total capacity of the sub-bins

def create_and_save_individual_pie_charts(values, total_capacity, output_path='individual_pie_charts.png'):
    # Set the figure size based on your desired dimensions
    fig, axs = plt.subplots(1, len(values), figsize=(7, 3))

    for i, value in enumerate(values):
        # Calculate the percentage values
        percentage = value / total_capacity * 100
        empty_percentage = 100 - percentage

        # Create a pie chart
        labels = [f'{percentage:.1f}%', '']  # Display only the percentage as label
        colors = ['red', 'white']
        axs[i].pie([percentage, empty_percentage], labels=labels, colors=colors, autopct='', startangle=90)
        axs[i].set_title(f'Sub-bin {i+1}')

    # Adjust layout to prevent clipping of titles
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig(output_path)

    # Close the plot to release resources
    plt.close()

    # Return the path of the saved image
    return os.path.abspath(output_path)

# Call the function to get sensor values from Firebase
sensor_values = get_sensor_values()

# Call the function to create and save individual pie charts
saved_image_path = create_and_save_individual_pie_charts(sensor_values, total_capacity)

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
