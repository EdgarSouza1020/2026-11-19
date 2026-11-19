"""importacoes"""
import pandas as pd
from pathlib import Path


def load_data(path: Path) -> pd.DataFrame:
    """Carrega um xlsx no pah informado e devolve um DF"""
    return pd.read_excel(path)
