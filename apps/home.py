from dash import Dash, html, dcc, Output, Input, callback, dash_table
# import pandas as pd
# import plotly.express as px  # (version 4.7.0)
# from app import app

layout = html.Div([
    html.Div([
        html.Div([
            html.H1("Halo", style={'text-align': 'center', 'color': "white", 'padding-left': "500px",
                                   'padding-top': "250px", 'font-family': "Tahoma", 'font-size': "64px"}),
            html.H4("Kami dari kelompok 145 yang beranggotakan aya, azka, diah dan ridho."
                    "Ini adalah dashboard web untuk project terakhir di RuangGuru bootcamp ",
                    style={'text-align': 'center', 'color': "white", 'padding-left': "700px", 'padding-right': "200px",
                           'font-family': "Tahoma"}),
        ]),
    ], style={'display': "flex", 'background-image': "url('/assets/zzz.gif')", 'background-size': 'cover',
              'height': '100vh', 'width': '100%'})
], style={'height': "auto", 'background-color': "black", 'width': "100%"})
