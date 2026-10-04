from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data"


def load_data():

    return {

        "orders":
            pd.read_csv(DATA_DIR / "orders.csv"),

        "products":
            pd.read_csv(DATA_DIR / "products.csv"),

        "inventory":
            pd.read_csv(DATA_DIR / "inventory.csv"),

        "shipments":
            pd.read_csv(DATA_DIR / "shipments.csv"),

        "exceptions":
            pd.read_csv(DATA_DIR / "exceptions.csv"),

        "transfers":
            pd.read_csv(DATA_DIR / "transfers.csv")
    }