"""
Generador de Códigos QR para Tarjetas de Contacto (vCard 3.0)
=============================================================
Punto de entrada principal para generar códigos QR ultra-compactos y profesionales
compatibles con iOS (iPhone) y Android.

Uso rápido para usuarios:
    1. Abre y edita el archivo 'datos_contacto.txt' con el Bloc de Notas.
    2. Ejecuta en tu terminal:
       python main.py
    3. Tu código QR se creará listo en la carpeta 'output/'.
"""

import sys
import argparse
from src.parser import load_config_file
from src.generator import generate_vcard_qr


def main():
    parser = argparse.ArgumentParser(
        description="Generador de Códigos QR para Tarjetas de Contacto (vCard 3.0) sin foto para CV."
    )
    parser.add_argument(
        "-i", "--input", "--config",
        dest="config_path",
        default=None,
        help="Ruta al archivo de configuración (.txt o .json). Por defecto usa 'datos_contacto.txt'."
    )
    args = parser.parse_args()

    try:
        # 1. Cargar la configuración desde el archivo de texto o JSON
        config = load_config_file(args.config_path)

        # 2. Generar el código QR
        generate_vcard_qr(config)

    except Exception as error:
        print(f"[X] Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
