import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from data_processing import load_dataset, candidate_full_names_column, add_department_type_column, candidate_political_side_column
from src.constants import political_side_colours
from src.data_processing import create_df_by_candidate
from visualisations import plot_scores_pol_sides
from statistical_analysis import scores_by_political_side
from constants import base_cols, candidates_political_sides
import json
import requests
import plotly.express as px

# Loading dataset into a dataframe
file_name = "elections_results_by_department.xlsx"
df_by_dpt = load_dataset(file_name)

# Creating new column with candidate full names
df_by_dpt_full_name = candidate_full_names_column(df_by_dpt)
df_by_dpt_full_name = candidate_political_side_column(df_by_dpt_full_name, candidates_political_sides)

df_by_candidate = create_df_by_candidate(df_by_dpt, base_cols)

results_pol_side = scores_by_political_side(df_by_candidate)

df_by_dpt_type = add_department_type_column(df_by_dpt)



import seaborn as sns
import matplotlib.pyplot as plt



#### TRY CHatGPT code
# Dropping row with votes from French citizens living abroad as it is not a department
#df_light = df_by_dpt.drop(106, axis="index")
#df_by_dpt_type.to_excel("test_file.xlsx")


