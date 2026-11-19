"""importacoes"""
from pathlib import Path
import pandas as pd
from app import config


def save_data(df: pd.DataFrame, path: Path = config.OUTPUT_DIR / "resultado.xlsx" ) -> None:
    """Recebe um DF e salva no path informado em formato xlsx"""
    df.to_excel(path)
