import matplotlib.pyplot as plt

def plot_bar_chart_cand_scores(df, columns, title, x_label, y_label, color=None, label_base="Label"):
    """
    Plots a bar chart of mean ratings for a list of columns.
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to calculate the scores.
        title (str): Title of the chart.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        color (str or list, optional): Colour for the bars. Default is None (Matplotlib default colors).
        label_base (str): Base label for x-axis ticks (e.g. 'Module', 'Candidate').
    """
    print("Creating bar chart...")
    total_cand_votes = df[columns[0]].sum()
    means = [round(df[col].mean(), 2) for col in columns[:, 1:]]
    labels = [f"{label_base} {i + 1}" for i in range(len(columns))]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, means, color=color)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ylim(0, 100)

    for i, v in enumerate(means):
        plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()
    print("Done!")


def plot_individual_scores(df, candidate_col, score_col, title, x_label, y_label, color=None, highlight_top_n=0):
    """
    Plots a bar chart showing individual scores for each candidate.

    Parameters:
        df (pd.DataFrame): DataFrame with candidate data
        candidate_col (str): Column name containing candidate names
        score_col (str): Column name containing scores
        title (str): Chart title
        x_label (str): X-axis label
        y_label (str): Y-axis label
        color (str, optional): Bar color
        highlight_top_n (int, optional): Highlight top n candidates
    """
    plt.figure(figsize=(12, 6))

    # Create color list - highlight top candidates
    colors = []
    for i in range(len(df)):
        if i < highlight_top_n:
            colors.append('mediumpurple')
        else:
            colors.append(color if color else 'skyblue')

    # Create bars using candidate names and their scores
    bars = plt.bar(df[candidate_col], df[score_col], color=colors)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45, ha='right')  # Rotate names for readability

    # Add value labels on bars
    for bar, score in zip(bars, df[score_col]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                 f'{score:.2f}%', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()