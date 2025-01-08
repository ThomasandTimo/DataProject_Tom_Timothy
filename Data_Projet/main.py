import dash
from dash import html, dcc
import plotly.express as px
from src.utils.get_data import load_sheet  # Importer la fonction de get_data.py

# Charger les données à partir de get_data.py
file_path = "data/raw/rawdata.xlsx"  # Chemin vers ton fichier Excel
sheet_name = "EM-DAT Data"  # Nom de la feuille
data = load_sheet(file_path)  # Appel à la fonction load_sheet

if data is None:
    raise ValueError("Les données n'ont pas pu être chargées. Vérifiez le chemin ou le fichier.")

# Regrouper les catastrophes par pays
catastrophes_par_pays = data.groupby("Country").size().reset_index(name="Count")

# Créer une carte choroplèthe
fig = px.choropleth(
    catastrophes_par_pays,
    locations="Country",
    locationmode="country names",
    color="Count",
    title="Nombre de Catastrophes par Pays",
    color_continuous_scale="Reds"
)

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Layout du dashboard
app.layout = html.Div([
    html.H1("Dashboard des Catastrophes Naturelles"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)