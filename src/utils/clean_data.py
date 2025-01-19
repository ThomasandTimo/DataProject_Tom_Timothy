import pandas as pd
import os

def clean_data(input_path: str, output_path: str):
    """
    Nettoie les données brutes et les sauvegarde dans un fichier nettoyé.

    Args:
        input_path (str): Chemin vers le fichier brut.
        output_path (str): Chemin où sauvegarder le fichier nettoyé.
    """
    print(f"Chargement des données depuis {input_path}...")
    # Charger les données brutes
    data = pd.read_excel(input_path, sheet_name="EM-DAT Data")
    
    print("Nettoyage des données...")

    # Ne conserver que les colonnes "Country" et "Total Affected"
    data = data[["Country", "Total Affected"]]

    # Supprimer les lignes avec des valeurs manquantes essentielles
    data = data.dropna(subset=["Country"])
    
    # Corriger les noms de pays (ex : Eswatini -> Swaziland)
    country_corrections = {
        "Eswatini": "Swaziland",
        "Türkiye": "Turkey",
    }
    data["Country"] = data["Country"].replace(country_corrections)
    
    print(f"Sauvegarde des données nettoyées dans {output_path}...")
    # Sauvegarder les données nettoyées en Excel
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Crée le dossier si nécessaire
    data.to_excel(output_path, index=False, engine='openpyxl')  # Sauvegarde au format Excel
    print("Données nettoyées sauvegardées avec succès.")

# Exécuter le nettoyage
if __name__ == "__main__":
    input_path = "data/raw/rawdata.xlsx"
    output_path = "data/cleaned/cleaned_data.xlsx"  # Changer l'extension pour .xlsx
    clean_data(input_path, output_path)