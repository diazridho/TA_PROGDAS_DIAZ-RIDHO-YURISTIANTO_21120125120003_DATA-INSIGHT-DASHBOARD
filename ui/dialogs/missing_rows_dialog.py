from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel
from PyQt6.QtCore import Qt
from core.data_analyzer import DataAnalyzer
import pandas as pd
from widgets.table_widget import TableWidget

class MissingRowsDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.setWindowTitle("Missing Rows")
        self.setGeometry(200, 200, 800, 500)
        
        layout = QVBoxLayout(self)
        
        # Count info
        count = DataAnalyzer.sum_missing_rows(self.df)
        total = len(self.df)
        info_label = QLabel(f"Missing rows: {count} / {total}")
        layout.addWidget(info_label)
        
        # Table
        self.table = TableWidget()
        layout.addWidget(self.table)
        
        # Close button
                # Close button
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        self.populate_missing_rows()
        
    def populate_missing_rows(self):
        missing_df = DataAnalyzer.show_missing_rows(self.df)
        
        if missing_df is not None and len(missing_df) > 0:
            display_df = missing_df.head(100)
            
            self.table.setRowCount(len(display_df))
            self.table.setColumnCount(len(display_df.columns))
            self.table.setHorizontalHeaderLabels(display_df.columns.tolist())
            
            for i in range(len(display_df)):
                for j in range(len(display_df.columns)):
                    value = display_df.iloc[i, j]
                    item = QTableWidgetItem(str(value) if not pd.isna(value) else "NaN")
                    self.table.setItem(i, j, item)  # PERBAIKAN: tambah item
        else:
            # Jika tidak ada missing rows
            self.table.setRowCount(1)
            self.table.setColumnCount(1)
            self.table.setHorizontalHeaderLabels(["Info"])
            item = QTableWidgetItem("No missing rows found")
            self.table.setItem(0, 0, item)  # PERBAIKAN: tambah item