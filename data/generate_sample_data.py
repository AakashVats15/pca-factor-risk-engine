from pathlib import Path
import pandas as pd
import numpy as np

base = Path(__file__).resolve().parent
raw = base / "raw"
processed = base / "processed"

raw.mkdir(parents=True, exist_ok=True)
processed.mkdir(parents=True, exist_ok=True)

np.random.seed(0)

dates = pd.date_range("2020-01-01", periods=300, freq="B")
assets = [f"A{i}" for i in range(15)]

prices = np.cumprod(1 + np.random.normal(0, 0.01, size=(300, 15)), axis=0) * 100
returns = pd.DataFrame(np.diff(prices, axis=0) / prices[:-1], index=dates[1:], columns=assets)

prices_df = pd.DataFrame(prices, index=dates, columns=assets)
returns_df = returns

universe_df = pd.DataFrame({"ticker": assets})
metadata_df = pd.DataFrame({
    "ticker": assets,
    "sector": np.random.choice(["Tech", "Finance", "Energy", "Health"], size=len(assets)),
    "country": np.random.choice(["US", "DE", "UK", "JP"], size=len(assets))
})

prices_df.to_csv(raw / "prices_raw.csv")
returns_df.to_csv(raw / "returns_raw.csv")
universe_df.to_csv(raw / "universe.csv", index=False)
metadata_df.to_csv(raw / "metadata.csv", index=False)

prices_df.to_csv(processed / "prices.csv")
returns_df.to_csv(processed / "returns.csv")
universe_df.to_csv(processed / "universe.csv", index=False)
metadata_df.to_csv(processed / "metadata.csv", index=False)