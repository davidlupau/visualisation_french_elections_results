import pandas as pd
from data_processing import save_analysis_to_excel
from constants import candidates_full_names

def explore_dataset_quality(df):
    """
    Retrieve basic information about the dataset quality.
    param:
        df
    return:
        Information about the dataset quality.
        Two Excel files are saved: basic information about the dataset and % of null values in each column
    """
    print("Basic information about dataset:\n")
    # Get a summary of the dataset
    print(df.info())

    # Get descriptive statistics for numerical columns in a csv file
    print("Retrieving basic information from the dataset\n ")
    describe_dataset = df.describe(include='all')
    # Save to an Excel file
    save_analysis_to_excel(describe_dataset, 'dataset_quality.xlsx')

    # Calculate missing values in each column
    print("Calculating the percentage of null values for in each column.\n")
    missing_percentage = df.isnull().mean() * 100

    # Save to an Excel file
    save_analysis_to_excel(missing_percentage, 'missing_percentage.xlsx')


def calculate_national_candidate_scores(df):
    """
    Calculates national candidate scores as percentage of total votes.
    Returns a sorted DataFrame with columns 'candidate' and 'score'.
    """
    print("Calculating candidate scores on national level (sorted by score)...\n")
    scores = []

    for i in range(1, 13):
        vote_col = f"candidate_{i}_votes"
        full_name_key = f"candidate_{i}_full_name"
        full_name = candidates_full_names.get(full_name_key, f"Candidate {i}")

        total_votes = df[vote_col].sum()
        total_voters = df["total_voters"].sum()

        score = round((total_votes / total_voters) * 100, 2)
        scores.append({"candidate": full_name, "score": score})

    df_scores = pd.DataFrame(scores)
    df_scores = df_scores.sort_values(by="score", ascending=False).reset_index(drop=True)

    return df_scores


def national_abstention_null_invalid(df):
    """
    Calculate the national abstention null invalid.
    param:
        df
    return:
        Display percentage of national abstention, null and invalid votes.
    """
    print("Calculating abstention, null and invalid votes on national level...\n")
    abstention_pct = df["abstention"].sum() / df["total_registered_voters"].sum() * 100
    null_pct = df["blank_votes"].sum() / df["total_voters"].sum() * 100
    invalid_pct = df["invalid_votes"].sum() / df["total_voters"].sum() * 100

    print(f"Abstention: {round(abstention_pct, 2)}% of registered voters. \n")
    print(f"Null votes: {round(null_pct, 2)}% of votes.\n")
    print(f"Invalid votes: {round(invalid_pct, 2)}% of votes.\n")


def scores_by_political_side(df):
    """Calculate political side scores using vote totals"""

    # Sum actual votes by political side
    political_totals = df.groupby('political_side')['votes'].sum().reset_index()

    # Calculate total votes (all candidates combined)
    total_votes = political_totals['votes'].sum()

    # Calculate percentages
    political_totals['percentage'] = (political_totals['votes'] / total_votes * 100).round(2)

    # Sort by percentage, descending
    result = political_totals.sort_values('percentage', ascending=False)

    print("Scores by political side:")
    for _, row in result.iterrows():
        print(f"{row['political_side']}: {row['percentage']}%")

    return result
