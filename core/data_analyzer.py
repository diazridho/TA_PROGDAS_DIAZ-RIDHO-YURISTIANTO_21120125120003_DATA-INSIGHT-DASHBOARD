import pandas as pd

class DataAnalyzer:

    @staticmethod
    def complete_rows(df):
        return df.dropna(how="any")
    
    @staticmethod
    def sum_complete_rows(df):
        return len(DataAnalyzer.complete_rows(df))
    
    @staticmethod
    def missing_rows(df):
        tmp = df.isna().any(axis=1)
        return df[tmp]
    
    @staticmethod
    def sum_missing_rows(df):
        return len(DataAnalyzer.missing_rows(df))
    