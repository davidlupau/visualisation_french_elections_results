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


def save_analysis_to_excel(data, file_name):
    """Save analysis results to Excel file in analysis_output folder
    Parameters:
        data: DataFrame or dict of DataFrames to save
        file_name (str): name of the output Excel file
    Returns:
        str: path to saved file, None if failed
    """
    print(f"\nSaving analysis to {file_name}...\n")
    try:
        # Get the project root (go up from src/)
        project_root = Path(__file__).parent.parent
        output_dir = project_root / "analysis_output"

        # Create directory if it doesn't exist
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / file_name

        if isinstance(data, dict):
            # Multiple sheets
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                for sheet_name, df in data.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            # Single DataFrame
            data.to_excel(output_file, index=False)

        print(f"Successfully saved to {output_file}\n")
        return str(output_file)

    except Exception as e:
        print(f"Error saving {file_name}: {e}")
        return None

def candidate_full_names_column(df):
    print("Creating new column with candidate full names... \n")
    for i in range(1, 13):
        first_name_col = f"candidate_{i}_first_name"
        surname_col = f"candidate_{i}_surname"
        full_name_col = f"candidate_{i}_full_name"
        df[full_name_col] = df[first_name_col] + " " + df[surname_col].str.title()

    print("Columns created. \n")