from dash import Dash, html, dcc, Output, Input, callback, dash_table
import pandas as pd
import plotly.express as px  # (version 4.7.0)
# from app import app
import pathlib


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("datatu.csv"))

fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="totaluser",
                     projection="natural earth",
                     template="plotly_dark")

layout = html.Div([

    html.H2("Marketing", style={'text-align': 'center', 'color': "white", 'margin-top': "0px", 'padding-top': "25px"}),
    html.Div([
        html.H4("Total User", style={'color': "white", 'margin-top': "0px", 'padding-left': "20px"}),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )])
], style={'height': "700px", 'background-color': "black", 'width': "100%"})
