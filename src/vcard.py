def build_vcard_payload(config: dict) -> str:
    """
    Construye la tarjeta de contacto en formato vCard 3.0 siguiendo el estándar RFC 2426.
    
    Reglas de optimización:
    - OMITE estrictamente cualquier campo vacío para que el QR sea ultra-compacto y ligero.
    - Utiliza terminadores de línea CRLF (\r\n) obligatorios para compatibilidad con iOS y Android.
    - Asigna etiquetas limpias a los enlaces web sin generar duplicados.
    """
    lines = ["BEGIN:VCARD", "VERSION:3.0"]
    
    # 1. Nombre estructurado y formateado
    last = config.get("last_name", "").strip()
    first = config.get("first_name", "").strip()
    middle = config.get("middle_name", "").strip()
    prefix = config.get("prefix", "").strip()
    suffix = config.get("suffix", "").strip()
    formatted_name = config.get("formatted_name", "").strip()
    
    # N: Apellidos;Nombre;SegundoNombre;Prefijo;Sufijo
    lines.append(f"N:{last};{first};{middle};{prefix};{suffix}")
    
    if formatted_name:
        lines.append(f"FN:{formatted_name}")
    elif first or last:
        lines.append(f"FN:{first} {last}".strip())
        
    if config.get("nickname"):
        lines.append(f"NICKNAME:{config['nickname'].strip()}")
        
    # 2. Información profesional y empresa
    if config.get("title"):
        lines.append(f"TITLE:{config['title'].strip()}")
        
    org = config.get("organization", "").strip()
    dept = config.get("department", "").strip()
    if org and dept:
        lines.append(f"ORG:{org};{dept}")
    elif org:
        lines.append(f"ORG:{org}")
        
    if config.get("role"):
        lines.append(f"ROLE:{config['role'].strip()}")
        
    # 3. Teléfonos (con etiquetas limpias)
    if config.get("phone_cell"):
        lines.append(f"TEL;TYPE=CELL,VOICE:{config['phone_cell'].strip()}")
    elif config.get("phone"):
        lines.append(f"TEL;TYPE=CELL,VOICE:{config['phone'].strip()}")
        
    if config.get("phone_work"):
        lines.append(f"TEL;TYPE=WORK,VOICE:{config['phone_work'].strip()}")
        
    if config.get("phone_home"):
        lines.append(f"TEL;TYPE=HOME,VOICE:{config['phone_home'].strip()}")
        
    # 4. Correos electrónicos (TYPE=HOME / TYPE=WORK para evitar la etiqueta 'INTERNET')
    if config.get("email_personal"):
        lines.append(f"EMAIL;TYPE=HOME:{config['email_personal'].strip()}")
    elif config.get("email"):
        email_type = config.get("email_type", "HOME")
        lines.append(f"EMAIL;TYPE={email_type}:{config['email'].strip()}")
        
    if config.get("email_work"):
        lines.append(f"EMAIL;TYPE=WORK:{config['email_work'].strip()}")
        
    # 5. Dirección física
    street = config.get("street", "").strip()
    neighborhood = config.get("neighborhood", "").strip()
    full_street = f"{street} {neighborhood}".strip() if neighborhood else street
    city = config.get("city", "").strip()
    state = config.get("state", "").strip()
    postal = config.get("postal_code", "").strip()
    country = config.get("country", "").strip()
    
    if any([full_street, city, state, postal, country]):
        lines.append(f"ADR;TYPE=HOME:;;{full_street};{city};{state};{postal};{country}")
        
    # 6. Fecha de cumpleaños
    if config.get("birthday"):
        lines.append(f"BDAY:{config['birthday'].strip()}")
        
    # 7. Sitios web y redes sociales (etiquetadas sin duplicados)
    websites = config.get("websites", [])
    for idx, site in enumerate(websites, start=1):
        url = site.get("url", "").strip()
        label = site.get("label", f"Sitio {idx}").strip()
        if url:
            lines.append(f"item{idx}.URL:{url}")
            lines.append(f"item{idx}.X-ABLabel:{label}")
            
    # 8. Nota / Descripción profesional
    if config.get("note"):
        clean_note = config["note"].replace("\n", " ").replace("\r", "").strip()
        lines.append(f"NOTE:{clean_note}")
        
    lines.append("END:VCARD")
    
    # Terminador CRLF (\r\n) según RFC 2426
    return "\r\n".join(lines)
