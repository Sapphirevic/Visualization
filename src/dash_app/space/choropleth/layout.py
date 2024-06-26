from dash import dcc, html

def choropleth_map_layout():
    return html.Div(
        [
            dcc.Graph(id='choropleth-map'),
        ],
        style={"padding": "20px"},
    )
