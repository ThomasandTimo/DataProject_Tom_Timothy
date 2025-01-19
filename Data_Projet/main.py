import dash
from dash import html, dcc
import plotly.express as px
from src.utils.get_data import load_sheet  # Importer la fonction de get_data.py
from src.utils.clean_data import clean_data  # Importer la fonction de get_data.py

# region Data load

# Nettoyer et charger les données à partir de get_data.py
clean_data("data/raw/rawdata.xlsx", "data/cleaned/cleaned_data.xlsx")
file_path = "data/cleaned/cleaned_data.xlsx"  # Chemin vers le fichier Excel NEttoyé
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

# Ajouter un style CSS externe pour personnalisation
app.css.config.serve_locally = True
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap",
        "rel": "stylesheet",
    }
]

# Layout du dashboard
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f4f9",
        "fontFamily": "Roboto, sans-serif",
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "#ff5e5b",
                "padding": "1rem",
                "textAlign": "center",
                "color": "white",
            },
            children=[
                html.H1(
                    "Dashboard des Catastrophes Naturelles (2000-2024)",
                    style={"margin": "0", "fontSize": "2.5rem"},
                ),
                html.P(
                    "Une analyse des catastrophes naturelles et de leur impact dans le monde",
                    style={"marginTop": "0.5rem", "fontSize": "1.2rem"},
                ),
            ],
        ),
        html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "background": "url('https://via.placeholder.com/1920x1080') center/cover no-repeat",
                "height": "25vh",
            },
            children=[
                html.Div(
                    style={"background": "rgba(0,0,0,0.6)", "padding": "2rem", "borderRadius": "10px"},
                    children=[
                        html.H2(
                            "Visualisation des Données",
                            style={"color": "white", "fontSize": "2rem"},
                        ),
                        html.P(
                            "Explorez les données interactives sur les catastrophes naturelles",
                            style={"color": "#dcdcdc"},
                        ),
                    ],
                )
            ],
        ),
        dcc.Tabs(
            style={"margin": "1rem"},
            children=[
                dcc.Tab(
                    label="Carte", 
                    style={"padding": "1rem"},
                    children=[
                        dcc.Graph(
                            figure=fig_map,
                            style={"height": "80vh", "width": "100%"}
                        ) 
                    ]
                ),
                dcc.Tab(
                    label="Histogramme", 
                    style={"padding": "1rem"},
                    children=[
                        dcc.Graph(figure=fig_histogram)
                    ]
                )
            ],
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)
