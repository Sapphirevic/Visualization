import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from side_nav.layout import company_side_nav
from side_nav.callbacks import company_side_nav_callback
from space.overview.callbacks import register_overview_callbacks
from space.detailed_analysis.callbacks import register_detailed_analysis_callbacks
from space.comparison.callbacks import (register_comparison_callbacks, register_bubble_chart_callbacks, register_comparison_scatter_plot_callbacks)
from space.choropleth.callbacks import register_choropleth_map_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src="https://via.placeholder.com/150", height="30px")),
                    dbc.Col(dbc.NavbarBrand("Company Data Analysis", className="ms-2")),
                ],
                align="center",
                className="g-0",
                justify="center",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
        ]
    ),
    color="dark",
    dark=True,
)

app.layout = html.Div([header, company_side_nav()])

company_side_nav_callback(app)
register_overview_callbacks(app)
register_detailed_analysis_callbacks(app)
register_comparison_callbacks(app)
register_choropleth_map_callbacks(app)
register_bubble_chart_callbacks(app)
register_comparison_scatter_plot_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
