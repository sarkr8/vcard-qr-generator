import os
import qrcode
from .vcard import build_vcard_payload


def generate_vcard_qr(config: dict) -> str:
    """
    Genera y guarda el código QR final a partir de la configuración provista.
    
    Parámetros:
        config (dict): Diccionario de configuración del contacto.
        
    Retorna:
        str: Ruta del archivo generado.
    """
    # 1. Construir la vCard omitiendo campos vacíos
    vcard_payload = build_vcard_payload(config)
    payload_size = len(vcard_payload.encode("utf-8"))
    
    # 2. Configuración visual del QR
    box_size = config.get("box_size", 6)
    border = config.get("border", 2)
    
    # Corrección de errores M (15%) para óptima robustez y legibilidad en papel
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(vcard_payload)
    qr.make(fit=True)
    
    # 3. Renderizar imagen del código QR
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # 4. Asegurar que el directorio de salida exista
    output_path = config.get("output_filename", "output/mi_contacto_qr.png")
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
    # 5. Guardar archivo final
    qr_img.save(output_path)
    
    print("=" * 60)
    print(" CODIGO QR GENERADO CON EXITO")
    print("=" * 60)
    print(f" Archivo guardado: {output_path}")
    print(f" Dimensiones imagen: {qr_img.size[0]}x{qr_img.size[1]} px (box_size={box_size}, border={border})")
    print(f" Matriz QR: Version {qr.version} ({qr.modules_count}x{qr.modules_count} modulos)")
    print(f" Tamano payload vCard: {payload_size} bytes")
    print(f" Nombre: {config.get('formatted_name') or config.get('first_name')}")
    if config.get('title'):
        print(f" Cargo: {config.get('title')}")
    if config.get('phone_cell') or config.get('phone'):
        print(f" Telefono: {config.get('phone_cell') or config.get('phone')}")
    if config.get('email_personal') or config.get('email'):
        print(f" Correo: {config.get('email_personal') or config.get('email')}")
    print("=" * 60)
    print(" Escanealo con la camara de tu movil para guardar el contacto.")
    
    return output_path
