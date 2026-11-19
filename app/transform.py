"""importacoes"""
import pandas as pd


def agrupar_por_subgrupo(
    df: pd.DataFrame,
    coluna_agrupar: str = "Sub-Grupo"
) -> pd.DataFrame:
    """Agrupa as vendas do grupo pelo subgrupo"""
    colunas_metricas = [
        "Venda R$",
        "Qtde. Venda",
        "Margem R$"
    ]
    return (
    df.groupby(coluna_agrupar)[colunas_metricas]
    .sum()
    .reset_index()
    .sort_values(by="Venda R$", ascending=False)
)



def fazer_merge(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    chave_esquerda: str = "Cód. Barras",
    chave_direita: str = "BARCODE",
) -> pd.DataFrame:
    """Faz o merge entre as bases de grupo e mercado."""
    return pd.merge(
        left=df1,
        right=df2,
        left_on=chave_esquerda,
        right_on=chave_direita,
        how="left",
        suffixes=("_grupo", "_mercado"),
    )
