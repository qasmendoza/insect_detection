#!/usr/bin/env python3

import cv2
import os
import datetime

# Path to save the images on the external SSD
SAVE_PATH = "/media/cs2227lab/SanDisk/Insects"

# Check if the save path exists, if not create it
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# Open the first camera device
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

print("Press 'c' to capture an image.")
print("Press 'q' to quit.")

while True:
    # Capture a single frame
    ret, frame = cap.read()

    # Display the frame in a window
    cv2.imshow('Camera Feed', frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # If 'c' is pressed, capture and save the image
    if key == ord('c'):
        # Generate a filename based on the current timestamp
        filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"  # Changed .jpg to .png
        filepath = os.path.join(SAVE_PATH, filename)
        
        # Save the image
        cv2.imwrite(filepath, frame)
        print(f"Image saved to {filepath}")

    # If 'q' is pressed, exit the loop and close the camera
    elif key == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
