# Video-Frame-Extraction-and-Saving-Script
This Python script extracts frames from a video file, resizes them, and saves every third frame as an image. It uses OpenCV to process the video and handle frame extraction, resizing, and displaying.

#Requirements
Python 3.x
OpenCV (cv2 package)
A video file (e.g., cr.mp4)
To install the necessary Python package, run:

#Description
This script performs the following tasks:

1) Video Processing: It reads a video file frame by frame.
2) Frame Skipping: Every third frame is selected.
3) Frame Resizing: The selected frames are resized to 1080x500 pixels.
4) Frame Saving: The selected and resized frames are saved as images in a specified folder.
5) Displaying Frames: Each frame is displayed in a window as it is processed.
6) Exit Condition: The script can be interrupted by pressing the ESC key.

# How to Use
1) Place your video file (cr.mp4 or any other .mp4 video) in the same directory as the script or specify the full path to the video file in the code.
2) Update the directory path where the images will be saved. By default, images are saved to C:\PROGRAMMING\ARYA PYTHON\Crash\image\.
3) Run the script using Python:

The script will process the video, extract every third frame, resize it to 1080x500, and save it in the specified directory.

File Structure
bash
Copy code
.
├── video_frame_extraction.py   # Python script
└── cr.mp4                      # Input video file (or specify your own)
Example Output
If the video has enough frames, the script will save images like:

bash
Copy code
C:\PROGRAMMING\ARYA PYTHON\Crash\image\car_0.jpg
C:\PROGRAMMING\ARYA PYTHON\Crash\image\car_1.jpg
...
Notes
Ensure the output folder (C:\PROGRAMMING\ARYA PYTHON\Crash\image\) exists before running the script, or you may encounter a file saving error.
The script processes a maximum of 130 frames from the video. You can adjust this limit by changing the maxFrames variable in the script.
Troubleshooting
If the video file is not found, make sure the path to the video file is correct.
If images are not being saved, verify that the folder path is correct and accessible.
