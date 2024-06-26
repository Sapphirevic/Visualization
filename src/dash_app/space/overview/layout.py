from dash import dcc, html
import dash_bootstrap_components as dbc

def overview_layout():
    return html.Div([
        html.H2("Overview", style={'textAlign': 'center', 'color': 'white'}),
        dbc.Button("Update Overview", id='btn-overview', color='primary'),
        dcc.Graph(id='overview-line-chart'),
        dcc.Graph(id='overview-bar-chart'),
        dcc.Graph(id='overview-histogram'),
    ],
        style={"padding": "20px"},
    )
