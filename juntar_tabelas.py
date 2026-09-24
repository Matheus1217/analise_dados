import pandas as pd

t12 = pd.read_csv("Tabela5-sem_emprego_2012.csv", sep=";", decimal=",")
t26 = pd.read_csv("Tabela5-sem_emprego_2026.csv", sep=";", decimal=",")

ind = pd.read_excel("Tabela 1.1.1.xls", engine="xlrd", header=None).iloc[8:41].copy()
ind.columns = [
    "uf_regiao",
    "total",
    "total_branca",
    "total_preta_parda",
    "homem_branca",
    "homem_preta_parda",
    "mulher_branca",
    "mulher_preta_parda",
]

comp = t12.merge(t26, on=["Sigla", "Código", "Estado"], how="inner")
ind = ind.rename(columns={"uf_regiao": "Estado"})
geral = comp.merge(ind, on="Estado", how="inner")

geral.to_csv("geral.csv", sep=";", index=False, decimal=",")
