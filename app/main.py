import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Sidebar
st.title('Solar Radiation Analysis Dashboard')
st.sidebar.header('User Input Parameters')

@st.cache_data
def fetch_data():
    # Load CSV files for each country
    benin = pd.read_csv('data/benin-malanville.csv')
    sierraleone = pd.read_csv('data/sierraleone-bumbuna.csv')
    togo = pd.read_csv('data/togo-dapaong_qc.csv')
    
    # Return as a dictionary
    return {'Benin': benin, 'Sierraleone': sierraleone, 'Togo': togo}

data_dict = fetch_data()

# Sidebar selection for country
st.sidebar.subheader('Country')
country_selected = st.sidebar.selectbox('Select Country', options=list(data_dict.keys()))

# Get data for the selected country
df = data_dict[country_selected]

# Convert 'Timestamp' to datetime if it exists
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Select columns for correlation analysis
columns_for_correlation = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
available_columns = [col for col in columns_for_correlation if col in df.columns]

if len(available_columns) < 2:
    st.warning(f"Not enough data available for correlation analysis in {country_selected}.")
else:
    st.subheader(f"Correlation Analysis for {country_selected}")
    
    # Scatter plot matrix
    scatter_fig = px.scatter_matrix(
        df[available_columns],
        dimensions=available_columns,
        color="GHI",  # Adjust this to a relevant column
        title=f"Correlation Matrix for {country_selected}",
        labels={col: col for col in available_columns},
    )
    st.plotly_chart(scatter_fig)

    # Individual scatter plots
    st.write("### Relationships Between Variables")
    st.write("Scatter plots to explore relationships between variables:")
    
    # Iterate over pairs of variables to create scatter plots
    for x in available_columns:
        for y in available_columns:
            if x != y:
                fig = px.scatter(
                    df,
                    x=x,
                    y=y,
                    size="WSgust" if "WSgust" in df.columns else None,
                    color="WD" if "WD" in df.columns else None,
                    hover_data=available_columns,
                    title=f"{x} vs {y} in {country_selected}",
                )
                st.plotly_chart(fig)