===============================================
 EXAMEN PARCIAL — FASE III (Automatización)
===============================================

🔹 Proyecto: Automatización de formulario y ejecución PowerShell
🔹 Lenguaje: Python 3.10+
🔹 Integrantes: Alejandro Martinez Moya - 2225328 | Fernando Garza Chávez - 2142789 | Kevin Daniel Grimaldo Esquivel - 1997415
🔹 Equipo: Nano
🔹 Fecha: 31/10/2025

Descripción

Este proyecto tiene como objetivo automatizar el llenado de un formulario web utilizando el módulo pyautogui y la ejecución de comandos PowerShell desde Python. El script captura tres pantallazos en diferentes etapas del proceso de llenado del formulario, valida las entradas del usuario, registra eventos y genera un archivo de log.

1. Información General

Lenguaje: Python 3.10+

Dependencias:

pyautogui

pillow

pyinstaller

logging (módulo estándar)

subprocess (módulo estándar)

pathlib (módulo estándar)

2. Plataforma Probada

Sistema Operativo: Windows 10 / 11

Versión de Python: 3.10 o superior

3. Resolución de Pantalla Usada

Resolución usada para pruebas: 1920x1080
Nota: La resolución debe ajustarse según el monitor del usuario, ya que las coordenadas de la pantalla están directamente relacionadas con la resolución utilizada.

4. Coordenadas Usadas

Coordenadas iniciales para el llenado del formulario:
start_coords = (610, 264)

5. Archivos y Estructura del Proyecto
Archivos Principales:

runner.py: Script encargado de la ejecución principal del proyecto, gestionando los argumentos y llamando las funciones necesarias para ejecutar los comandos PowerShell y automatizar el llenado del formulario.

core.py: Contiene la lógica de la automatización, incluyendo funciones para ejecutar comandos PowerShell, tomar capturas de pantalla y llenar el formulario.

6. Instrucciones de Ejecución
Ejecución desde la línea de comandos

Para ejecutar el script, basta con ejecutar el siguiente comando:

python runner.py --coords "610,264" --fecha "30/10/2025" --nombres "Kevin Grimaldo\nFernando Garza\nAlejandro Martinez" --suma "6365532" --opcion "DC" --ps "Get-Date"

Argumentos:

--coords: Coordenadas del formulario donde se hará clic para iniciar el llenado. (Por defecto: 610,264)

--fecha: Fecha a ingresar en el formulario. (Por defecto: 30/10/2025)

--nombres: Lista de nombres a ingresar. (Por defecto: "Kevin Grimaldo\nFernando Garza\nAlejandro Martinez")

--suma: Número a ingresar en el campo "suma". (Por defecto: 6365532)

--opcion: Opción seleccionada en el formulario (Ninguno, DC, Marvel). (Por defecto: DC)

--ps: Comando PowerShell a ejecutar (puede incluir varios comandos). (Por defecto: Get-Date)

7. Ejecución de Comandos PowerShell

El script ejecuta uno o más comandos PowerShell a través de subprocess. En el ejemplo de ejecución proporcionado, el comando por defecto es Get-Date, pero el usuario puede especificar otros comandos PowerShell.

Comando de PowerShell ejecutado:

Get-Date

8. Capturas de Pantalla

Durante la ejecución del script, se capturan tres pantallazos:

Antes del llenado del formulario:
El formulario vacío antes de iniciar la automatización.

Durante el llenado del formulario:
Durante el proceso de llenado, con los campos siendo completados.

Después del llenado del formulario:
El formulario completo después de enviar los datos.

Las imágenes generadas se guardan con el siguiente formato:
before_<timestamp>.png, during_<timestamp>.png, after_<timestamp>.png

9. Validación de Entradas

Antes de llenar el formulario, el script valida que los datos proporcionados sean correctos:

Campos requeridos:

fecha, nombres, suma, opcion

Validaciones específicas:

La "suma" debe ser numérica.

La "opcion" debe ser uno de los siguientes valores: ninguno, dc, marvel.

Si hay campos faltantes o los valores no son válidos, el script lanzará un error y no continuará con el llenado del formulario.

10. Empaquetado del Proyecto

El proyecto se empaqueta en un ejecutable usando pyinstaller para generar un archivo ejecutable que puede ser ejecutado sin necesidad de una ventana de consola visible.

Comando para generar el ejecutable:
pyinstaller --onefile --noconsole runner.py


Este comando crea un archivo ejecutable que no muestra la ventana de consola mientras se ejecuta.

11. Log de Ejecución

El script genera un archivo de log llamado run.log, que contiene los eventos ocurridos durante la ejecución, incluidos los comandos PowerShell ejecutados, los errores (si los hay) y la información sobre las capturas de pantalla tomadas.

12. Consideraciones Finales

Asegúrate de tener Python 3.10 o superior instalado.

Instala las dependencias necesarias utilizando pip:

pip install pyautogui pillow pyinstaller


El código debe ejecutarse correctamente en sistemas Windows 10/11. La resolución de pantalla debe ser ajustada según el monitor utilizado.
