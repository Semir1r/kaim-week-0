## This project aims to analyze solar irradiance data from three countries (Benin, Togo, Sierra Leone) by identifying trends, detecting outliers, and visualizing key relationships.
<!-- 
As part of this project, comprehensive Exploratory Data Analysis (EDA) will be conducted to gain insights into the dataset and prepare it for further analysis. Below is an overview of the key steps and methodologies that will be applied:

1. Summary Statistics
We will calculate key descriptive statistics, including mean, median, standard deviation, minimum, and maximum values for all numeric columns. This will help us:

Understand the overall distribution of each variable.
Identify potential issues such as extreme outliers or unexpected ranges.
2. Data Quality Check
Missing Values: Examine the dataset for missing or null values and document their occurrence. Handle these values by imputation or removal based on context.
Outliers: Identify and flag outliers in critical columns like GHI, DNI, and DHI using:
Statistical methods (e.g., Z-scores or IQR).
Visual methods (e.g., boxplots).
Incorrect Entries: Detect physically impossible values, such as negative irradiance values, and address these anomalies.
3. Time Series Analysis
Using time-based plots (line or bar charts), we will analyze:

Monthly patterns in GHI, DNI, DHI, and Tamb to identify seasonal trends.
Daily trends to observe peaks in solar irradiance or fluctuations in temperature.
Anomalies in solar or temperature readings that deviate significantly from expected patterns.
4. Impact of Cleaning
Evaluate the effect of cleaning operations (indicated in the Cleaning column) on sensor readings (ModA, ModB) by comparing data before and after cleaning over time.

5. Correlation Analysis
We will compute and visualize correlations to uncover relationships between variables:

Use correlation matrices and pair plots to analyze the association between solar radiation components (GHI, DNI, DHI) and temperature (TModA, TModB).
Explore how wind conditions (WS, WSgust, WD) influence solar irradiance using scatter matrices.
6. Wind Analysis
Using radial bar plots or wind roses, we will:

Visualize the distribution of wind speed (WS) and direction (WD).
Highlight trends in wind behavior and identify significant wind events.
7. Temperature Analysis
Analyze the interaction between temperature (Tamb) and relative humidity (RH):

Investigate how RH impacts temperature readings.
Examine how variations in RH influence solar radiation (GHI, DNI, DHI).
8. Histograms
Create histograms for variables like GHI, DNI, DHI, WS, and temperature to:

Visualize frequency distributions.
Detect skewness, uniformity, or multimodal patterns in the data.
9. Z-Score Analysis
Compute Z-scores for all numeric columns to flag data points significantly different from the mean. These will be treated as potential outliers and reviewed for validity.

10. Bubble Charts
Leverage bubble charts to explore complex relationships between variables, such as:

GHI vs. Tamb vs. WS, with bubble size representing relative humidity (RH) or barometric pressure (BP).
Identify clusters or patterns that suggest interactions among these variables.
11. Data Cleaning
Based on the above analyses:

Handle missing values and outliers appropriately.
Remove or rectify anomalies (e.g., negative irradiance values).
Drop irrelevant or entirely null columns like Comments if they add no value to the analysis.
Outcome
By following this structured approach to EDA, the dataset will be thoroughly analyzed and cleaned. This will ensure high-quality data that is ready for further modeling and insights extraction. Detailed findings and visualizations from each step will be documented to facilitate reproducibility and understanding. -->