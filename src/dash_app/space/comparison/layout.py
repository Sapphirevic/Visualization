from dash import dcc, html

def comparison_layout():
    return html.Div(
        [
            dcc.Graph(id='comparison-heatmap'),
            dcc.Graph(id='comparison-scatter-matrix'),
            dcc.Graph(id='comparison-bubble-chart')
        ],
        style={"padding": "20px"},
    )
