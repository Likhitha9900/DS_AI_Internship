import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("kolkata_electricity_consumption.csv")

df.columns = df.columns.str.strip()

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

X = df[[
    "number_of_appliances_used",
    "total_energy_kwh",
    "tariff_rs_per_kwh"
]]

y = df["total_electricity_bill_rs"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

print("\nElectricity Bill Prediction")

appliances = float(input("Enter number of appliances used: "))
energy = float(input("Enter total energy consumption (kWh): "))
tariff = float(input("Enter tariff (Rs/kWh): "))

input_data = pd.DataFrame({
    "number_of_appliances_used": [appliances],
    "total_energy_kwh": [energy],
    "tariff_rs_per_kwh": [tariff]
})

prediction = model.predict(input_data)

print("\nPredicted Electricity Bill: ₹", round(prediction[0], 2))