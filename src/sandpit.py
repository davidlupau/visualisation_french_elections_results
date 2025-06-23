from data_processing import load_dataset, candidate_full_names_column
from constants import candidates_full_names
from src.statistical_analysis import explore_dataset_quality

# Loading dataset into a dataframe
file_name = "elections_results_by_department.xlsx"
df_by_dpt = load_dataset(file_name)


# Calculating candidate scores on national level i.e. total number of votes / total number of valid votes
print("Calculating candidate scores on national level (sorted by score)\n")

candidate_scores = []

for i in range(1, 13):
    vote_col = f"candidate_{i}_votes"
    full_name_key = f"candidate_{i}_full_name"

    full_name = candidates_full_names.get(full_name_key, f"Candidate {i}")

    total_votes = df_by_dpt[vote_col].sum()
    total_voters = df_by_dpt["valid_votes"].sum()

    score = round((total_votes / total_voters) * 100, 2)

    candidate_scores.append((full_name, score))

# Sort by descending score
candidate_scores_sorted = sorted(candidate_scores, key=lambda x: x[1], reverse=True)

# Print results
for name, score in candidate_scores_sorted:
    print(f"{name}: {score}%")

#df_by_dpt.to_excel("test_file.xlsx")


# Mapping candidate surname to political side


#df["political_side"] = df["candidate_surname"].map(candidates_political_sides)


# Calculate the national abstention, blank and null votes
print("\nCalculate the national abstention, blank and null votes:")

for col, label in column_labels.items():
    mean = df_by_dpt[col].mean().round(2)
    print(f"{label}: {mean}%")