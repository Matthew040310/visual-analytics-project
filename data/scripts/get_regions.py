import pandas as pd
from pathlib import Path

data_dir = Path(__file__).resolve().parent.parent
data = pd.read_csv(data_dir / "processed" / "cqi_2023_cleaned.csv")

country_region = (
    data[['Country_of_Origin', 'Region_Clean']]
    .dropna()
    .drop_duplicates()
    .sort_values(
        ['Country_of_Origin', 'Region_Clean'],
        ascending=True
    )
    .reset_index(drop=True)
)

country_region.to_csv(data_dir / "reference" / "regions.csv", index=False)