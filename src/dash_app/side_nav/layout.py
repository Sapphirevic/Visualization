import dash_bootstrap_components as dbc
from dash import dcc, html
from space.overview.layout import overview_layout
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

sidebar = html.Div(
    [
        html.H4("Company Data Analysis"),
        html.Hr(),
        html.P("Choose one from the optional views listed below:"),
        dbc.Button(
            "Overview",
            id="btn-overview",
            color="primary",
            className="mb-3",
            style={"flex": 1, "gap": "10px"},
        ),
        dbc.Button(
            "Detailed Analysis",
            id="btn-detailed-analysis",
            color="primary",
            className="mb-3",
            style={"flex": 1, "gap": "10px"},
        ),
        dbc.Button(
            "Comparison",
            id="btn-comparison",
            color="primary",
            className="mb-3",
            style={"flex": 1, "gap": "10px"},
        ),
        dbc.Button(
            "Choropleth Map",
            id="btn-choropleth-map",
            color="primary",
            className="mb-3",
            style={"flex": 1, "gap": "10px"},
        ),
    ],
    style={
        "width": "20%",
        "background-color": "black",
        "border-radius": "10px",
        "padding": "10px",
        "height": "min-content",
        "display": "flex",
        "flex-direction": "column",
    },
)

content = html.Div(
    id="page-content",
    style={"flex": 1, "overflow-y": "scroll", "height": "100%"},
    children=[overview_layout()],
)

def company_side_nav():
    return html.Div(
        [sidebar, content],
        style={"display": "flex", "height": "100%", "gap": "20px"},
    )
