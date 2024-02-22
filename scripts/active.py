import subprocess
import time

def switch_to_video():
    subprocess.run(["python3", "/home/akash/SIH/scripts/video.py"])

def get_active_window_title():
    try:
        result = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"], text=True, stderr=subprocess.PIPE)
        return result.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def main():
    while True:
        # Wait for 30 seconds
        time.sleep(30)

        # Check if there was inactivity for the last 30 seconds
        current_window_before = get_active_window_title()
        time.sleep(5)  # Additional time to ensure no recent activity

        current_window_after = get_active_window_title()

        if current_window_before == current_window_after and current_window_after != "video.py":
            switch_to_video()

if __name__ == "__main__":
    main()
