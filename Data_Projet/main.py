import dash
from dash import html, dcc
import plotly.express as px
from src.utils.get_data import load_sheet  # Importer la fonction de get_data.py

# region Data load

# Charger les données à partir de get_data.py
file_path = "data/raw/rawdata.xlsx"  # Chemin vers ton fichier Excel
sheet_name = "EM-DAT Data"  # Nom de la feuille
data = load_sheet(file_path)  # Appel à la fonction load_sheet

if data is None:
    raise ValueError("Les données n'ont pas pu être chargées. Vérifiez le chemin ou le fichier.")

# endregion

# region Map

# Regrouper les catastrophes par pays
catastrophes_par_pays = data.groupby("Country").size().reset_index(name="Count")

# Créer une carte choroplèthe
fig_map = px.choropleth(
    catastrophes_par_pays,
    locations="Country",
    locationmode="country names",
    color="Count",
    title="Nombre de Catastrophes par Pays",
    color_continuous_scale="Reds"
)

# endregion

#region histogramme

# Calculer la moyenne de "Total Affected" par pays
affected_avg_by_country = data.groupby("Country")["Total Affected"].mean().reset_index()

# Renommer les colonnes pour plus de clarté
affected_avg_by_country.columns = ["Country", "Average Affected"]

# remplacer None par 0
affected_avg_by_country["Average Affected"] = affected_avg_by_country["Average Affected"].fillna(0)

# mettre en int
affected_avg_by_country["Average Affected"] = affected_avg_by_country["Average Affected"].astype(int) 

# Renommer les colonnes pour plus de clarté
affected_avg_by_country.columns = ["Country", "Average Affected"]

# Créer l'histogramme
fig_histogram = px.bar(
    affected_avg_by_country.sort_values("Average Affected", ascending=False),
    x="Country",
    y="Average Affected",
    title="Moyenne des Personnes Affectées par Pays",
    labels={"Average Affected": "Personnes Moyenne Affectées", "Country": "Pays"},
    text="Average Affected"  # Affiche les valeurs sur les barres
)

# endregion

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Layout du dashboard
app.layout = html.Div([
    html.H1("Dashboard des Catastrophes Naturelles de 2000 à 2024"),
    dcc.Tabs([
        dcc.Tab(label="Carte", children=[
            dcc.Graph(
                figure=fig_map,
                style={"height": "80vh", "width": "90%"}
            ) 
        ]),
        dcc.Tab(label="Histogramme", children=[
            dcc.Graph(figure=fig_histogram)
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)