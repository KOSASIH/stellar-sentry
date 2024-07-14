import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stellar Sentry Web App"),
    dcc.Dropdown(
        id="exoplanet-dropdown",
        options=[
            {"label": "Kepler-62f", "value": "Kepler-62f"},
            {"label": "TRAPPIST-1e", "value": "TRAPPIST-1e"},
        ],
        value="Kepler-62f",
    ),
    dcc.Graph(id="exoplanet-orbit-graph"),
    dcc.Graph(id="stellar-system-graph"),
])

@app.callback(
    Output("exoplanet-orbit-graph", "figure"),
    [Input("exoplanet-dropdown", "value")]
)
def update_exoplanet_orbit_graph(exoplanet_name):
    # Retrieve exoplanet data from API or database
    exoplanet_data = [
        {"semi_major_axis": 0.42, "eccentricity": 0.01, "orbital_period": 267.3},
        # ...
    ]
    fig = px.scatter(x="semi_major_axis", y="eccentricity", data=exoplanet_data)
    return fig

@app.callback(
    Output("stellar-system-graph", "figure"),
    [Input("exoplanet-dropdown", "value")]
)
def update_stellar_system_graph(exoplanet_name):
    # Retrieve stellar system data from API or database
    stellar_system_data = [
        {"name": "Kepler-62", "exoplanets": ["Kepler-62f", "Kepler-62g"]},
        # ...
    ]
    fig = px.bar(x="name", y="exoplanets", data=stellar_system_data)
    return fig

if __name__ == "__main__":
    app.run_server()
