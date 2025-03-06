import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('Tunisair_flights_dataset.csv')

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
profile = ProfileReport(df, title="Tunisair Flights Dataset Report")
profile.to_file("tunisair_flights_report.html")