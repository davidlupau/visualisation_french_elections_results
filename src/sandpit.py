import pandas as pd
from data_processing import load_dataset, candidate_full_names_column, create_df_by_candidate, candidate_political_side_column
from src.data_processing import create_df_by_candidate
from visualisations import plot_bar_chart_cand_scores
from visualisations import plot_individual_scores
from statistical_analysis import scores_by_political_side
from constants import base_cols, candidates_political_sides

# Loading dataset into a dataframe
file_name = "elections_results_by_department.xlsx"
df_by_dpt = load_dataset(file_name)

# Creating new column with candidate full names
df_by_dpt_full_name = candidate_full_names_column(df_by_dpt)
df_by_dpt_full_name = candidate_political_side_column(df_by_dpt_full_name, candidates_political_sides)

df_by_candidate = create_df_by_candidate(df_by_dpt, base_cols)
#df_by_candidate.to_excel("test_file.xlsx")

results_pol_side = scores_by_political_side(df_by_candidate)

