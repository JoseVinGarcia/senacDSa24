# AULA 24 - Big data

import pandas as pd
from datetime import datetime

try:
    ENDERECO_DADOS = r'./dados/'

    # hora de inicio
    hora_import = datetime.now()

    df_janeiro = pd.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv',sep=';',encoding='iso-885')

    print(df_janeiro.head())
except ImportError as e:
    print(f"Erro ao obter dados: {e}")
