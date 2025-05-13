# Projeto Análise de Dados

1. Fonte de dados: definir a origem da fonte de dados. Dataset escolhido: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance?resource=download

2. Criar 01 job (script) ETL que pega a fonte de dado e armazena em um lugar de Staging (pasta local, google drive, S3, etc)

3.Instalar o Postgres (sugestão: container docker do postgres) para servir de DataWarehouse

4. Criar 01 job(script) ETL que insere o dataset no postgres

5. Analisar o dataset e definir 4 dimensões a serem utilizadas

6. Criar 01 job(script) ETL normaliza os dados dessas dimensões e cria suas respectivas tabelas no DataWarehouse

7. Instalar o Metabase (sugestão: container docker do metabase)

8. Criar uma visualização contendo 02(dois) fatos sobre o dataset

Mapa do Fluxo

[Kaggle Dataset]
       │
       │ ETL 1 (Python)
       ▼
[File System (Staging)]
       │
       │ ETL 2 (Python)
       ▼
[Data Warehouse - PostgreSQL]
       │
       │ ETL 3 (Python - Normalização e Criação de Dimensões)
       ▼
[Metabase Dashboard]
   │── KPI 1 (Visualização)
   └── KPI 2 (Visualização)

# Data Warehouse and Analytical Visualization

Project developed during the Data Analysis and Visualization course at Cesar School's Computer Science program. It includes:

- ETL scripts for data ingestion, transformation, and normalization about students' habits and academic performance.

- Dimensional modeling with four analytical dimensions (Study Habits, Health and Well-being, Personal Profile, and Social Media).

- Relational Data Warehouse using PostgreSQL (Docker).

- Interactive dashboards and KPIs built with Metabase.

- Analytical insights exploring correlations like attendance vs. grades, part-time work impact, and mental health relationships with academic results.

Technologies: Python (pandas, sqlalchemy), PostgreSQL (Docker), Metabase, SQL, Git.
