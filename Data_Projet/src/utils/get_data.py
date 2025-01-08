import pandas as pd
from typing import Optional

def load_sheet(file_path: str) -> Optional[pd.DataFrame]:
    """
    Charge une seule feuille d'un fichier Excel.

    Args:
        file_path (str): Chemin vers le fichier Excel brut.
        sheet_name (str): Nom de la feuille à charger.

    Returns:
        Optional[pd.DataFrame]: Un DataFrame contenant les données de la feuille, ou None en cas d'erreur.
    """
    try:
        # Charger la feuille spécifique
        data = pd.read_excel(file_path, "EM-DAT Data")
        print(f"Feuille chargée avec succès.")
        return data
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement de la feuille : {e}")
        return None

if __name__ == "__main__":
    # Chemin du fichier brut
    file_path = "data/raw/rawdata.xlsx"
    
    # Charger la feuille
    data = load_sheet(file_path)
    
    # Regrouper par pays pour compter le nombre de catastrophes
    catastrophes_par_pays = data.groupby("Country").size().reset_index(name="Count")

    # Afficher un aperçu des résultats
    print(catastrophes_par_pays.head())