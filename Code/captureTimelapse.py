import subprocess
from os.path import isfile, join
from PIL import Image

def capture_stereo_image(output_filename="image%04d.jpg"):
    command = [
        "raspistill", "-t", "30000", "-tl", "1000", "-3d", "sbs", "-p", "100,100,1200,800", "-w", "8112", "-h", "3040", "-o", output_filename
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Timelapse complete, Images captured")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")

if __name__ == "__main__": # checks if script run directly (not as a module)
    try:
        while True:
            input("Press Enter to take an image. Press ctrl+c to exit.") # waits for user input (Enter)
            capture_stereo_image()
    except KeyboardInterrupt:
        print("Exiting...")     
