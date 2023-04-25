import keyboard
import time
import pyautogui
import numpy as np

# set up screen detection parameters
pixel_radius = 10
screen_threshold = 10  # adjust this value to suit your needs

# cast line
pyautogui.click(button='left')
cast_position = pyautogui.position()

# main loop
while True:
    # wait for catch
    while True:
        # check for change in screen within pixel radius
        x, y = pyautogui.position()
        if abs(x - cast_position[0]) > pixel_radius or abs(y - cast_position[1]) > pixel_radius:
            # compare current screen with reference screen
            reference_screen = np.array(pyautogui.screenshot())
            time.sleep(0.1)  # wait a bit to make sure screen has updated
            current_screen = np.array(pyautogui.screenshot())
            if np.sum(np.abs(reference_screen - current_screen)) > screen_threshold:
                # reel in
                keyboard.press_and_release('space')
                break
