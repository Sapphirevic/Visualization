from dash import dcc, html

def detailed_analysis_layout():
    return html.Div(
        [
            dcc.Graph(id='detailed-box-plot'),
            dcc.Graph(id='detailed-violin-plot'),
        ],
        style={"padding": "20px"},
    )
