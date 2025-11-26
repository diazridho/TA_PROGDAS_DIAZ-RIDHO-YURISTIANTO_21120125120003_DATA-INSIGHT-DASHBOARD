import pandas as pd
from pandas.api import types as cek_data

class DataAnalyzer:

    # Membuat ringkasan statistik dari dataframe dengan mengganti index asli describe
    @staticmethod
    def detect_column_type(df, column):
        if cek_data.is_numeric_dtype(df[column]):
            return "numeric"
        elif cek_data.is_string_dtype(df[column]) or cek_data.is_object_dtype(df[column]):
            return "categorical"
        elif cek_data.is_datetime64_any_dtype(df[column]):
            return "datetime"
        else:
            return "tidak diketahui tipe datanya bang"
        
    @staticmethod
    def summary(df):
        desc = df.describe(include='all')
        mapping_index = {
            'count': 'Jumlah Data',
            'mean': 'Rata-rata',
            'std': 'Standar Deviasi',
            'min': 'Nilai Minimum',
            '25%': 'Kuartil 25%',
            '50%': 'Median',
            '75%': 'Kuartil 75%',
            'max': 'Nilai Maksimum',
            'unique': 'Jumlah Nilai Unik',
            'top': 'Nilai Teratas',
            'freq': 'Frekuensi Nilai Teratas'
        }
        return desc.rename(index=mapping_index)
    
    # Baris lengkap dan hilang
    @staticmethod
    def show_complete_rows(df):
        return df.dropna(how="any")
    
    @staticmethod
    def sum_complete_rows(df):
        return len(DataAnalyzer.show_complete_rows(df))
    
    @staticmethod
    def show_missing_rows(df):
        tmp = df.isna().any(axis=1)
        if tmp.any():
            return df[tmp]
        else:
            return None
    
    @staticmethod
    def sum_missing_rows(df):
        return len(DataAnalyzer.show_missing_rows(df))

    # Nilai unik di setiap kolom
    @staticmethod
    def unique_values(df):
        return df.nunique().sort_values(ascending=False)
    
    # Tipe data setiap kolom
    @staticmethod
    def data_types(df):
        return df.dtypes
    
    # Penggunaan memori setiap kolom
    @staticmethod
    def memory_usage(df):
        return df.memory_usage(deep=True)


    
    




    

    