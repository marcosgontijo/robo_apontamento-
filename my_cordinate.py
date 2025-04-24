import pyautogui
import time

print("Mova o mouse e veja as posições...")
time.sleep(3)

while True:
    print(pyautogui.position())
    time.sleep(1)
