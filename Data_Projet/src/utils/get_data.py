import pandas as pd

def load_excel_data(file_path: str) -> dict:
    """Charge les données d'un fichier Excel avec plusieurs feuilles."""
    return pd.read_excel(file_path, sheet_name=None)  # Dictionnaire {feuille: DataFrame}

if __name__ == "__main__":
    file_path = "data/raw/rawdata.xlsx"
    data = load_excel_data(file_path)
    print(f"Feuilles disponibles : {data.keys()}")

    data_full = pd.read_excel(file_path, sheet_name="EM-DAT Data")

    print(data_full)