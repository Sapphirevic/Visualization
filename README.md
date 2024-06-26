# Visualization
Dash Plotly


# **Project Overview**

The Job Data Visualization Dashboard is designed to provide insightful and interactive visual representations of diverse job category and the salaries. The dashboard leverages data from a kaggle job dataset which is now named cleaned data to present various charts and plots. 

# Project SetUp
## **Step 1: Navigate to the src model**

       cd src

### Create a Virtual Environment
Setup a local environment using: 
```bash
python -m venv env
```

### Activate the Virtual Environment

On Windows run: 
```bash
env\\Scripts\\activate
```

On macOS/Linux run: 
```bash
source env/bin/activate
```

### Important

For dependency updates, please run the following command whenever a new dependency is added:
```bash
pip freeze > requirements.txt
```
This will update the \`requirements.txt\` for easy setup in a different working environment.

Dependencies have been included in \`requirements.txt\`. Install them using:
```bash
pip install -r requirements.txt
```

## **Step 2: Navigate to the dash_app module**

       cd dash_app


### Running the app
```bash
python app.py