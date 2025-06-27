from data_processing import load_dataset, candidate_full_names_column, create_df_by_candidate
from statistical_analysis import explore_dataset_quality, national_abstention_null_invalid, calculate_national_candidate_scores
from constants import base_cols
from visualisations import plot_individual_scores

def main():
    # === DATA LOADING AND PREPARATION ===
    print("=" * 50)
    print("  FRENCH ELECTIONS 2022 - DATA ANALYSIS")
    print("=" * 50)
    # Load dataset into a dataframe
    print("\n=== PREPARING DATA ===")
    file_name = "elections_results_by_department.xlsx"
    df_by_dpt = load_dataset(file_name)

    # Perform basic exploration
    explore_dataset_quality(df_by_dpt)

    # Create new column with candidate full names
    df_by_dpt_full_name = candidate_full_names_column(df_by_dpt)

    # Create a datafram with results by cadidate
    df_by_candidate = create_df_by_candidate(df_by_dpt, base_cols)

    print("\n=== NATIONAL ANALYSIS ===")
    # Calculate national abstention and blank and invalid votes
    national_abstention_null_invalid(df_by_dpt)

    # Calculate national candidate scores
    df_sorted_scores = calculate_national_candidate_scores(df_by_dpt_full_name)
    for row in df_sorted_scores.itertuples(index=False):
        print(f"{row.candidate}: {row.score}%")

    # Plot national candidate scores
    plot_individual_scores(df_sorted_scores, "candidate", "score",
                           "National Candidates Ratings", "Candidate",
                           "National Score in %", "thistle", highlight_top_n=2)


if __name__ == "__main__":
    main()