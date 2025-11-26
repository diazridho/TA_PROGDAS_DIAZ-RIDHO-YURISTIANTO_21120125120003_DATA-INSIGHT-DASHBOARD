from matplotlib.figure import Figure
import pandas as pd
from core.chart_abstract import abstract_double, abstract_single

# Class untuk visualisasi data tunggal (univariate)
class ChartGeneratorSingle(abstract_single):

    #chart untuk visualisasi data kategori
    @staticmethod
    def bar_chart(df: pd.DataFrame, column: str) -> Figure:
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        counts = df[column].value_counts()
        counts.plot(kind='bar', ax=ax)
        ax.set_title(f'Bar Chart of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Counts')
        return fig
    
    @staticmethod
    def pie_chart(df: pd.DataFrame, column: str) -> Figure:
        fig = Figure(figsize=(6, 6))
        ax = fig.add_subplot(111)
        counts = df[column].value_counts()
        counts.plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_title(f'Pie Chart of {column}')
        ax.set_ylabel('')
        return fig
    
    #chart untuk visualisasi data numerik   
    @staticmethod
    def histogram(df: pd.DataFrame, column: str) -> Figure:
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        df[column].plot(kind='hist', bins=30, ax=ax)
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        return fig
    
    @staticmethod
    def box_plot(df: pd.DataFrame, column: str) -> Figure:
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        df.boxplot(column=column, ax=ax)
        ax.set_title(f'Box Plot of {column}')
        return fig
    
    # Jenis chart berdasarkan jumlah variabel, diwajibkan class abstract
    @staticmethod
    def chart_type(df: pd.DataFrame, column: str) -> str:
        return "univariat"
    

# Class untuk visualisasi data ganda (bivariate)
class ChartGeneratorDouble(abstract_double):

    @staticmethod
    def line_chart(df: pd.DataFrame, x_column: str, y_column: str) -> Figure:
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        df.plot(kind='line', x=x_column, y=y_column, ax=ax)
        ax.set_title(f'Line Chart of {y_column} vs {x_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        return fig
    
    @staticmethod
    def scatter_plot(df: pd.DataFrame, x_column: str, y_column: str) -> Figure:
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        df.plot(kind='scatter', x=x_column, y=y_column, ax=ax)
        ax.set_title(f'Scatter Plot of {y_column} vs {x_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        return fig
    
    @staticmethod
    def chart_type(df: pd.DataFrame, column: str) -> str:
        return "bivariate"
    
