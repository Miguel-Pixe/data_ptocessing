import json, random, time
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import sqlite3 

''' 1: Camada de Bronze: Aqui os dados serão ingeridos em sua forma de origem para serem transformados
posteriormente'''

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE faturamento (
                id_cliente INTEGER,
                valor REAL,
                data TEXT,
                status TEXT
                )
                """)

    cursor.executemany("""
    INSERT INTO faturamento (id_cliente,valor,data,status)
    VALUES (?,?,?,?)
                    """,
                    [
                        (1,120.00,'2026-6-1', 'ativo'),
                        (2,200.00, '2026-6-2', 'cancelado'),
                        (3,150.00, '2026-6-3', 'ativo')
                        ])

    cursor.execute("SELECT * FROM faturamento")
    print(cursor.fetchall())


def pipeline():

    dados = []
    for i in range(10):
        data = {
            "corrente" : random.uniform(10, 50),
            "tensao" : random.uniform(200, 240),
            "soc" : random.uniform(0,100)
        }
        dados.append(data)
        time.sleep(2)
    return dados


def dataframe(dados):
    df = pd.DataFrame(dados)

    df["soc"] = df["soc"].fillna(df["soc"].mean())
    df = df.round(2)
    print(df)



'''
2: Camada de prata: Aqui os dados serão limpos e transformados para serem utilizados 
posteriormente
'''
def sentimento():
    frase = "O preço da energia está subindo rapidamente"
    sentimento = TextBlob(frase).sentiment.polarity
    print("=================================================")
    print(f"Sentimento da frase: {sentimento}")
    print("=================================================")

'''
3: Cmada de ouro: Aqui, os dados tratados serão utilizados para análises e visualizações,
além de serem usados para gerar insights para tomada de decisões estratégicas.
'''

def visualizacao():
    consumo = [200, 140, 220, 160,120,130,140,155,150,170,180]
    sentimentos = [-0.4,0.3,0.6,-0.2,0.0,0.1,0.2,-0.1,0.0,0.3,0.2]

    plt.scatter(sentimentos, consumo)
    plt.xlabel("Sentimento de mercado")
    plt.ylabel("Consumo (Em Kwh)")
    plt.show()


criar_tabela()
dados_pipeline = pipeline()
df = dataframe(dados_pipeline)
sentimento()
visualizacao()  


