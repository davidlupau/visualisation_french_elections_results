import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import json
import requests

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

def plot_scores_pol_sides(df, color_map=None):
    """
    Plots a bar chart showing scores for pol sides.
    Parameter:
        df (pd.DataFrame): The DataFrame containing the data.
        color_map (dict, optional): Color map for bars mapping political side and official colors. Default is None.
    """
    plt.figure(figsize=(10, 5))

    if color_map is None:
        bars = plt.bar(df['political_side'], df['percentage'])
    else:
        # Map colors to political sides
        colors = [color_map.get(side, '#808080') for side in df['political_side']]
        bars = plt.bar(df['political_side'], df['percentage'], color=colors)

    # add x- and y-axis labels
    plt.xlabel('Political Side')
    plt.ylabel('Score in %')
    plt.title('Scores by Political Side')

    # Fix x-axis labels
    plt.xticks(rotation=45, ha='right')

    # Add value labels on bars
    for bar, score in zip(bars, df['percentage']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                 f'{score:.1f}%', ha='center')

    # show figure
    plt.tight_layout()
    plt.show()


def abst_null_inva_pie_chart(df, custom_labels=None, explode_small_slices=True, color_scheme='neutral'):
    """
    Creates a pie chart showing voting statistics with politically neutral colors.
    Parameters:
        df: DataFrame with voting data
        custom_labels (list, optional): Custom labels for the pie slices
        explode_small_slices (bool): Whether to separate small slices for better visibility
        color_scheme (str): Color scheme - 'grey_highlight', 'brown_highlight', or 'neutral'
    """
    # Calculate totals
    total = [
        df['total_voters'].sum(),
        df['abstention'].sum(),
        df['blank_votes'].sum(),
        df['invalid_votes'].sum()
    ]

    # Define labels
    if custom_labels:
        labels = custom_labels
    else:
        labels = ['Total Voters', 'Abstention', 'Blank Votes', 'Invalid Votes']

    # Define color schemes
    color_schemes = {
        'grey_highlight': ['#E0E0E0', '#4A4A4A', '#B0B0B0', '#D0D0D0'],
        # Light grey, dark grey (abstention), medium greys
        'brown_highlight': ['#F5E6D3', '#8B4513', '#D2B48C', '#DEB887'],  # Light beige, dark brown (abstention), tans
        'neutral': ['#F0F0F0', '#606060', '#A0A0A0', '#C0C0C0'],  # Pure neutrals
        'blue_grey': ['#E6F3FF', '#2C5F7C', '#87CEEB', '#B0C4DE']
        # Very light blue, dark blue-grey (abstention), light blues
    }

    colors = color_schemes.get(color_scheme, color_schemes['neutral'])

    # Calculate percentages to determine which slices to explode
    total_sum = sum(total)
    percentages = [val / total_sum * 100 for val in total]

    # Explode small slices (less than 5%)
    if explode_small_slices:
        explode = [0.1 if pct < 5 else 0 for pct in percentages]
    else:
        explode = None

    # Create pie chart
    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(total,
                                       labels=labels,
                                       autopct='%1.1f%%',
                                       colors=colors,
                                       explode=explode,
                                       pctdistance=0.85,
                                       labeldistance=1.1)

    for i, autotext in enumerate(autotexts):
        # Check if this is abstention (index 1) - dark background needs white text
        if i == 1:  # Abstention slice
            autotext.set_color('white')
        else:  # All other slices have light backgrounds - use black text
            autotext.set_color('black')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    plt.title('French Election Participation Analysis', fontsize=14, fontweight='bold', pad=20)
    plt.axis('equal')

    plt.tight_layout()
    plt.show()

def scatterplot_by_dpt_type(df):
    """
    Creates a scatter plot showing voting statistics with politically neutral colors.
    parameter:
     df
    """
    print("Creating scatter plot with abstention and number of registered voters in each department..\n")
    # Creating Scatter plot showing Abstention Vs Number of registered voters by department
    plt.figure(figsize=(10, 5))

    colors = ['#333300', '#cccc00', '#a64dff', '#b35900']
    custom_palette = sns.set_palette(sns.color_palette(colors))

    # scatter plot with one variable
    ax = sns.scatterplot(data=df, x="total_registered_voters",
                         y="abstention_pct_reg",
                         hue="dpt_type",
                         color=custom_palette)

    plt.title("Abstention Rate Distribution Across French Departments")
    plt.xlabel("Population of registered voters in millions")
    plt.ylabel("Abstention Rate in %")
    sns.move_legend(ax, "center left", title="Department type", bbox_to_anchor=(1, 0.5))
    plt.tight_layout()

    plt.show()

def violin_plot_by_dpt_size(df):
    """
    Creates a violin plot showing voting statistics with politically neutral colors.
    Parameter: df with column splitting departments into 4 categories according to their number of registered voters.
    """
    print("Creating violin plot to visualise abstention rate by department size...")
    sns.violinplot(
        x="population_group",
        y="abstention_pct_reg",
        hue="population_group",
        data=df,
        inner="box",
        palette="PuOr"
    )

    plt.title("Abstention Rate by Department Size")
    plt.xlabel("Department Size (Population Quartiles)")
    plt.ylabel("Abstention Rate (%)")
    plt.show()

def choropleth_abstention(df):
    """
    Create a choropleth plot showing abstention rate by department size for metropolitan France.
    Parameter:
        df with metropolitan department and abstention rates.
    """
    print("Creating choropleth abstention...")
    # Load GeoJSON file from GitHub
    url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson"
    geojson = requests.get(url).json()

    fig = px.choropleth(
        df,
        geojson=geojson,
        locations='department_code',
        featureidkey='properties.code',
        color='abstention_pct_reg',
        color_continuous_scale='purples',
        labels={'abstention_pct_reg': 'Abstention (%)', 'department_code': 'Department Code'},
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        title_text='Abstention Rate per Department (France, 2022)',
        margin={"r": 10, "t": 60, "l": 10, "b": 10},
        height=700,
        title_x=0.5,
        title_y=0.95,
        title_font=dict(size=20),
        coloraxis_colorbar=dict(
            title="Abstention (%)",
            thickness=15,
            len=0.75,
            y=0.5,
            yanchor='middle'
        )
    )

    fig.show()


def choropleth_political_sides(df, political_side_colours):
    """
    Create a choropleth plot showing winning political side by department for metropolitan France.

    Parameters:
        df: DataFrame with department_code, department_name, and winning_political_side columns
        political_side_colours: Dictionary mapping political sides to hex colors
    """
    print("\n Creating political sides choropleth...")

    # Load GeoJSON file from GitHub
    url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson"
    geojson = requests.get(url).json()

    fig = px.choropleth(
        df,
        geojson=geojson,
        locations='department_code',
        featureidkey='properties.code',
        color='winning_political_side',
        color_discrete_map=political_side_colours,
        labels={
            'winning_political_side': 'Political Side',
            'department_code': 'Department Code'
        },
        hover_data=['department_name']
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_traces(
        marker_line_color='white',
        marker_line_width=0.5
    )

    fig.update_layout(
        title_text='Winning Political Side per Department (France, 2022)',
        margin={"r": 10, "t": 60, "l": 10, "b": 10},
        height=700,
        title_x=0.5,
        title_y=0.95,
        title_font=dict(size=20),
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
            title="Political Side"
        )
    )

    fig.show()