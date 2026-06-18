import pandas as pd

def load_excel(file_path, header_row=1):
    """
    Load Excel file and return DataFrame
    """

    df = pd.read_excel(file_path, header=header_row)

    return df