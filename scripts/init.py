import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

def summary_statistics(df):
    """Calculate summary statistics for each numeric column."""
    return df.describe()

def data_quality_check(df):
    """Check for missing values, outliers, and invalid entries."""
    # Check for missing values
    missing_values = df.isnull().sum()
    
    # Check for negative values where only positives should exist (for GHI, DNI, DHI, WS, WSgust)
    invalid_values = (df[['GHI', 'DNI', 'DHI', 'WS', 'WSgust']] < 0).sum()
    
    # Identify outliers using IQR for numeric columns (GHI, DNI, DHI, ModA, ModB, WS, WSgust)
    Q1 = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']].quantile(0.25)
    Q3 = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']] < (Q1 - 1.5 * IQR)) |
                (df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']] > (Q3 + 1.5 * IQR)))
    
    return missing_values, invalid_values, outliers

def time_series_analysis(df):
    """Plot time series data for GHI, DNI, DHI, Tamb over time."""
    df['Time'] = pd.to_datetime(df['Time'])  # Ensure 'Time' column is in datetime format
    df.set_index('Time', inplace=True)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    axes[0, 0].plot(df.index, df['GHI'], label='GHI', color='tab:orange')
    axes[0, 0].set_title('GHI Over Time')
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('GHI')
    
    axes[0, 1].plot(df.index, df['DNI'], label='DNI', color='tab:red')
    axes[0, 1].set_title('DNI Over Time')
    axes[0, 1].set_xlabel('Time')
    axes[0, 1].set_ylabel('DNI')
    
    axes[1, 0].plot(df.index, df['DHI'], label='DHI', color='tab:blue')
    axes[1, 0].set_title('DHI Over Time')
    axes[1, 0].set_xlabel('Time')
    axes[1, 0].set_ylabel('DHI')
    
    axes[1, 1].plot(df.index, df['Tamb'], label='Tamb', color='tab:green')
    axes[1, 1].set_title('Tamb Over Time')
    axes[1, 1].set_xlabel('Time')
    axes[1, 1].set_ylabel('Tamb')
    
    plt.tight_layout()
    plt.show()

def cleaning_impact(df):
    """Evaluate the impact of cleaning on sensor readings (ModA, ModB)."""
    fig, axes = plt.subplots(2, 1, figsize=(15, 10))
    
    axes[0].plot(df[df['Cleaning'] == 1].index, df[df['Cleaning'] == 1]['ModA'], label='Cleaning Applied', color='tab:purple', linestyle='-', alpha=0.7)
    axes[0].plot(df[df['Cleaning'] == 0].index, df[df['Cleaning'] == 0]['ModA'], label='No Cleaning', color='tab:gray', linestyle='--', alpha=0.7)
    axes[0].set_title('ModA Sensor Readings - Cleaning vs No Cleaning')
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel('ModA')
    axes[0].legend()
    
    axes[1].plot(df[df['Cleaning'] == 1].index, df[df['Cleaning'] == 1]['ModB'], label='Cleaning Applied', color='tab:purple', linestyle='-', alpha=0.7)
    axes[1].plot(df[df['Cleaning'] == 0].index, df[df['Cleaning'] == 0]['ModB'], label='No Cleaning', color='tab:gray', linestyle='--', alpha=0.7)
    axes[1].set_title('ModB Sensor Readings - Cleaning vs No Cleaning')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('ModB')
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()

def correlation_analysis(df):
    """Generate correlation matrix and pair plot."""
    corr_matrix = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'WS', 'WSgust']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

    # Pairplot for selected columns
    sns.pairplot(df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB']])
    plt.show()

def wind_analysis(df):
    """Generate wind rose plot."""
    # Wind rose plot to visualize wind speed and direction
    # Assuming `WD` is the wind direction and `WS` is the wind speed
    wind_direction = df['WD']
    wind_speed = df['WS']
    
    # Plotting wind rose
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection='polar')
    ax.bar(np.radians(wind_direction), wind_speed, width=0.1, bottom=0.0)
    ax.set_title('Wind Rose', va='bottom')
    plt.show()

def zscore_analysis(df):
    """Calculate Z-scores for numeric columns to flag outliers."""
    z_scores = np.abs(zscore(df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']]))
    outliers = (z_scores > 3).sum(axis=0)
    return outliers

def bubble_chart(df):
    """Create a bubble chart for GHI vs Tamb vs WS with bubble size representing RH."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['GHI'], df['Tamb'], s=df['RH'] * 10, c=df['WS'], cmap='viridis', alpha=0.5)
    plt.title('GHI vs Tamb vs WS (Bubble Size: RH)')
    plt.xlabel('GHI')
    plt.ylabel('Tamb')
    plt.colorbar(label='Wind Speed (WS)')
    plt.show()

def handle_missing_data(df):
    """Handle missing data by dropping or imputing."""
    # You can drop rows with missing critical columns or impute based on the mean/median
    df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust'])
    return df
