"""Ejecuta los 20 ejemplos desde cualquier directorio."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    for archivo in sorted(root.glob("nivel*/*.py")):
        print("\n=== " + archivo.name + " ===")
        runpy.run_path(str(archivo), run_name="__main__")
