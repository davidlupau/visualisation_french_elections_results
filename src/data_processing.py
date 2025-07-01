import pandas as pd
from pathlib import Path

# === LOADING AND SAVING FILES ===
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
    print(f"Saving analysis to {file_name}...\n")
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

# === ADDING COLUMNS ===
def candidate_full_names_column(df):
    """
    Create a new column with the full name of the candidates
    param:
        Dataframe containing the candidates first and last name
    return:
        DataFrame with a new column with the full name of the candidates
    """
    print("Creating new column with candidate full names... \n")
    for i in range(1, 13):
        first_name_col = f"candidate_{i}_first_name"
        surname_col = f"candidate_{i}_surname"
        full_name_col = f"candidate_{i}_full_name"
        df[full_name_col] = df[first_name_col] + " " + df[surname_col].str.title()

    print("Columns created. \n")
    return df

def candidate_political_side_column(df, mapping):
    print("Creating new column with candidate political side... \n")
    for i in range(1, 13):
        surname_col = f"candidate_{i}_surname"
        political_side_col = f"candidate_{i}_political_side"
        df[political_side_col] = df[surname_col].map(mapping)

    print("Columns created. \n")
    return df

# === CREATING AND MODIFYING DATAFRAMES ===
def create_df_by_candidate(df, base_cols):
    """
    Create a new dataframe with candidate candidates. All candidate names in the same column.
    param
        df: original dataframe created after uploading dataset
        base_cols: a list of columns from df that we want to keep
    return:
        dataframe with candidate names in a single
    """
    print("Creating new dataframe with consolidated candidate names... \n")
    # Create empty list to store our long-format rows
    long_data = []

    # For each department (row in original data)
    for idx, row in df.iterrows():
        dept_info = {col: row[col] for col in base_cols}

        # For each candidate (1 to 12)
        for candidate_num in range(1, 13):
            votes_col = f'candidate_{candidate_num}_votes'
            votes_pct_col = f'candidate_{candidate_num}_votes_pct_voters'
            name_col = f'candidate_{candidate_num}_full_name'
            pol_side_col = f'candidate_{candidate_num}_political_side'

            # Create one row per department-candidate combination
            candidate_row = dept_info.copy()
            candidate_row['candidate_name'] = row[name_col]
            candidate_row['votes'] = row[votes_col]
            candidate_row['votes_pct_voters'] = row[votes_pct_col]
            candidate_row['political_side'] = row[pol_side_col]

            long_data.append(candidate_row)

    # Convert to DataFrame
    df_long = pd.DataFrame(long_data)
    print("New dataframe created. \n")
    return df_long


def add_department_type_column(df):
    """
    Adds a 'dpt_type' column to the DataFrame based on department codes.

    Parameters:
        df (pd.DataFrame): DataFrame with department data
    Returns:
        pd.DataFrame: DataFrame with added 'dpt_type' column
    """

    # Make a copy to avoid modifying the original
    df = df.copy()

    df['dpt_type'] = df['department_code'].apply(lambda code:
                                                    'French living abroad' if code == 'ZZ' else
                                                    'Corsica' if code in ['2A', '2B'] else
                                                    'Overseas' if code in [971, 972, 973, 974, 976, 988,
                                                                        987, 975, 986, 977] else
                                                    'Metropolitan'
                                                    )

    return df

def categorisation_dpt_size(df):
    """
    Create a new column with department size category i.e. smallest, small, large, largest.
    parameter: df
    return: df with new column with department size category
    """
    print("Creating new column with categorical department size... \n")
    df["population_group"] = pd.qcut(
        df["total_registered_voters"],
        q=4,
        labels=["Smallest", "Small", "Large", "Largest"]
    )
    return df


import pandas as pd
import numpy as np

import pandas as pd
import numpy as np


def determine_winning_political_side(df):
    """
    Determine the winning political side for each department based on highest vote count.
    Parameters:
        df: DataFrame with candidate vote data and political sides
    Returns:
        DataFrame with department_code, department_name, winning_political_side, and abstention_rate
    """
    print("Determining winning political sides...")

    results = []

    for _, row in df.iterrows():
        # Get all candidate vote counts and their political sides
        candidate_votes = []

        for i in range(1, 13):  # candidates 1-12
            votes = row[f'candidate_{i}_votes']
            political_side = row[f'candidate_{i}_political_side']
            candidate_votes.append((votes, political_side))

        # Find the candidate with highest votes
        max_votes, winning_side = max(candidate_votes, key=lambda x: x[0])

        results.append({
            'department_code': row['department_code'],
            'department_name': row['department_name'],
            'winning_political_side': winning_side,
            'abstention_rate': row['abstention_pct_reg']
        })

    result_df = pd.DataFrame(results)

    # Print summary
    print(f"Political sides distribution:")
    side_counts = result_df['winning_political_side'].value_counts()
    for side, count in side_counts.items():
        print(f"  {side}: {count} departments")

    return result_df