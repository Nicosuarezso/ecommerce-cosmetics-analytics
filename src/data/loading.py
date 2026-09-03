
"""Funciones para carga de datos crudos."""

from pathlib import Path

import pandas as pd


def load_parquet(file_path: str | Path, **kwargs) -> pd.DataFrame:
    """Carga un archivo Parquet y devuelve sus datos como DataFrame."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

    if path.suffix.lower() != ".parquet":
        raise ValueError("El archivo debe tener extensión .parquet")

    return pd.read_parquet(path, **kwargs)
