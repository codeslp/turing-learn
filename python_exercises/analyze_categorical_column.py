
def analyze_categorical_column(
    dataframe: pd.DataFrame, column_name: str
) -> Tuple[Dict[str, Any], pd.DataFrame, pd.DataFrame]:
    """
    Analyze a categorical column of a given DataFrame.
    """

    analysis_results = {}

    if column_name not in dataframe.columns:
        return f"The column '{column_name}' does not exist in the DataFrame."

    col_data = dataframe[column_name]
    
    analysis_results["missing_values"] = col_data.isnull().sum()
    analysis_results["unique_values"] = col_data.nunique()
    analysis_results["total_values"] = col_data.count()
    analysis_results["duplicated_values"] = col_data.duplicated().sum()
    analysis_results["values_with_whitespace"] = col_data.str.strip().ne(col_data).sum()
    analysis_results["values_with_unusual_chars"] = (
        col_data
        .apply(lambda x: any(ord(char) < 32 or ord(char) > 126 for char in str(x)))
        .sum()
    )

    value_lengths = col_data.dropna().str.len()
    analysis_results["shortest_value_length"] = value_lengths.min()
    analysis_results["longest_value_length"] = value_lengths.max()
    analysis_results["average_value_length"] = value_lengths.mean()

    shortest_value = dataframe[col_data == value_lengths.min()]
    longest_value = dataframe[col_data == value_lengths.max()]

    return analysis_results, shortest_value, longest_value