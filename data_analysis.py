import pandas as pd
import requests

url = 'https://example.com/car_sales.csv'
response = requests.get(url)
with open('car_sales.csv', 'wb') as file:
    file.write(response.content)

df = pd.read_csv('car_sales.csv')





