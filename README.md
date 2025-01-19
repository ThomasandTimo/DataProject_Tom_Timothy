# **Dashboard des Catastrophes Naturelles**

## **User Guide**
### **Pré-requis**
1. Assurez-vous d'avoir Python (version >= 3.9) installé sur votre machine.
2. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/ThomasandTimo/DataProject.git
   ```
3. Installez les dépendances nécessaires à l'exécution du projet :
   ```bash
   pip install -r requirements.txt
   ```

### **Exécution du Dashboard**
1. Lancez le script principal :
   ```bash
   python main.py
   ```
2. Ouvrez votre navigateur à l'adresse suivante :
   ```
   http://127.0.0.1:8060/
   ```

### **Structure des Répertoires**
```plaintext
data_project/
├── data/
│   ├── raw/          # Contient les données brutes (rawdata.xlsx)
│   ├── cleaned/      # Contient les données nettoyées (cleaned_data.xlsx)
├── src/
│   ├── utils/        # Scripts utilitaires (chargement et nettoyage des données)
├── main.py           # Point d'entrée principal pour lancer le dashboard
├── requirements.txt  # Dépendances nécessaires au projet
└── README.md         # Documentation du projet
```

---

## **Data**
### **Description des Données**
Les données utilisées dans ce projet proviennent de la base publique [EM-DAT Data](https://public.emdat.be/). Elles documentent les catastrophes naturelles à travers le monde et incluent des informations sur :
- Les pays touchés (`Country`).
- L'impact humain (`Total Affected`).

### **Nettoyage des Données**
Un script de nettoyage (`data_clean.py`) est utilisé pour :
- Supprimer les colonnes non utilisées
- Supprimer les lignes avec des valeurs manquantes ou non pertinentes.
- Corriger les noms des pays (e.g., "Türkiye" → "Turkey").

Les données nettoyées sont sauvegardées dans `data/cleaned/cleaned_data.xlsx`.

---

## **Developer Guide**
### **Architecture du Code**
```plaintext
src/
├── utils/
│   ├── get_data.py     # Chargement des données brutes
└── ├── data_clean.py   # Nettoyage des données
main.py           # Point d'entrée principal pour lancer le dashboard
```

## **Rapport d'Analyse**
### **1. Répartition Géographique**
Une carte interactive montre la répartition des catastrophes naturelles par pays. Par exemple :
- La Chine et les États-Unis sont parmi les pays les plus touchés en termes de nombre total de catastrophes.

### **2. Moyenne des Personnes Affectées**
Un histogramme affiche la moyenne des personnes affectées par pays :
- Les pays densément peuplés (e.g., Inde, Bangladesh) montrent une forte moyenne d'impact humain.

---

## **Copyright**
Je déclare sur l’honneur que le code fourni a été produit par nous-même.

- Certaines fonctions de chargement des données (via `pandas`) et de visualisation (via `plotly`) s’appuient sur des exemples de documentation officielle :
  - [Documentation Pandas](https://pandas.pydata.org/docs/)
  - [Documentation Plotly](https://plotly.com/python/)

Toute ligne non déclarée ci-dessus est réputée être produite par l’auteur du projet. L’absence ou l’omission de déclaration sera considérée comme du plagiat.
