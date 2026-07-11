import pandas as pd
import os


def load_csv(filename):
    """
    Load a CSV file from the data folder as a pandas DataFrame.
    
    Args:
        filename (str): Name of the CSV file to load
        
    Returns:
        pd.DataFrame: DataFrame containing the CSV data
    """
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data/raw')
    filepath = os.path.join(data_dir, filename)
    df = pd.read_csv(filepath)
    return df


def load_all_csv():
    """
    Load all CSV files from the data/raw folder as a dictionary of pandas DataFrames.
    
    Returns:
        dict: Mapping of filename to DataFrame for each CSV file in data/raw
    """
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data/raw')
    csv_files = [f for f in os.listdir(data_dir) if f.lower().endswith('.csv')]
    data_frames = {}
    for filename in csv_files:
        filepath = os.path.join(data_dir, filename)
        data_frames[filename] = pd.read_csv(filepath)
    return data_frames
