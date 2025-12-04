from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QTableWidget, QTableWidgetItem,
                            QHeaderView, QGridLayout)
from PyQt6.QtCore import Qt
import pandas as pd
from core.data_analyzer import DataAnalyzer
from ui.dialogs.summary_dialog import SummaryDialog
from ui.dialogs.complete_rows_dialog import CompleteRowsDialog
from ui.dialogs.missing_rows_dialog import MissingRowsDialog
from ui.dialogs.unique_values_dialog import UniqueValuesDialog
from ui.dialogs.data_types_dialog import DataTypesDialog
from ui.dialogs.memory_usage_dialog import MemoryUsageDialog
from ui.dialogs.chart_dialog import ChartDialog
from widgets.table_widget import TableWidget

class DataExplorerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.df = None
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Header
        header = QLabel("DATA EXPLORER")
        header.setStyleSheet("""
            font-size: 18px; 
            font-weight: bold; 
            color: #2c3e50;
            margin-bottom: 10px;
        """)
        layout.addWidget(header)

        # Feature buttons 
        features_layout = QGridLayout()
        features_layout.setSpacing(8)
        
        features = [
            ("Summary", self.show_summary),
            ("Complete Rows", self.show_complete_rows), 
            ("Missing Rows", self.show_missing_rows),
            ("Unique Values", self.show_unique_values),
            ("Data Types", self.show_data_types),
            ("Memory Usage", self.show_memory_usage),
            ("Chart", self.show_chart)
        ]

        for i, (text, slot) in enumerate(features):
            btn = QPushButton(text)
            btn.setFixedHeight(35)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;  /* TEKS PUTIH */
                    border: none;
                    border-radius: 4px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #21618c;
                }
            """)
            btn.clicked.connect(slot)
            features_layout.addWidget(btn, i // 4, i % 4)

        layout.addLayout(features_layout)

        # Data table
        table_label = QLabel("Data Preview")
        table_label.setStyleSheet("font-weight: bold; color: #2c3e50; margin-top: 10px;")
        layout.addWidget(table_label)

        self.data_table = TableWidget()
        layout.addWidget(self.data_table, 1)

    def update_data(self, df):
        """Update data when new dataset is loaded"""
        print(f"DataExplorer: update_data called with {type(df)}")
        
        try:
            self.df = df
            if df is not None and hasattr(df, 'columns'):
                print(f"DataExplorer: DataFrame shape {df.shape}")
                self.data_table.load_dataframe(df)  # Panggil load_dataframe
            else:
                print("DataExplorer: No valid data received")
                self.data_table.clear_table()
                
        except Exception as e:
            print(f"DataExplorer update error: {e}")
            self.data_table.clear_table()

    def clear_table(self):
        """Clear the table"""
        self.data_table.setRowCount(1)
        self.data_table.setColumnCount(1)
        self.data_table.setHorizontalHeaderLabels(["Info"])
        item = QTableWidgetItem("No data available")
        self.data_table.setItem(0, 0, item) 

    def populate_table(self, df):
        """Populate table with dataframe data"""
        try:
            if df is None or len(df) == 0:
                self.clear_table()
                return
                
            # Show first 1000 rows
            display_rows = min(1000, len(df))
            self.data_table.setRowCount(display_rows)
            self.data_table.setColumnCount(len(df.columns))
            self.data_table.setHorizontalHeaderLabels(df.columns.tolist())

            for i in range(display_rows):
                for j in range(len(df.columns)):
                    value = df.iloc[i, j]
                    item_text = str(value) if not pd.isna(value) else "NaN"
                    item = QTableWidgetItem(item_text)
                    self.data_table.setItem(i, j, item)  

            self.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            print(f"DataExplorer: Table populated with {display_rows} rows")  # Debug
            
        except Exception as e:
            print(f"DataExplorer populate error: {e}")  # Debug
            self.clear_table()

    # Feature methods
    def show_summary(self):
        if self.df is not None:
            try:
                dialog = SummaryDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing summary: {e}")

    def show_complete_rows(self):
        if self.df is not None:
            try:
                dialog = CompleteRowsDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing complete rows: {e}")

    def show_missing_rows(self):
        if self.df is not None:
            try:
                dialog = MissingRowsDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing missing rows: {e}")

    def show_unique_values(self):
        if self.df is not None:
            try:
                dialog = UniqueValuesDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing unique values: {e}")

    def show_data_types(self):
        if self.df is not None:
            try:
                dialog = DataTypesDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing data types: {e}")

    def show_memory_usage(self):
        if self.df is not None:
            try:
                dialog = MemoryUsageDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing memory usage: {e}")

    def show_chart(self):
        if self.df is not None:
            try:
                dialog = ChartDialog(self.df, self)
                dialog.exec()
            except Exception as e:
                print(f"Error showing chart: {e}")