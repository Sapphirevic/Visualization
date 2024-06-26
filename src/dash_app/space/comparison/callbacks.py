import pandas as pd
import plotly.express as px
from dash import Input, Output
import plotly.graph_objects as go

# Load your data
df = pd.read_csv('C:/Users/2024/plotly/Visualization/src/data/cleaned_data.csv')

def register_comparison_callbacks(app):
    @app.callback(
        Output('comparison-heatmap', 'figure'),
        Input('btn-comparison', 'n_clicks')
    )
    def update_comparison_heatmap(n_clicks):
        pivot_table = df.pivot_table(values='salary_in_usd', index='job_category', columns='work_year', aggfunc='mean')
        figu = px.imshow(pivot_table, title='Average Salary Heatmap by Job Category and Work Year')
        figu.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        return figu

    # def register_comparison_callbacks(app):
def register_comparison_scatter_plot_callbacks(app):
    @app.callback(
        Output('comparison-scatter-plot', 'figure'),
        Input('btn-comparison', 'n_clicks')
    )
    def register_comparison_scatter_plot(n_clicks):
        figs = px.scatter(df, x='salary_in_usd', y='work_year', color='job_category', title='Salary vs. Year by Job Category')
        print(type(figs))  # Check the type of fig
        figs.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        return figs

df['num_employees'] = df['company_size'].apply(lambda x: 100 if x == 'Large' else (50 if x == 'Medium' else 20))

def register_bubble_chart_callbacks(app):
    @app.callback(
        Output('comparison-bubble-chart', 'figure'),
        Input('btn-comparison', 'n_clicks')
    )
    def update_comparison_bubble_chart(n_clicks):
        max_num_employees = df['num_employees'].max()
        fig = go.Figure()

        for job_title in df['job_title'].unique():
            filtered_df = df[df['job_title'] == job_title]
            bubble_sizes = filtered_df['num_employees'] / max_num_employees
            
            fig.add_trace(go.Scatter(
                x=filtered_df['company_size'],
                y=[0] * len(filtered_df),
                mode='markers',
                marker=dict(
                    size=bubble_sizes,
                    line=dict(width=2),
                    opacity=0.8
                ),
                name=job_title
            ))

        fig.update_layout(
            title='Job Titles vs. Company Size',
            xaxis_title='Company Size',
            yaxis_title='Employees',
            legend_title='Job Title',
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )

        return fig
