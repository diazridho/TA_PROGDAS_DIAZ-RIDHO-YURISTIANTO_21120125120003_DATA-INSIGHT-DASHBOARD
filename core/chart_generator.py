from matplotlib.figure import Figure
import pandas as pd
import numpy as np
from core.chart_abstract import abstract_single, abstract_double

class ChartGeneratorSingle(abstract_single):
    """Class untuk visualisasi data tunggal (univariate)"""
    
    # Data kategori
    def bar_chart(self, data, column):
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        
        counts = data[column].value_counts()
        counts.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title(f'Bar Chart of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Counts')
        ax.tick_params(axis='x', rotation=45)
        
        return fig

    def pie_chart(self, data, column):
        fig = Figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        
        counts = data[column].value_counts()
        counts.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Pie Chart of {column}')
        ax.set_ylabel('')
        
        return fig
    
    # Data numerik
    def histogram(self, data, column):
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        
        data[column].plot(kind='hist', bins=30, ax=ax, color='lightgreen', alpha=0.7)
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        
        return fig

    def heatmap(self, data, column):
        """Heatmap correlation untuk semua numerical columns"""
        fig = Figure(figsize=(10, 8))
        ax = fig.add_subplot(111)
        
        # Ambil hanya numerical columns
        numerical_data = data.select_dtypes(include=[np.number])
        
        if len(numerical_data.columns) < 2:
            # Jika kurang dari 2 numerical columns, buat heatmap sederhana
            ax.text(0.5, 0.5, 'Need at least 2 numerical columns for heatmap', 
                   ha='center', va='center', transform=ax.transAxes, fontsize=12)
            ax.set_title('Heatmap - Insufficient Numerical Data')
        else:
            # Hitung correlation matrix
            corr_matrix = numerical_data.corr()
            
            # Buat heatmap
            im = ax.imshow(corr_matrix.values, cmap='coolwarm', vmin=-1, vmax=1)
            
            # Set labels
            ax.set_xticks(range(len(corr_matrix.columns)))
            ax.set_yticks(range(len(corr_matrix.columns)))
            ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
            ax.set_yticklabels(corr_matrix.columns)
            
            # Add values di cells
            for i in range(len(corr_matrix.columns)):
                for j in range(len(corr_matrix.columns)):
                    ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}', 
                           ha='center', va='center', 
                           color='white' if abs(corr_matrix.iloc[i, j]) > 0.5 else 'black',
                           fontsize=10)
            
            ax.set_title('Correlation Heatmap')
            fig.colorbar(im, ax=ax)
        
        return fig

    def box_plot(self, data, column):
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        
        data.boxplot(column=column, ax=ax)
        ax.set_title(f'Box Plot of {column}')
        ax.set_ylabel(column)
        
        return fig
    
    # Metadata chart
    def chart_type(self, data, column):
        return "univariat"


class ChartGeneratorDouble(abstract_double):
    """Class untuk visualisasi data ganda (bivariate)"""
    
    def histogram(self, data, x_column, y_column):
        """Histogram grouped by categorical column"""
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Group data by x_column dan plot histogram untuk y_column
        groups = data.groupby(x_column)[y_column]
        
        # Plot histogram untuk setiap group
        for i, (name, group) in enumerate(groups):
            group.hist(ax=ax, alpha=0.7, label=str(name), bins=20)
        
        ax.set_title(f'Histogram of {y_column} grouped by {x_column}')
        ax.set_xlabel(y_column)
        ax.set_ylabel('Frequency')
        ax.legend(title=x_column)
        
        return fig

    def bar_chart(self, data, x_column, y_column):
        """Bar chart dengan 2 variabel (grouped bar chart)"""
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Group by x_column dan aggregate y_column
        if data[y_column].dtype in ['int64', 'float64']:
            # Jika y_column numerical, gunakan mean
            grouped = data.groupby(x_column)[y_column].mean()
            y_label = f'Average {y_column}'
        else:
            # Jika y_column categorical, gunakan count
            grouped = data.groupby(x_column)[y_column].count()
            y_label = f'Count of {y_column}'
        
        grouped.plot(kind='bar', ax=ax, color='steelblue', alpha=0.7)
        ax.set_title(f'Bar Chart: {y_column} by {x_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_label)
        ax.tick_params(axis='x', rotation=45)
        
        return fig

    def scatter_plot(self, data, x_column, y_column):
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        
        data.plot(kind='scatter', x=x_column, y=y_column, ax=ax, alpha=0.6)
        ax.set_title(f'Scatter Plot: {y_column} vs {x_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        
        # Add trend line jika numerical
        if data[x_column].dtype in ['int64', 'float64'] and data[y_column].dtype in ['int64', 'float64']:
            z = np.polyfit(data[x_column], data[y_column], 1)
            p = np.poly1d(z)
            ax.plot(data[x_column], p(data[x_column]), "r--", alpha=0.8)
        
        return fig

    def chart_type(self, data, column):
        return "bivariate"