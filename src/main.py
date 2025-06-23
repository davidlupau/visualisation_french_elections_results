from data_processing import load_dataset, candidate_full_names_column
from constants import candidates_full_names
from src.statistical_analysis import explore_dataset_quality

def main():
    # Loading dataset into a dataframe
    file_name = "elections_results_by_department.xlsx"
    df_by_dpt = load_dataset(file_name)

    # Performing basic exploration
    explore_dataset_quality(df_by_dpt)

    # Creating new column with candidate full names
    candidate_full_names_column(df_by_dpt)


if __name__ == "__main__":
    main()