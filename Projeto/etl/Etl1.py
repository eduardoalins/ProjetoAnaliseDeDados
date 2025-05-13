import pandas as pd
import os

def extrair_dados():
    origem_csv = "./staging/raw/marketing_campaign.csv"
    destino_csv = "./staging/raw/marketing_campaign_copia.csv"  # Exemplo: cópia para simular etapa de carga

    # Lê o arquivo existente
    df = pd.read_csv(origem_csv)
    print("Dataset lido com sucesso.")

    # Garante que o destino existe
    os.makedirs(os.path.dirname(destino_csv), exist_ok=True)

    # Salva uma cópia na mesma pasta (poderia ser renomeado ou validado)
    df.to_csv(destino_csv, index=False)
    print(f"Arquivo salvo em {destino_csv}")

if __name__ == "__main__":
    extrair_dados()
