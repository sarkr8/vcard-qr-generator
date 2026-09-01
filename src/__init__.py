"""Paquete modular para la generación de códigos QR con vCard 3.0"""
from .vcard import build_vcard_payload
from .generator import generate_vcard_qr
from .parser import load_config_file, parse_text_config, parse_json_config

__all__ = [
    "build_vcard_payload",
    "generate_vcard_qr",
    "load_config_file",
    "parse_text_config",
    "parse_json_config"
]
