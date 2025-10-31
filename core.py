import subprocess
import pyautogui
import time
import logging
from datetime import datetime
from pathlib import Path

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

class FormError(Exception):
	pass

def run_powershell(cmd, timeout=10):
	try:
		r = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, timeout=timeout)
		return r.returncode, r.stdout.strip(), r.stderr.strip()
	except Exception as e:
		return 1, "", str(e)

def take_screenshot(name):
	out = Path("out")
	out.mkdir(exist_ok=True)
	ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
	path = out / f"{name}_{ts}.png"
	img = pyautogui.screenshot()
	img.save(path)
	logging.info(f"Screenshot: {path}")
	return path

def parse_coords(value):
	try:
		xs, ys = value.split(",")
		x, y = int(xs), int(ys)
		if x < 0 or y < 0:
			raise ValueError("negativas")
		return (x, y)
	except Exception as e:
		raise ValueError(f"Coordenadas inválidas '{value}': {e}")

def validate_data(data):
	req = ["fecha", "nombres", "suma", "opcion"]
	missing = [k for k in req if k not in data or not str(data[k]).strip()]
	if missing:
		raise FormError(f"Campos faltantes: {', '.join(missing)}")
	if not str(data["suma"]).strip().isdigit():
		raise FormError("La 'suma' debe ser numérica.")
	if str(data["opcion"]).lower() not in {"ninguno","dc","marvel"}:
		raise FormError("La 'opcion' debe ser: Ninguno, DC o Marvel.")

def fill_form(data, start_coords):
	validate_data(data)
	take_screenshot("before")
	pyautogui.click(start_coords[0], start_coords[1], clicks=2)
	hoy = datetime.now().strftime("%d/%m/%Y")
	pyautogui.typewrite(hoy)
	logging.info(f"Fecha escrita: {hoy}")
	pyautogui.press("tab")
	pyautogui.typewrite(str(data["nombres"]))
	pyautogui.press("tab")
	pyautogui.typewrite(str(data["suma"]))
	pyautogui.press("tab")
	opt = str(data["opcion"]).lower()
	if opt == "dc":
		pyautogui.press("down")
	elif opt == "marvel":
		pyautogui.press("down")
		pyautogui.press("down")
	time.sleep(0.5)
	pyautogui.press("tab")
	pyautogui.press("enter")
	take_screenshot("during")
	time.sleep(1)
	take_screenshot("after")
