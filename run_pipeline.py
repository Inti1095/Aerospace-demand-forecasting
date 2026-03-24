import pandas as pd
from src.data_processing import load_data, clean_data, save_processed_data
from src.feature_engineering import create_time_features
from src.forecasting_model import train_arima_model, forecast

# Step 1: Load data
df = load_data("data/raw/data.csv")

# Step 2: Clean data
df = clean_data(df)

# Step 3: Feature engineering
df = create_time_features(df, "date")

# Step 4: Train model
model = train_arima_model(df["demand"])

# Step 5: Forecast
future_forecast = forecast(model, steps=10)

# Step 6: Save output
forecast_df = pd.DataFrame({"forecast": future_forecast})
forecast_df.to_csv("outputs/forecasts.csv", index=False)

print("Pipeline executed successfully!")
