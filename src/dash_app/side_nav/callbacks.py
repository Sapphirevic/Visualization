import dash
from dash import Input, Output, State
from space.overview.layout import overview_layout
from space.detailed_analysis.layout import detailed_analysis_layout
from space.comparison.layout import comparison_layout
from space.choropleth.layout import choropleth_map_layout
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))


def company_side_nav_callback(app):
    @app.callback(
        [
            Output("page-content", "children"),
            Output("btn-overview", "style"),
            Output("btn-detailed-analysis", "style"),
            Output("btn-comparison", "style"),
            Output("btn-choropleth-map", "style")
        ],
        [
            Input("btn-overview", "n_clicks"),
            Input("btn-detailed-analysis", "n_clicks"),
            Input("btn-comparison", "n_clicks"),
            Input("btn-choropleth-map", "n_clicks")
        ],
        [State("page-content", "children")]
    )
    def display_page(btn_overview, btn_detailed_analysis, btn_comparison, btn_choropleth_map, children):
        ctx = dash.callback_context

        if not ctx.triggered:
            button_id = 'btn-overview'
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        button_styles = {
            "btn-overview": {"color": "white", "background-color": "blue"},
            "btn-detailed-analysis": {"color": "white", "background-color": "blue"},
            "btn-comparison": {"color": "white", "background-color": "blue"},
            "btn-choropleth-map": {"color": "white", "background-color": "blue"}
        }

        if button_id == 'btn-overview':
            content = overview_layout()
        elif button_id == 'btn-detailed-analysis':
            content = detailed_analysis_layout()
        elif button_id == 'btn-comparison':
            content = comparison_layout()
        elif button_id == 'btn-choropleth-map':
            content = choropleth_map_layout()
        else:
            content = overview_layout()

        for btn in button_styles.keys():
            if btn == button_id:
                button_styles[btn]["background-color"] = "red"

        return content, button_styles["btn-overview"], button_styles["btn-detailed-analysis"], button_styles["btn-comparison"], button_styles["btn-choropleth-map"]
