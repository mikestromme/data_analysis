import pandas as pd
import requests


""" url = 'https://example.com/car_sales.csv'
response = requests.get(url)
with open('car_sales.csv', 'wb') as file:
    file.write(response.content)

df = pd.read_csv('car_sales.csv') """


# insert file to dataframe
file_path = 'aviation-accident-data-2023-05-16.csv'
df = pd.read_csv(file_path)


# Display the first few rows of the dataset
df.head()

# Check the column names and data types
df.info()

# Get summary statistics of the dataset
df.describe()

# Check for missing values in each column
df.isnull().sum()


# Check for missing values in each column
df.isnull().sum()

# Remove rows with missing values
df_clean = df.dropna()

# Fill missing values with appropriate values
df_filled = df.fillna(value=0)  # Replace missing values with 0

# Use imputation techniques to fill missing values
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')  # Use mean imputation
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)


