import subprocess
from os.path import isfile, join
from PIL import Image

def capture_stereo_image(output_filename="1.jpg"):
    command = [
        "raspistill", "-3d", "sbs", "-n", "-w", "8112", "-h", "3040", "-o", output_filename
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Image saved as {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")
        
folderName = "/home/Simulimb/Code"
if __name__ == "__main__": # checks if script run directly (not as a module)
    image_count = 1
    try:
        while True:
            input("Press Enter to take an image. Press ctrl+c to exit.") # waits for user input (Enter)
            fileNameNow = join(folderName,"image_"+str(image_count)+".jpg")
            capture_stereo_image(f"image_{image_count}.jpg")
            img = Image.open(fileNameNow)
            img.show()
            image_count += 1
    except KeyboardInterrupt:
        print("Exiting...")
