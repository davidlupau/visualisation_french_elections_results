# === CANDIDATE MAPPINGS ===

# Map candidate IDs from dataset to full names
candidates_full_names = {
    "candidate_1_full_name": "Nathalie Arthaud",
    "candidate_2_full_name": "Fabien Roussel",
    "candidate_3_full_name": "Emmanuel Macron",
    "candidate_4_full_name": "Jean Lassalle",
    "candidate_5_full_name": "Marine Le Pen",
    "candidate_6_full_name": "Éric Zemmour",
    "candidate_7_full_name": "Jean-Luc Mélenchon",
    "candidate_8_full_name": "Anne Hidalgo",
    "candidate_9_full_name": "Yannick Jadot",
    "candidate_10_full_name": "Valérie Pécresse",
    "candidate_11_full_name": "Philippe Poutou",
    "candidate_12_full_name": "Nicolas Dupont-Aignan"
}

# Map candidate surnames to political side
candidates_political_sides = {
    "ARTHAUD": "Far-left",
    "ROUSSEL": "Far-left",
    "MACRON": "Center",
    "LASSALLE": "Other",
    "LE PEN": "Far-right",
    "ZEMMOUR": "Far-right",
    "MÉLENCHON": "Far-left",
    "HIDALGO": "Left",
    "JADOT": "Left",
    "PÉCRESSE": "Right",
    "POUTOU": "Far-left",
    "DUPONT-AIGNAN": "Right"
}

# === ANALYSIS CONFIGURATION ===
# Define the columns to keep to build df by candidate
base_cols = ['department_code',
             'department_name',
             'abstention_pct_reg',
             'total_voters',
             'blank_votes',
             'invalid_votes']

# Columns for candidates scores calculation
column_candidate_scores = ["total_voters",
                           "candidate_1_votes",
                           "candidate_2_votes",
                           "candidate_3_votes",
                           "candidate_4_votes",
                           "candidate_5_votes",
                           "candidate_6_votes",
                           "candidate_7_votes",
                           "candidate_8_votes",
                           "candidate_9_votes",
                           "candidate_10_votes",
                           "candidate_11_votes",
                           "candidate_12_votes"
]

# Colour palette matching political side for visualisation
political_side_colours = {
    "Far-right": "#000099",
    "Center": "#ff9900",
    "Far-left": "#DC143C",
    "Right": "#4169E1",
    "Left": "#FF69B4",
    "Other": "#808080"
}

