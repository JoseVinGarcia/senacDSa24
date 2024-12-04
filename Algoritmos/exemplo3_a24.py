# AULA 24 - Usando Polars (Final)

import pandas as pd
import polars as pl
from datetime import datetime
import gc # garbage collector
import os

ENDERECO_DADOS = r'./dados/'
try:
    print("Obtendo Dados")

    # hora de inicio
    inicio = datetime.now()

    lista_arquivos = []

    # Lista fina dos arquivos de dados que vieram do diretório
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    # Pega os arquivos CSV do diretorio
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
    
    #print(lista_arquivos)

    for arquivo in lista_arquivos:
        print(f"Processando arquivo {arquivo}")

        # Leitura de cada um dos dataframes
        df = pl.read_csv(ENDERECO_DADOS + arquivo,separator=';',encoding='iso-8859-1')

        # verifica no ambiente local se tem uma variavel chamada df_bolsa_familia. De primeira retornará o Else
        if "df_bolsa_familia" in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df
    
        # limpar df da memoria
        del df
        #print(df_bolsa_familia.head())
        #print(df_bolsa_familia.shape)
        #print(df_bolsa_familia.columns)
        #print(df_bolsa_familia.dtypes)
        print(f"Arquivo {arquivo} processado com sucesso!")

    # Criar arquivo parquet, que criptografa e diminui a memoria
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + "bolsa_familia.parquet")
    # Deletar DF da memoria
    del df_bolsa_familia
    # coletar residuos da memoria
    gc.collect()

    # hora final
    fim = datetime.now()

    print(f"Tempo de execução: {fim - inicio}")

except ImportError as e:
    print(f"Erro ao obter dados: {e}")

