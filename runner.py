
import logging
from core import run_powershell, validate_data, fill_form

def main():
    logging.basicConfig(
        filename="run.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )

    logging.info("Inicio del examen práctico — Fase III")

    data = {
        "nombre": "Alumno Ejemplo",
        "correo": "ejemplo@correo.com",
        "equipo": "Equipo 3"
    }

    if not validate_data(data):
        logging.error("Datos inválidos. Terminando ejecución.")
        return

    start_coords = (450, 320)
    logging.info(f"Coordenadas de inicio: {start_coords}")

    code, out, err = run_powershell("Get-Date")
    logging.info(f"PowerShell code: {code}")
    logging.info(f"PowerShell output: {out}")
    if err:
        logging.warning(f"PowerShell error: {err}")

    fill_form(data, start_coords)

    logging.info("Fin del examen. Ejecución completada con éxito.")


if __name__ == "__main__":
    main()
