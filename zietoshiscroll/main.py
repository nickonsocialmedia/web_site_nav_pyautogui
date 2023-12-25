import pyautogui
import pyautogui as pt
import subprocess
import platform
import time
import random


# Helper function to open Chromium with the Android user agent
def open_chromium_with_android_agent():
    website_url = "http://luc.zietoshi.com"
    chromium_command = ""

    if platform.system() == 'Linux':
        chromium_command = f"snap run chromium --user-agent=\"Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36\" {website_url}"
    elif platform.system() == 'Windows':
        # Add Windows command if needed
        pass
    elif platform.system() == 'Darwin':
        # Add macOS command if needed
        pass
    else:
        print("Unsupported operating system")
        return

    try:
        # Open Chromium without waiting for user input
        subprocess.Popen(chromium_command, shell=True)
    except Exception as e:
        print(f"Error: {e}")


# Function to simulate human-like typing speed
def type_with_random_speed(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.5))  # Random delay between keystrokes


# Helper function to navigate to an image on the screen
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateOnScreen(image, 3, confidence=.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=1)
        pt.moveRel(off_x, off_y, duration=.4)
        pt.click(clicks=clicks, interval=.3)


if __name__ == "__main__":
    open_chromium_with_android_agent()

    # Wait for a brief moment before continuing (adjust as needed)
    pt.sleep(18)

    # Navigate to the first image
    nav_to_image('images/image1.png', 1)

    # Wait for a brief moment before continuing (adjust as needed)
    pt.sleep(18)

    # Navigate to the second image
    nav_to_image('images/image2.png', 1)
    time.sleep(random.uniform(12, 15))

    # find email text box click
    # Navigate to the second image
    nav_to_image('images/image3.png', 1)

    # Type email with random speed
    email = "luczietoshi@email.com"
    type_with_random_speed(email)

    time.sleep(random.uniform(12, 15))

    # Navigate to the second image
    nav_to_image('images/image4.png', 1)

    # Type username with random speed
    username = "luczietoshi"
    type_with_random_speed(username)
    time.sleep(random.uniform(12, 15))

    # Navigate to the second image
    nav_to_image('images/image5.png', 1)

    # Type username with random speed
    passwd = "1234567"
    type_with_random_speed(passwd)
    time.sleep(random.uniform(12, 15))

    # Navigate to the second image
    nav_to_image('images/image6.png', 1)

    # Type username with random speed
    passwd2 = "1234567"
    type_with_random_speed(passwd2)
    time.sleep(random.uniform(10, 15))

    # Navigate to the second image
    nav_to_image('images/image7.png', 1)
    time.sleep(random.uniform(10, 15))

    # Navigate to the second image
    nav_to_image('images/image8.png', 1)

    # Type username with random speed
    notes = "Hey ......  This is my new test website. It only uses http which some people dont like...... leave a comment please like the video!! I will go on longer tommorrow. But for now I hope you enjoy!"
    type_with_random_speed(notes)
    time.sleep(random.uniform(10, 15))

    # Wait for user input before continuing
    input("Press Enter to find and click on images...")
