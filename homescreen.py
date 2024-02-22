# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# # from PyQt5.QtCore import Qt  # Import the Qt module

# # class HomeScreen(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Home Screen")
# #         self.setGeometry(0, 0, 800, 480)  # Set the initial window size (you can adjust this)

# #         # Create buttons
# #         bin_stats_button = QPushButton("Bin Stats", self)
# #         bin_stats_button.setFixedSize(200, 100)  # Set the fixed size (width, height)

# #         sanitization_button = QPushButton("Sanitisation", self)
# #         sanitization_button.setFixedSize(200, 100)

# #         button_3 = QPushButton("Button 3", self)
# #         button_3.setFixedSize(200, 100)

# #         # Create vertical layout and add buttons with center alignment
# #         layout = QVBoxLayout(self)
# #         layout.addWidget(bin_stats_button, alignment=Qt.AlignCenter)
# #         layout.addWidget(sanitization_button, alignment=Qt.AlignCenter)
# #         layout.addWidget(button_3, alignment=Qt.AlignCenter)

# #         # Connect buttons to the close function
# #         bin_stats_button.clicked.connect(self.close_app)
# #         sanitization_button.clicked.connect(self.close_app)
# #         button_3.clicked.connect(self.close_app)

# #     def close_app(self):
# #         self.close()

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     home_screen = HomeScreen()

# #     # Show the window in fullscreen
# #     home_screen.showFullScreen()

# #     sys.exit(app.exec_())


# # import sys
# # import subprocess
# # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# # from PyQt5.QtCore import Qt

# # class HomeScreen(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Home Screen")
# #         self.setGeometry(0, 0, 800, 480)

# #         bin_stats_button = QPushButton("Bin Stats", self)
# #         bin_stats_button.setFixedSize(200, 100)

# #         sanitization_button = QPushButton("Sanitisation", self)
# #         sanitization_button.setFixedSize(200, 100)

# #         button_3 = QPushButton("Button 3", self) 
# #         button_3.setFixedSize(200, 100)

# #         layout = QVBoxLayout(self)
# #         layout.addWidget(bin_stats_button, alignment=Qt.AlignCenter)
# #         layout.addWidget(sanitization_button, alignment=Qt.AlignCenter)
# #         layout.addWidget(button_3, alignment=Qt.AlignCenter)

# #         bin_stats_button.clicked.connect(self.run_piechart)
# #         sanitization_button.clicked.connect(self.close_app)
# #         button_3.clicked.connect(self.close_app)

# #     def run_piechart(self):
# #         subprocess.run(["python3", "/home/akash/Desktop/piechart.py"])

# #     def close_app(self):
# #         self.close()

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     home_screen = HomeScreen()
# #     home_screen.showFullScreen()
# #     sys.exit(app.exec_())


# # import sys
# # import subprocess
# # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# # from PyQt5.QtCore import Qt, QTimer

# # class HomeScreen(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Home Screen")
# #         self.setGeometry(0, 0, 800, 480)
        
# #         self.bin_stats_button = QPushButton("Bin Stats", self)
# #         self.bin_stats_button.setFixedSize(200, 100)

# #         sanitization_button = QPushButton("Sanitisation", self)
# #         sanitization_button.setFixedSize(200, 100)

# #         button_3 = QPushButton("Button 3", self)
# #         button_3.setFixedSize(200, 100)

# #         layout = QVBoxLayout(self)
# #         layout.addWidget(self.bin_stats_button, alignment=Qt.AlignCenter)
# #         layout.addWidget(sanitization_button, alignment=Qt.AlignCenter)
# #         layout.addWidget(button_3, alignment=Qt.AlignCenter)

# #         self.bin_stats_button.clicked.connect(self.run_piechart)
# #         sanitization_button.clicked.connect(self.close_app)
# #         button_3.clicked.connect(self.close_app)

# #         # Set up a timer to check for idle time
# #         self.idle_timer = QTimer(self)
# #         self.idle_timer.timeout.connect(self.check_idle)
# #         self.idle_timer.start(1000)  # Check every second

# #         # Track the last mouse activity time
# #         self.last_activity_time = 0

# #     def run_piechart(self):
# #         subprocess.run(["python3", "/home/akash/Desktop/piechart.py"])

