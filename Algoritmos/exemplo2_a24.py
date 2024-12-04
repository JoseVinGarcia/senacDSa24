# AULA 24 - Usando Polars

import pandas as pd
import polars as pl
from datetime import datetime
import gc # garbage collector

# Com pandas - 02m19s
# Com polars - 00m56s

try:
    ENDERECO_DADOS = r'./dados/'

    # hora de inicio
    inicio = datetime.now()

    lista_arquivos = ['202401_NovoBolsaFamilia.csv','202402_NovoBolsaFamilia.csv']

    for arquivo in lista_arquivos:
        print(f"Processando arquivo {arquivo}")
        df = pl.read_csv(ENDERECO_DADOS + arquivo,separator=';',encoding='iso-8859-1')

        # verifica no ambiente local se tem uma variavel chamada df_bolsa_familia. De primeira retornará o Else
        if "df_bolsa_familia" in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df
    
    print(df.head())
    #print(df.shape)
    #print(df.columns)
    #print(df.dtypes)

    # limpar df da memoria
    del df
    # coletar residuos da memoria
    gc.collect()

    # hora final
    fim = datetime.now()

    print(f"Tempo de execução: {fim - inicio}")

except ImportError as e:
    print(f"Erro ao obter dados: {e}")

