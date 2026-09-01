# 📇 vCard QR Code Generator (iOS & Android Compatible)

Generador en **Python** de códigos QR profesionales, ultra-compactos y de alta definición para tarjetas de contacto en formato estándar **vCard 3.0 (RFC 2426)**.

Diseñado específicamente para ser **fácil de usar por personas sin experiencia técnica** y optimizado para insertar en **Currículum Vitae (CV)**, portafolios digitales o tarjetas de presentación.

---

## 📁 Estructura del Proyecto

```text
vcard-qr-generator/
│
├── datos_contacto.txt          # ⭐ ARCHIVO PRINCIPAL: Edita tus datos aquí con el Bloc de Notas
├── datos_contacto.ejemplo.txt  # Plantilla de ejemplo con todos los campos disponibles
├── config.json                 # (Opcional) Configuración alternativa en formato JSON
├── requirements.txt            # Dependencias de Python (qrcode, pillow)
├── .gitignore                  # Reglas de exclusión para Git
├── README.md                   # Documentación completa del proyecto
├── main.py                     # Script ejecutable principal
│
├── output/                     # Carpeta donde se guardan automáticamente los códigos QR (.png)
│   ├── .gitkeep
│   └── qr_contacto.png  # Código QR generado listo para usar
│
└── src/                        # Código fuente modular
    ├── __init__.py
    ├── parser.py               # Lector inteligente de archivos .txt (Clave = Valor) y .json
    ├── vcard.py                # Constructor estricto de vCard 3.0 con CRLF (\r\n) y filtro de vacíos
    └── generator.py            # Motor de renderizado del código QR
```

---

## ✨ Características Principales

1. **Facilidad total para no-programadores**: No necesitas tocar código Python; solo abres `datos_contacto.txt` con el Bloc de Notas de Windows, llenas tus datos y ejecutas `python main.py`.
2. **Omisión automática de campos vacíos**: Todos los campos que dejes vacíos (ej. teléfonos adicionales, redes que no uses) son ignorados por completo. El código QR solo contendrá lo que tú llenes, manteniéndolo ultra-ligero y rápido de leer.
3. **Formato ultra-compacto y nítido para CV**:
   - Sin sobrecargar el código QR con datos binarios pesados.
   - Matriz pequeña (~85 a 95 módulos) con bloques grandes y limpios (`BOX_SIZE = 6`, `BORDE = 2`).
   - Se escanea instantáneamente en papel o pantalla incluso a un tamaño de **2 x 2 cm** en tu CV sin riesgo de distorsión al imprimir.
4. **Compatibilidad móvil universal**: Cumple la norma RFC 2426 con saltos `\r\n` (CRLF) para que las cámaras de **iPhone / iOS** y **Android** abran directamente la acción *"Añadir a contactos"*.
5. **Todos los campos vCard disponibles**: Nombre, prefijos, sufijos, cargo, empresa, departamento, rol, celular, teléfono de oficina, WhatsApp directo, correo personal y de oficina, dirección, fecha de cumpleaños, notas y redes sociales (LinkedIn, GitHub, portafolio, Twitter/X, etc.).

---

## 🚀 Guía de Uso Paso a Paso

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Editar tus datos personales
Abre el archivo **`datos_contacto.txt`** con el Bloc de Notas y escribe tus datos:

```ini
# --- IDENTIDAD ---
NOMBRE = xxxxx
APELLIDOS = xxxxxx
NOMBRE_COMPLETO = xxxxx 

# --- PROFESIONAL ---
PUESTO = Desarrollador Backend Java
EMPRESA = Desarrollo de Software

# --- CONTACTO ---
TELEFONO_CELULAR = xxxxxxxx
EMAIL_PERSONAL = example@gmail.com
CIUDAD = 
PAIS = 

# --- ENLACES ---
LINKEDIN = xxxxxxxx
GITHUB = https://github.com/sarkr8
```

### 3. Generar el código QR
Ejecuta el script:

```bash
python main.py
```

Tu código QR se creará de inmediato en la carpeta `output/` (ejemplo: `output/qr_contacto.png`).

---

## 🛠️ Uso Avanzado (CLI)

Puedes especificar diferentes archivos de entrada si deseas generar códigos QR para múltiples personas o colaboradores:

