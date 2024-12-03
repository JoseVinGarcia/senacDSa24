# AULA 24 - Big data

import pandas as pd
import polars as pl
from datetime import datetime

# TRY COM PANDAS
# try:
#     ENDERECO_DADOS = r'./dados/'

#     # hora de inicio
#     hora_import = datetime.now()

#     df_janeiro = pd.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv',sep=';',encoding='iso-8859-1')

#     print(df_janeiro.head())

#     # hora final
#     hora_impressao = datetime.now()

#     print(f"Tempo de execução: {hora_impressao - hora_import}")


# except ImportError as e:
#     print(f"Erro ao obter dados: {e}")

# TRY COM POLARS
try:
    ENDERECO_DADOS = r'./dados/'

    # hora de inicio
    hora_import = datetime.now()

    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv',separator=';',encoding='iso-8859-1')

    print(df_janeiro.head())

    # hora final
    hora_impressao = datetime.now()

    print(f"Tempo de execução: {hora_impressao - hora_import}")

except ImportError as e:
    print(f"Erro ao obter dados: {e}")

