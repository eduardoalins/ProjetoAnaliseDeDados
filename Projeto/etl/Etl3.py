import pandas as pd
from sqlalchemy import create_engine

# 1. Conexão com o PostgreSQL
db_user = "admin"
db_pass = "admin123"
db_host = "localhost"
db_port = "5432"
db_name = "dw_db"

engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

# 2. Leitura do CSV bruto
df = pd.read_csv("../staging/raw/marketing_campaign.csv", sep="\t")
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True)

# 3. Criação das dimensões com as colunas solicitadas
dim_dados_pessoais = df[["Year_Birth", "Income", "Education", "MntWines"]].drop_duplicates()
dim_moradia = df[["Kidhome", "Teenhome", "MntWines"]].drop_duplicates()
dim_tempo = df[["Dt_Customer", "Recency", "MntWines"]].drop_duplicates()
dim_relacionamento = df[["Marital_Status", "MntWines"]].drop_duplicates()

# 4. Inserção no PostgreSQL (substitui as tabelas se já existirem)
dim_dados_pessoais.to_sql("dim_dados_pessoais", con=engine, index=False, if_exists='replace')
dim_moradia.to_sql("dim_moradia", con=engine, index=False, if_exists='replace')
dim_tempo.to_sql("dim_tempo", con=engine, index=False, if_exists='replace')
dim_relacionamento.to_sql("dim_relacionamento", con=engine, index=False, if_exists='replace')

print("✅ Tabelas dimensionais criadas e populadas com sucesso.")
