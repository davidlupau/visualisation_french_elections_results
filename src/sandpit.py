from functions import load_dataset

# Loading dataset into a dataframe
file_name = "elections_results_by_department.xlsx"
df = load_dataset(file_name)

# Adding columns with candidates names and political side
# Mapping candidate surname to candidate full name
candidates_full_names = {
    "candidate_1_surname": "Nathalie Arthaud",
    "candidate_2_surname": "Fabien Roussel",
    "candidate_3_surname": "Emmanuel Macron",
    "candidate_4_surname": "Jean Lassalle",
    "candidate_5_surname": "Marine Le Pen",
    "candidate_6_surname": "Éric Zemmour",
    "candidate_7_surname": "Jean-Luc Mélenchon",
    "candidate_8_surname": "Anne Hidalgo",
    "candidate_9_surname": "Yannick Jadot",
    "candidate_10_surname": "Valérie Pécresse",
    "candidate_11_surname": "Philippe Poutou",
    "candidate_12_surname": "Nicolas Dupont-Aignan"
}

# Mapping candidate surname to political side
candidates_political_sides = {
    "candidate_1_surname": "Far-left",
    "candidate_2_surname": "Far-left",
    "candidate_3_surname": "Center",
    "candidate_4_surname": "Other",
    "candidate_5_surname": "Far-right",
    "candidate_6_surname": "Far-right",
    "candidate_7_surname": "Far-left",
    "candidate_8_surname": "Left",
    "candidate_9_surname": "Left",
    "candidate_10_surname": "Right",
    "candidate_11_surname": "Far-left",
    "candidate_12_surname": "Right"
}

df["political_side"] = df["candidate_surname"].map(candidates_political_sides)


# Calculate the national abstention, blank and null votes
column_to_mean: ["abstention_pct_reg",
                "blank_votes_pct_voters",
                "invalid_votes_pct_voterst"
]

abstention = df["abstention_pct_reg"].mean().round(2)
print(f"Abstention PCT: {abstention}%")