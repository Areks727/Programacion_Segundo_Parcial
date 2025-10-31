import pyautogui
import time

print("Mueve el cursor a la posición deseada...")
time.sleep(5)
pos = pyautogui.position()
print(f"Coordenadas actuales: {pos}")

