import pyautogui


class ScreenCapture:

    def capture(self):

        # capture screen
        screenshot = pyautogui.screenshot()

        print("Screen captured")

        return screenshot