# #     def check_idle(self):
# #         # Check if more than 30 seconds have passed since the last activity
# #         if self.last_activity_time > 0 and time.time() - self.last_activity_time > 30:
# #             # Close homescreen.py and open video.py
# #             self.close_app()
# #             subprocess.run(["python3", "/home/akash/Desktop/video.py"])

# #     def close_app(self):
# #         self.close()

# #     def mousePressEvent(self, event):
# #         # Update the last mouse activity time when a mouse click is detected
# #         self.last_activity_time = time.time()

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     home_screen = HomeScreen()
# #     home_screen.showFullScreen()
# #     sys.exit(app.exec_())

# import sys
# import subprocess
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# from PyQt5.QtCore import Qt

# class HomeScreen(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Home Screen")
#         self.setGeometry(0, 0, 800, 480)

#         bin_stats_button = QPushButton("Bin Stats", self)
#         bin_stats_button.setFixedSize(200, 100)

#         sanitization_button = QPushButton("Sanitisation", self)
#         sanitization_button.setFixedSize(200, 100)

#         button_3 = QPushButton("Button 3", self)
#         button_3.setFixedSize(200, 100)

#         layout = QVBoxLayout(self)
#         layout.addWidget(bin_stats_button, alignment=Qt.AlignCenter)
#         layout.addWidget(sanitization_button, alignment=Qt.AlignCenter)
#         layout.addWidget(button_3, alignment=Qt.AlignCenter)

#         bin_stats_button.clicked.connect(self.run_piechart)
#         sanitization_button.clicked.connect(self.close_app)
#         button_3.clicked.connect(self.close_app)

#     def run_piechart(self):
#         subprocess.Popen(["python3", "/home/akash/Desktop/piechart.py"])

#     def close_app(self):
#         self.close()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     home_screen = HomeScreen()
#     home_screen.showFullScreen()
#     sys.exit(app.exec_())

# import sys
# import subprocess
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
# from PyQt5.QtCore import Qt

# class HomeScreen(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Home Screen")
#         self.setGeometry(0, 0, 800, 480)

#         bin_stats_button = QPushButton("Bin Stats", self)
#         bin_stats_button.setFixedSize(200, 100)

#         sanitization_button = QPushButton("Sanitisation", self)
#         sanitization_button.setFixedSize(200, 100)

#         button_3 = QPushButton("Disposal", self)
#         button_3.setFixedSize(200, 100)

#         layout = QVBoxLayout(self)
#         layout.addWidget(bin_stats_button, alignment=Qt.AlignCenter)
#         layout.addWidget(sanitization_button, alignment=Qt.AlignCenter)
#         layout.addWidget(button_3, alignment=Qt.AlignCenter)

#         bin_stats_button.clicked.connect(self.run_piechart)
#         sanitization_button.clicked.connect(self.show_sanitization_message)
#         button_3.clicked.connect(self.show_disposal_message)

#     def run_piechart(self):
#         subprocess.Popen(["python3", "/home/akash/Desktop/piechart.py"])

#     def show_sanitization_message(self):
#         message_box = QMessageBox(self)
#         message_box.setWindowTitle("Sanitisation Instructions")
#         message_box.setText("Open the flap and put your phone inside")
#         message_box.setIcon(QMessageBox.Information)
#         message_box.setInformativeText("Caution: Do not put your hand inside, UVC is harmful!")
#         message_box.exec_()

#     def show_disposal_message(self):
#         message_box = QMessageBox(self)
#         message_box.setWindowTitle("Disposal")
#         message_box.setText("Your trash is being disposed!")
#         message_box.exec_()
#         subprocess.Popen(["python3", "/home/akash/Desktop/disposalClicked.py"])

#     def close_app(self):
#         self.close()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     home_screen = HomeScreen()
#     home_screen.showFullScreen()
#     sys.exit(app.exec_())
   #----------------------------------------(1)--------------------
# import sys
# import subprocess
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
# from PyQt5.QtCore import Qt
# import time

# class HomeScreen(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Home Screen")
#         self.setGeometry(0, 0, 800, 480)

#         bin_stats_button = QPushButton("Bin Stats", self)
#         bin_stats_button.setFixedSize(200, 100)

#         sanitization_button = QPushButton("Sanitisation", self)
#         sanitization_button.setFixedSize(200, 100)

#         button_3 = QPushButton("Disposal", self)
#         button_3.setFixedSize(200, 100)

