import argparse
import logging
from core import run_powershell, fill_form, parse_coords, FormError

def main():
	logging.basicConfig(filename="run.log", level=logging.INFO,
						format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
	logging.info("Inicio del examen")

	parser = argparse.ArgumentParser(description="Examen Parcial - Fase III runner")
	parser.add_argument("--coords", type=str, default="610,264")
	parser.add_argument("--fecha", type=str, default="30/10/2025")
	parser.add_argument("--nombres", type=str, default="Kevin Grimaldo\nFernando Garza\nAlejandro Martinez")
	parser.add_argument("--suma", type=str, default="6365532")
	parser.add_argument("--opcion", type=str, default="DC")
	parser.add_argument("--ps", type=str, action="append", default=["Get-Date"])
	args = parser.parse_args()

	try:
		start_coords = parse_coords(args.coords)
	except ValueError as e:
		logging.error(str(e))
		return

	data = {
		"fecha": args.fecha,
		"nombres": args.nombres,
		"suma": args.suma,
		"opcion": args.opcion
	}

	for cmd in args.ps:
		code, out, err = run_powershell(cmd)
		logging.info(f"PS '{cmd}' code={code}")
		if out: logging.info(f"stdout:\n{out}")
		if err: logging.warning(f"stderr:\n{err}")

	try:
		fill_form(data, start_coords)
	except FormError as e:
		logging.error(f"Validación falló: {e}")
	except Exception as e:
		logging.exception(f"Error en llenado: {e}")

	logging.info("Fin del examen")

if __name__ == "__main__":
	main()
