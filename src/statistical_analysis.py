from data_processing import save_analysis_to_excel
def explore_dataset_quality(df):
    # Get a summary of the dataset
    print(df.info())

    # Get descriptive statistics for numerical columns in a csv file
    print("Retrieving basic information from the dataset\n ")
    describe_dataset = df.describe(include='all')
    # Save to an Excel file
    save_analysis_to_excel(describe_dataset, 'dataset_quality.xlsx')

    # Calculate missing values in each column
    print("Calculating the percentage of null values for in each column.\n")
    missing_percentage = df.isnull().mean() * 100

    # Save to an Excel file
    save_analysis_to_excel(missing_percentage, 'missing_percentage.xlsx')