```bash
# Usar una plantilla de texto personalizada
python main.py -i datos_contacto.ejemplo.txt

# O usar un archivo JSON
python main.py -i config.json
# 📇 vCard QR Code Generator (iOS & Android Compatible)

Generador en **Python** de códigos QR profesionales, ultra-compactos y de alta definición para tarjetas de contacto en formato estándar **vCard 3.0 (RFC 2426)**.

Diseñado específicamente para ser **fácil de usar por personas sin experiencia técnica** y optimizado para insertar en **Currículum Vitae (CV)**, portafolios digitales o tarjetas de presentación.

---

## 📁 Estructura del Proyecto

```text
vcard-qr-generator/
│
├── datos_contacto.txt          # ⭐ ARCHIVO PRINCIPAL: Edita tus datos aquí con el Bloc de Notas
├── datos_contacto.ejemplo.txt  # Plantilla de ejemplo con todos los campos disponibles
├── config.json                 # (Opcional) Configuración alternativa en formato JSON
├── requirements.txt            # Dependencias de Python (qrcode, pillow)
├── .gitignore                  # Reglas de exclusión para Git
├── README.md                   # Documentación completa del proyecto
├── main.py                     # Script ejecutable principal
│
├── output/                     # Carpeta donde se guardan automáticamente los códigos QR (.png)
│   ├── .gitkeep
│   └── qr_contacto.png  # Código QR generado listo para usar
│
└── src/                        # Código fuente modular
    ├── __init__.py
    ├── parser.py               # Lector inteligente de archivos .txt (Clave = Valor) y .json
    ├── vcard.py                # Constructor estricto de vCard 3.0 con CRLF (\r\n) y filtro de vacíos
    └── generator.py            # Motor de renderizado del código QR
```

---

## ✨ Características Principales

1. **Facilidad total para no-programadores**: No necesitas tocar código Python; solo abres `datos_contacto.txt` con el Bloc de Notas de Windows, llenas tus datos y ejecutas `python main.py`.
2. **Omisión automática de campos vacíos**: Todos los campos que dejes vacíos (ej. teléfonos adicionales, redes que no uses) son ignorados por completo. El código QR solo contendrá lo que tú llenes, manteniéndolo ultra-ligero y rápido de leer.
3. **Formato ultra-compacto y nítido para CV**:
   - Sin sobrecargar el código QR con datos binarios pesados.
   - Matriz pequeña (~85 a 95 módulos) con bloques grandes y limpios (`BOX_SIZE = 6`, `BORDE = 2`).
   - Se escanea instantáneamente en papel o pantalla incluso a un tamaño de **2 x 2 cm** en tu CV sin riesgo de distorsión al imprimir.
4. **Compatibilidad móvil universal**: Cumple la norma RFC 2426 con saltos `\r\n` (CRLF) para que las cámaras de **iPhone / iOS** y **Android** abran directamente la acción *"Añadir a contactos"*.
5. **Todos los campos vCard disponibles**: Nombre, prefijos, sufijos, cargo, empresa, departamento, rol, celular, teléfono de oficina, WhatsApp directo, correo personal y de oficina, dirección, fecha de cumpleaños, notas y redes sociales (LinkedIn, GitHub, portafolio, Twitter/X, etc.).

---

## 🚀 Guía de Uso Paso a Paso

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Editar tus datos personales
Abre el archivo **`datos_contacto.txt`** con el Bloc de Notas y escribe tus datos:

```ini
# --- IDENTIDAD ---
NOMBRE = xxxxxxxx
APELLIDOS = xxxxxxxxxxx
NOMBRE_COMPLETO =  xxxxxxxxx

# --- PROFESIONAL ---
PUESTO = Desarrollador Backend Java
EMPRESA = Desarrollo de Software

# --- CONTACTO ---
TELEFONO_CELULAR = 
EMAIL_PERSONAL = exaple@gmail.com
CIUDAD = CDMX
PAIS = México

# --- ENLACES ---
LINKEDIN = xxxxxxxxxxxx
GITHUB = https://github.com/sarkr8
```

### 3. Generar el código QR
Ejecuta el script:

```bash
python main.py
```

Tu código QR se creará de inmediato en la carpeta `output/` (ejemplo: `output/qr_contacto.png`).

---

## 🛠️ Uso Avanzado (CLI)

Puedes especificar diferentes archivos de entrada si deseas generar códigos QR para múltiples personas o colaboradores:

```bash
# Usar una plantilla de texto personalizada
python main.py -i datos_contacto.ejemplo.txt

# O usar un archivo JSON
python main.py -i config.json
```
