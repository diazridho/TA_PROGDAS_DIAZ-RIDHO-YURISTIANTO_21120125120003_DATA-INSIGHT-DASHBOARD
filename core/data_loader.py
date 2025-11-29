import pandas as pd
import os

class DataLoader:
    SUPPORTED = ('.csv', '.xlsx', '.json', '.parquet', '.txt')

    @staticmethod
    def DataLoad(path):
        path = os.path.abspath(path)
        extension = os.path.splitext(path)[1].lower()
        if extension not in DataLoader.SUPPORTED:
            raise ValueError(f"Format {extension} tidak didukung.")
        if extension == '.csv':
            return pd.read_csv(path, na_values=["", " "], keep_default_na=True)    
        elif extension == '.xlsx':
            return pd.read_excel(path)
        elif extension == '.json':
            return pd.read_json(path)
        elif extension == '.parquet':
            return pd.read_parquet(path)
        elif extension == '.txt':
            return pd.read_csv(path, delimiter='\t')
        