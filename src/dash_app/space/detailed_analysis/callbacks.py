import pandas as pd
import plotly.express as px
from dash import Input, Output

# Load your data
df = pd.read_csv('C:/Users/2024/plotly/Visualization/src/data/cleaned_data.csv')

def register_detailed_analysis_callbacks(app):
    @app.callback(
        Output('detailed-box-plot', 'figure'),
        Input('btn-detailed-analysis', 'n_clicks')
    )
    def update_detailed_box_plot(n_clicks):
        fig = px.box(df, x='job_category', y='salary_in_usd', color='experience_level', title='Salary Distribution by Job Category and Experience Level')
        print(type(fig))  # Check the type of fig
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        return fig

    @app.callback(
        Output('detailed-violin-plot', 'figure'),
        Input('btn-detailed-analysis', 'n_clicks')
    )
    def update_overview_violin_plot(n_clicks):
        fig = px.violin(df, x='job_category', y='salary_in_usd', color='job_category', title='Salary Distribution by Job Category')
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        return fig