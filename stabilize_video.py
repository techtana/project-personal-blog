import vidstab
import os
import cv2

# Define the input and output video paths
input_video_path = r'C:\Users\Tanat\OneDrive\_Projects\project-personal-blog\kings-peak.mp4'
output_video_path = r'C:\Users\Tanat\OneDrive\_Projects\project-personal-blog\kings-peak_stabilized.mp4'

# Create a VidStab object
stabilizer = vidstab.VidStab()

try:
    # Stabilize the video
    # The `border_type='black'` will add black borders to fill the gaps created by stabilization.
    # You can also use 'replicate' or 'reflect'.
    stabilizer.stabilize(input_path=input_video_path, output_path=output_video_path, border_type='black')

    print(f"Video stabilization complete. Stabilized video saved to: {output_video_path}")

except FileNotFoundError:
    print(f"Error: Input video not found at {input_video_path}")
except Exception as e:
    print(f"An error occurred during video stabilization: {e}")
    print("Please ensure you have ffmpeg installed and accessible in your system's PATH.")
    print("You also need the 'vidstab' and 'opencv-python' libraries.")
    print("Install them using: pip install vidstab opencv-python")
