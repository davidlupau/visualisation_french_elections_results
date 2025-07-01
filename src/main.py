from data_processing import load_dataset, candidate_full_names_column, create_df_by_candidate, candidate_political_side_column, add_department_type_column, categorisation_dpt_size
from statistical_analysis import explore_dataset_quality, national_abstention_null_invalid, calculate_national_candidate_scores, scores_by_political_side
from constants import base_cols, candidates_political_sides, political_side_colours
from visualisations import plot_individual_scores, plot_scores_pol_sides, abst_null_inva_pie_chart, scatterplot_by_dpt_type, violin_plot_by_dpt_size, choropleth_abstention

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
    df_by_dpt_full_name = candidate_political_side_column(df_by_dpt_full_name, candidates_political_sides)

    # Create a dataframe with results by candidate
    df_by_candidate = create_df_by_candidate(df_by_dpt, base_cols)

    print("\n=== NATIONAL ANALYSIS ===")
    # Calculate national abstention, blank and invalid votes
    national_abstention_null_invalid(df_by_dpt)
    abst_null_inva_pie_chart(df_by_dpt)

    # Calculate national candidate scores
    df_sorted_scores = calculate_national_candidate_scores(df_by_dpt_full_name)
    for row in df_sorted_scores.itertuples(index=False):
        print(f"{row.candidate}: {row.score}%")

    # Plot national candidate scores
    plot_individual_scores(df_sorted_scores, "candidate", "score",
                           "National Candidates Scores", "Candidate",
                           "National Score in %", "thistle", highlight_top_n=2)

    # Results by political side
    results_pol_side = scores_by_political_side(df_by_candidate)
    # Plotting the results
    plot_scores_pol_sides(results_pol_side, political_side_colours)

    print("\n=== ANALYSIS BY DEPARTMENT ===")
    # Add a column department type (Metropolitan, Corsica, Oversea, French living abroad)
    df_by_dpt_type = add_department_type_column(df_by_dpt)
    # Create scatter plot with abstention rate and department type
    scatterplot_by_dpt_type(df_by_dpt_type)

    # Add a new column to categorize departments by registered voter population
    df_cat_dpt = categorisation_dpt_size(df_by_dpt)

    # Create violin plot to visualise abstention rate by department size
    violin_plot_by_dpt_size(df_cat_dpt)

    # Remove rows related to French citizen abroad and oversea departments
    df_metropolitan_dpt = df_by_dpt_full_name.iloc[:96]

    # Create a map of France to plot abstention by department
    choropleth_abstention(df_metropolitan_dpt)

if __name__ == "__main__":
    main()