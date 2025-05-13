import pandas as pd

def descriptive_analysis(df, columns, group_by=None):
    """
    Generates frequency and percentage tables for specified categorical columns,
    optionally grouped by a variable (e.g., province or gender).

    Parameters:
    - df: pandas DataFrame
    - columns: dictionary where keys are labels and values are column names
    - group_by: optional string column name to group results (e.g., 'Province' or 'Gender')

    Returns:
    - results: dictionary with question labels as keys and DataFrames as values
              Each DataFrame contains frequency and percentage columns.
    """
    results = {}

    for label, col in columns.items():
        if col not in df.columns:
            results[label] = f"Column '{col}' not found in DataFrame."
            continue

        if group_by and group_by in df.columns:
            # Grouped analysis
            grouped = df.groupby(group_by)[col].value_counts(dropna=False).unstack(fill_value=0)

            # Calculate percentage within each group
            percent = grouped.div(grouped.sum(axis=1), axis=0).multiply(100).round(2)

            # Combine counts and percentage for easier reading
            combined = grouped.astype(int).astype(str) + " (" + percent.round(1).astype(str) + "%)"
            results[label] = combined

        else:
            # Overall analysis
            freq = df[col].value_counts(dropna=False).reset_index()
            freq.columns = [label, 'Frequency']
            freq['Percentage'] = (freq['Frequency'] / freq['Frequency'].sum() * 100).round(2)
            results[label] = freq

    return results

def range_frequency_analysis(df, numeric_col, bins, labels):
    """
    Analyzes a numeric column by dividing it into specified bins and calculating frequency and percentage.

    Parameters:
    - df: pandas DataFrame
    - numeric_col: string, name of the numeric column to analyze
    - bins: list of numeric bin edges (e.g., [400, 600, 800, 1000, 1200])
    - labels: list of labels corresponding to the bin intervals

    Returns:
    - DataFrame with 'Range', 'Frequency', and 'Percentage'
    """
    if numeric_col not in df.columns:
        raise ValueError(f"Column '{numeric_col}' not found in the DataFrame.")

    # Create a categorical column based on bins
    df['Range_Binned'] = pd.cut(df[numeric_col], bins=bins, labels=labels, right=False)

    # Calculate frequency and percentage
    freq_df = df['Range_Binned'].value_counts(sort=False).reset_index()
    freq_df.columns = ['Range', 'Frequency']
    freq_df['Percentage'] = (freq_df['Frequency'] / freq_df['Frequency'].sum() * 100).round(2)

    return freq_df

def multiple_response_analysis(df, columns_dict, question_label, group_by=None):
    """
    Analyzes a multiple-response question with each option in a separate column,
    with optional group-wise frequency and percentage output.

    Parameters:
    - df: pandas DataFrame
    - columns_dict: dictionary where keys are option labels and values are column names
    - question_label: string, main question text to prefix in output
    - group_by: optional column name to group by (e.g., 'Province', 'Gender')

    Returns:
    - DataFrame or dictionary of DataFrames (if grouped)
      showing frequency and percentage for each option.
    """
    # Create a binary DataFrame (1 = selected, 0 = not selected)
    binary_df = pd.DataFrame()
    for option_text, col in columns_dict.items():
        if col in df.columns:
            binary_df[option_text] = df[col].notnull().astype(int)
        else:
            binary_df[option_text] = 0  # if column missing, fill with 0

    binary_df[group_by] = df[group_by] if group_by and group_by in df.columns else None

    if group_by and group_by in df.columns:
        results = []

        # Grouped frequency and percentage
        grouped = binary_df.groupby(group_by)
        counts = grouped.sum()
        totals = grouped.size().rename("Total")

        percentages = counts.div(totals, axis=0).multiply(100).round(2)

        # Combine frequency and percentage in a readable format
        for col in counts.columns:
            counts[col] = counts[col].astype(int).astype(str) + " (" + percentages[col].astype(str) + "%)"

        results_df = counts.reset_index()
        return results_df

    else:
        # Overall frequency and percentage
        total = len(df)
        summary = []

        for option in columns_dict.keys():
            freq = binary_df[option].sum()
            percent = round((freq / total) * 100, 2)
            summary.append({
                'Reason': f"{question_label} – {option}",
                'Frequency': freq,
                'Percentage': percent
            })

        return pd.DataFrame(summary)
