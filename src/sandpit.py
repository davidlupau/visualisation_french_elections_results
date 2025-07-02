import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from data_processing import load_dataset, candidate_full_names_column, determine_winning_political_side, candidate_political_side_column
from src.constants import political_side_colours
from src.data_processing import create_df_by_candidate
from visualisations import choropleth_political_sides
from statistical_analysis import scores_by_political_side
from constants import base_cols, candidates_political_sides, political_side_colours
import json
import requests
import plotly.express as px
# Set display option to show all columns
pd.set_option('display.max_columns', None)

# Loading dataset into a dataframe
file_name = "elections_results_by_department.xlsx"
df_by_dpt = load_dataset(file_name)

# Creating new column with candidate full names
df_by_dpt_full_name = candidate_full_names_column(df_by_dpt)
df_by_dpt_full_name = candidate_political_side_column(df_by_dpt_full_name, candidates_political_sides)

df_by_candidate = create_df_by_candidate(df_by_dpt, base_cols)

df_metropolitan_dpt = df_by_dpt_full_name.iloc[:96]
df_political_side = determine_winning_political_side(df_metropolitan_dpt)

plt.figure(figsize=(10, 5))
sns.histplot(data=df_by_dpt['abstention_pct_reg'], bins=7)
plt.show()
#### Plot map with color wining candidate + strip chart to compare wining side on x (3 lines) and abstention on y
# Dropping row with votes from French citizens living abroad as it is not a department
#df_light = df_by_dpt.drop(106, axis="index")
#df_by_dpt_type.to_excel("test_file.xlsx")


