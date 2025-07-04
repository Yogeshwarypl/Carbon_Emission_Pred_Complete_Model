import pandas as pd

def load_dataset(path):
    """Load dataset from CSV file."""
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
