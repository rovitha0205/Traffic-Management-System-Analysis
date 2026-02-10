
import pandas as pd

# Load raw dataset
df = pd.read_excel("chennai_raw_uncleaned_dataset.xlsx")


df["state"] = df["state"].replace({
    "TN": "Tamil Nadu",
    "TamilNadu": "Tamil Nadu"
})


df["zone"] = df["zone"].str.strip()


df["ID"] = df["ID"].fillna(method="ffill")


df["its"] = df["its"].astype(str).str.capitalize()
df["its"] = df["its"].replace({
    "Yes": "Yes",
    "No": "No",
    "Partial": "Partial",
    "None": "No"
})


numerical_columns = [
    "population",
    "signal_coverage",
    "cameras",
    "commute_time"
]

for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())


df = df.rename(columns={
    "state": "State",
    "region_name": "Region",
    "zone": "Zone_District",
    "population": "Population",
    "vehicle_density": "Vehicle_Density_veh_per_km",
    "accident_rate": "Accident_Rate_per_100k",
    "signal_coverage": "Traffic_Signal_Coverage_percent",
    "its": "ITS_Deployed",
    "cameras": "Num_Traffic_Cameras",
    "commute_time": "Avg_Commute_Time_mins"
})


df.to_excel("chennai_traffic_cleaned.xlsx", index=False)

print("Data preprocessing completed successfully.")
