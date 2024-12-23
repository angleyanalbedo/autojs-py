import numpy as np
import pyautogui
import pygetwindow as gw


def screenshot():
    # 截取屏幕并保存为 screenshot.png
    return np.array(pyautogui.screenshot())

def screenshot_app(window_title):
    # Get the window by title
    window = gw.getWindowsWithTitle(window_title)[0]

    # Activate the window
    window.activate()

    # Get the window's bounding box
    left, top, right, bottom = window.left, window.top, window.right, window.bottom

    # Capture the screenshot of the window
    shot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))

    return np.array(shot)