#         close_button = QPushButton("Close", self)
#         close_button.setFixedSize(200, 100)

#         button_layout = QHBoxLayout()
#         button_layout.addStretch(1)  # Add an empty stretch to push buttons to the right
#         button_layout.addWidget(bin_stats_button)
#         button_layout.addWidget(sanitization_button)
#         button_layout.addWidget(button_3)
#         button_layout.addWidget(close_button)

#         layout = QVBoxLayout(self)
#         layout.addLayout(button_layout)
        
#         bin_stats_button.clicked.connect(self.run_piechart)
#         sanitization_button.clicked.connect(self.show_sanitization_message)
#         button_3.clicked.connect(self.show_disposal_message)
#         close_button.clicked.connect(self.close_app)

#     def run_piechart(self):
#         subprocess.Popen(["python3", "/home/akash/Desktop/piechart.py"])

#     def show_sanitization_message(self):
#         message_box = QMessageBox(self)
#         message_box.setWindowTitle("Sanitisation Instructions")
#         message_box.setText("Open the flap and put your phone inside")
#         message_box.setIcon(QMessageBox.Information)
#         message_box.setInformativeText("Caution: Do not put your hand inside, UVC is harmful!")
#         message_box.exec_()
#         time.sleep(3)
#         subprocess.Popen(["python3", "/home/akash/Desktop/sanitisation.py"])
#         subprocess.Popen(["python3","/home/akash/SIH/scripts/active.py"])

#     def show_disposal_message(self):
#         message_box = QMessageBox(self)
#         message_box.setWindowTitle("Disposal")
#         message_box.setText("Your trash is being disposed!")
#         message_box.exec_()
#         subprocess.Popen(["python3", "/home/akash/Desktop/disposalClicked.py"])

#     def close_app(self):
#         self.close()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     home_screen = HomeScreen()
#     home_screen.showFullScreen()
    # sys.exit(app.exec_())
        #----------------------------------(end)----------------------------->

import sys
import subprocess
import time
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Screen")
        self.setGeometry(0, 0, 800, 480)

        bin_stats_button = QPushButton("Bin Stats", self)
        bin_stats_button.setFixedSize(200, 100)

        sanitization_button = QPushButton("Sanitisation", self)
        sanitization_button.setFixedSize(200, 100)

        button_3 = QPushButton("Disposal", self)
        button_3.setFixedSize(200, 100)

        close_button = QPushButton("Close", self)
        close_button.setFixedSize(200, 100)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)  # Add an empty stretch to push buttons to the right
        button_layout.addWidget(bin_stats_button)
        button_layout.addWidget(sanitization_button)
        button_layout.addWidget(button_3)
        button_layout.addWidget(close_button)

        layout = QVBoxLayout(self)
        layout.addLayout(button_layout)
        
        bin_stats_button.clicked.connect(self.run_piechart)
        sanitization_button.clicked.connect(self.show_sanitization_message)
        button_3.clicked.connect(self.show_disposal_message)
        close_button.clicked.connect(self.close_app)

        # Initialize audio
        self.init_audio()

    def init_audio(self):
        pygame.mixer.init()

    def play_audio(self, audio_path):
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

    def run_piechart(self):
        subprocess.Popen(["python3", "/home/akash/Desktop/piechart.py"])

    def show_disposal_message(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Disposal")
        message_box.setText("Your trash is being disposed!")
        message_box.exec_()

        # Play the MP3 file
        self.play_audio("/home/akash/Downloads/disposal.mp3")
        
        subprocess.Popen(["python3", "/home/akash/Desktop/disposalClicked.py"])

    def close_app(self):
        self.close()

    def show_sanitization_message(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Sanitisation Instructions")
        message_box.setText("Open the flap and put your phone inside")
        message_box.setIcon(QMessageBox.Information)
        message_box.setInformativeText("Caution: Do not put your hand inside, UVC is harmful!")
        message_box.exec_()
        
        # Play the MP3 file
        self.play_audio("/home/akash/Downloads/openflaphi.mp3")

        time.sleep(3)
        subprocess.Popen(["python3", "/home/akash/Desktop/sanitisation.py"])
        subprocess.Popen(["python3", "/home/akash/SIH/scripts/active.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.showFullScreen()
    sys.exit(app.exec_())

