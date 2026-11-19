"""Importacoes"""
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = SCRIPT_DIR.resolve().parent

INPUT_DIR = PROJECT_ROOT / "data" / "input"

OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
