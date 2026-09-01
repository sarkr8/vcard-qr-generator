import os
import json


def parse_text_config(file_path: str) -> dict:
    """
    Parsea un archivo de texto plano tipo Clave = Valor (.txt).
    Omite líneas vacías y comentarios (iniciados con #).
    """
    config = {}
    with open(file_path, "r", encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            
            if "=" in line:
                key, val = line.split("=", 1)
                key = key.strip().upper()
                if "#" in val and not val.strip().startswith("http"):
                    val = val.split("#", 1)[0]
                val = val.strip()
                config[key] = val

    # Mapear redes sociales y enlaces web
    websites = []
    website_keys = [
        ("LINKEDIN", "LinkedIn"),
        ("GITHUB", "GitHub"),
        ("SITIO_WEB_PERSONAL", "Sitio Web"),
        ("PORTAFOLIO", "Portafolio"),
        ("TWITTER_X", "Twitter / X"),
        ("INSTAGRAM", "Instagram"),
        ("FACEBOOK", "Facebook"),
        ("YOUTUBE", "YouTube"),
        ("CALENDLY", "Calendly"),
    ]
    for key, label in website_keys:
        if config.get(key):
            websites.append({"label": label, "url": config[key]})
            
    # WhatsApp (si está definido)
    if config.get("TELEFONO_WHATSAPP"):
        clean_num = config["TELEFONO_WHATSAPP"].replace("+", "").replace(" ", "").replace("-", "")
        websites.append({
            "label": "WhatsApp",
            "url": f"https://wa.me/{clean_num}"
        })

    structured_config = {
        # Identidad
        "first_name": config.get("NOMBRE", ""),
        "middle_name": config.get("SEGUNDO_NOMBRE", ""),
        "last_name": config.get("APELLIDOS", ""),
        "prefix": config.get("PREFIJO", ""),
        "suffix": config.get("SUFIJO", ""),
        "formatted_name": config.get("NOMBRE_COMPLETO", "") or f"{config.get('NOMBRE', '')} {config.get('APELLIDOS', '')}".strip(),
        "nickname": config.get("APODO", ""),
        
        # Profesional
        "title": config.get("PUESTO", ""),
        "organization": config.get("EMPRESA", ""),
        "department": config.get("DEPARTAMENTO", ""),
        "role": config.get("ROL", ""),
        
        # Teléfonos
        "phone_cell": config.get("TELEFONO_CELULAR", ""),
        "phone_work": config.get("TELEFONO_TRABAJO", ""),
        "phone_home": config.get("TELEFONO_CASA", ""),
        
        # Correos
        "email_personal": config.get("EMAIL_PERSONAL", ""),
        "email_work": config.get("EMAIL_TRABAJO", ""),
        
        # Dirección
        "street": config.get("CALLE_Y_NUMERO", ""),
        "neighborhood": config.get("COLONIA_BARRIO", ""),
        "city": config.get("CIUDAD", ""),
        "state": config.get("ESTADO_PROVINCIA", ""),
        "postal_code": config.get("CODIGO_POSTAL", ""),
        "country": config.get("PAIS", ""),
        
        # Enlaces
        "websites": websites,
        
        # Nota y Cumpleaños
        "note": config.get("NOTA_DESCRIPCION", ""),
        "birthday": config.get("CUMPLEANOS", ""),
        
        # Configuración Visual QR
        "box_size": int(config.get("BOX_SIZE", 6)) if config.get("BOX_SIZE", "").isdigit() else 6,
        "border": int(config.get("BORDE", 2)) if config.get("BORDE", "").isdigit() else 2,
        "output_filename": config.get("ARCHIVO_SALIDA_QR", "output/mi_contacto_qr.png")
    }

    return structured_config


def parse_json_config(file_path: str) -> dict:
    """
    Parsea un archivo JSON de configuración.
    """
    with open(file_path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def load_config_file(preferred_path: str = None) -> dict:
    """
    Carga la configuración buscando en orden:
    1. preferred_path (si se pasa por CLI)
    2. datos_contacto.txt
    3. config.json
    """
    if preferred_path and os.path.exists(preferred_path):
        if preferred_path.endswith(".json"):
            print(f"[+] Cargando configuración desde JSON: '{preferred_path}'")
            return parse_json_config(preferred_path)
        else:
            print(f"[+] Cargando configuración desde archivo de texto: '{preferred_path}'")
            return parse_text_config(preferred_path)

    if os.path.exists("datos_contacto.txt"):
        print("[+] Cargando configuración desde: 'datos_contacto.txt'")
        return parse_text_config("datos_contacto.txt")

    if os.path.exists("config.json"):
        print("[+] Cargando configuración desde: 'config.json'")
        return parse_json_config("config.json")

    raise FileNotFoundError("No se encontró ningún archivo de configuración ('datos_contacto.txt' o 'config.json').")
