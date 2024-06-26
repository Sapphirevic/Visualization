import pandas as pd
import plotly.express as px
from dash import Input, Output

# Load your data
df = pd.read_csv('C:/Users/2024/plotly/Visualization/src/data/cleaned_data.csv')

def register_choropleth_map_callbacks(app):
    @app.callback(
        Output('choropleth-map', 'figure'),
        Input('btn-choropleth-map', 'n_clicks')
    )
    def update_choropleth_map(n_clicks):
        fig = px.choropleth(
            df,
            locations='company_location',  
            locationmode='country names',  
            color='salary_in_usd',  
            hover_name='company_location',  
            title='Average Salary by Company Location',  
            color_continuous_scale='Viridis',  
            range_color=(df['salary_in_usd'].min(), df['salary_in_usd'].max()),  
            labels={'salary_in_usd': 'Average Salary (USD)'},  
        )
        
        fig.update_geos(
            visible=False,  
            projection_type='equirectangular'  
        )
        
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'  
            )
        )
        
        return fig
