# import pandas as pd
# import plotly.express as px
# from dash import Input, Output

# # Load your data
# df = pd.read_csv('C:/Users/2024/plotly/Visualization/src/data/cleaned_data.csv')

import pandas as pd
import plotly.express as px
from dash import Input, Output
# from services.data_processing import df

df = pd.read_csv('C:/Users/2024/plotly/Visualization/src/data/cleaned_data.csv')
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')

average_salary = df['salary_in_usd'].mean()
highest_paid_job_title = df.groupby('job_title')['salary_in_usd'].max().idxmax()

print(f"Average Salary: {average_salary}")
print(f"Highest Paid Job Title: {highest_paid_job_title}")


def register_overview_callbacks(app):
    @app.callback(
        Output('overview-line-chart', 'figure'),
        Input('btn-overview', 'n_clicks')
    )
    def update_overview_line_chart(n_clicks):
        fig = px.line(df, x='work_year', y='salary_in_usd', color='job_category', title='Salary Trends Over Years by Job Category')
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        return fig

    @app.callback(
        Output('overview-bar-chart', 'figure'),
        Input('btn-overview', 'n_clicks')
    )
    def update_overview_bar_chart(n_clicks):
        fig = px.bar(df, x='job_category', y='salary_in_usd', color='employment_type', title='Average Salary by Job Category and Employment Type')
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        return fig

    

    @app.callback(
    Output('overview-histogram', 'figure'),
    Input('btn-overview', 'n_clicks')
    )
    def update_overview_histogram(n_clicks):
        job_categories = [
            'Data Science and Research',
            'Data Analysis',
            'Data Engineering',
            'Data Architecture and Modeling',
            'Data Management Strategy',
            'Data Quality and Operations',
            'Leadership and Management',
            'Machine Learning and AI',
            'BI and Visualization'
        ]
        
        filtered_df = df[df['job_category'].isin(job_categories)]
        
        fig = px.histogram(filtered_df, x="experience_level", y="salary_in_usd",
                        color="job_category",
                        labels={"experience_level": "Experience Level", "salary_in_usd": "Salary"},
                        title='Salary Distribution by Experience Level and Job Category',
                        nbins=20)
        
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
            legend_title_font_color='white'
        )
        
        fig.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(label="All Categories",
                            method="restyle",
                            args=[{"visible": [True] * len(filtered_df)}]),
                        dict(label="Data Science and Research",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Data Science and Research' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Data Analysis",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Data Analysis' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Data Engineering",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Data Engineering' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Data Architecture and Modeling",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Data Architecture and Modeling' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Data Management Strategy",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Data Management Strategy' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Data Quality and Operations",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Data Quality and Operations' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Leadership and Management",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Leadership and Management' else False for cat in filtered_df['job_category']]}]),
                        dict(label="Machine Learning and AI",
                            method="restyle",
                            args=[{"visible": [True if cat == 'Machine Learning and AI' else False for cat in filtered_df['job_category']]}]),
                        dict(label="BI and Visualization",
                            method="restyle",
                            args=[{"visible": [True if cat == 'BI and Visualization' else False for cat in filtered_df['job_category']]}]),
                    ]),
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.1,
                    xanchor="left",
                    y=1.1,
                    yanchor="top"
                )
            ]
        )
        
        return fig
