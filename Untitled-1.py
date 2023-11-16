import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Eric', 'Cameron', 'Drew', 'James'],
    'Age': [18, 20, 20, 21],
    'Score': [85, 63, 77, 90],
    'Country': ['US','CA','UK','AU']
}

df = pd.DataFrame(data)
df['Age - Score'] = df['Age'] - df['Score']
print(df)   


