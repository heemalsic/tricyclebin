from ultralytics import YOLO
import subprocess

def capture_image(file_path='/home/akash/Pictures/akash.jpg'):
    try:
        # Run fswebcam command
        subprocess.run(['fswebcam', file_path])
        print(f"Image captured and saved to {file_path}")
        return file_path

    except Exception as e:
        print(f"Error capturing image: {e}")
        return None

# Call the function to capture an image
captured_image_path = capture_image()

if captured_image_path:
    print(f"The image is stored at: {captured_image_path}")

    model_path = "/home/akash/SIH/weights/train686.pt"

    model = YOLO(model_path)
    names = model.names

    results = model(captured_image_path, save=True)

    result_list = []
    print(results)
    for r in results:
        for c in r.boxes.cls:
            result_list.append(names[int(c)])

    message = 0 if len(result_list) == 0 else 1
    print(f"Message: {message}")

else:
    print("Image capture failed.")
