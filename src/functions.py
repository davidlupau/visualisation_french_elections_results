import pandas as pd
from pathlib import Path

def load_dataset(file_name):
    """Load the dataset from the excel file
    Parameters:
         file_name (string): name of the excel file in /data folder
    Returns:
        dataframe containing the election results
    """
    print("\nLoading dataset...\n")
    try:
        # Get the project root (go up from src/)
        project_root = Path(__file__).parent.parent
        data_file = project_root / "data" / file_name

        # Check if file exists first
        if not data_file.exists():
            print(f"File not found: {data_file}")
            return None

        df = pd.read_excel(data_file)
        print(f"Successfully loaded {file_name} \n")
        return df
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        return None
