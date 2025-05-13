import pandas as pd
from sqlalchemy import create_engine
import os

def carregar_dados_para_postgres():
    # Parâmetros da conexão
    usuario = "admin"
    senha = "admin123"
    host = "localhost"
    porta = "5432"
    banco = "dw_db"

    # Criação da engine SQLAlchemy
    engine = create_engine(f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco}')

    # Caminho do dataset
    caminho_csv = '../staging/raw/marketing_campaign.csv'

    if not os.path.exists(caminho_csv):
        print("❌ Arquivo CSV não encontrado.")
        return

    # Leitura do dataset
    df = pd.read_csv(caminho_csv)
    print("📥 Dataset carregado com sucesso.")

    # Inserção no banco: substitui a tabela se já existir
    nome_tabela = "marketing_raw"
    df.to_sql(nome_tabela, con=engine, index=False, if_exists='replace')
    print(f"✅ Dados inseridos na tabela '{nome_tabela}' no PostgreSQL.")

if __name__ == "__main__":
    carregar_dados_para_postgres()
