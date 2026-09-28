import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data - EXACTLY 500 ROWS as promised
housing = fetch_california_housing()
df = pd.DataFrame(housing.data[:500], columns=housing.feature_names)
df['PRICE'] = housing.target[:500]

# Save CSV for GitHub - 500 rows only, ~35KB
df.to_csv('data.csv', index=False)

X = df.drop('PRICE', axis=1)
y = df['PRICE']

model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X, y)

pickle.dump(model, open('model.pkl','wb'))
print("Done! data.csv (500 rows) and model.pkl created")