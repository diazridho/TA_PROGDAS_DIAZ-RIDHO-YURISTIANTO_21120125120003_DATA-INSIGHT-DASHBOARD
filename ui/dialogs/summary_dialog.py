from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt
from core.data_analyzer import DataAnalyzer
import pandas as pd
from widgets.table_widget import TableWidget

class SummaryDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.setWindowTitle("Summary")
        self.setGeometry(200, 200, 700, 500)
        
        layout = QVBoxLayout(self)
        
        # Table
        self.table = TableWidget()
        layout.addWidget(self.table)
        
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
        self.populate_summary()
        
    def populate_summary(self):
        summary_df = DataAnalyzer.summary(self.df)
        
        # Pastikan summary_df adalah DataFrame, bukan string
        if isinstance(summary_df, pd.DataFrame):
            self.table.setRowCount(len(summary_df))
            self.table.setColumnCount(len(summary_df.columns))
            self.table.setHorizontalHeaderLabels(summary_df.columns.tolist())
            self.table.setVerticalHeaderLabels(summary_df.index.tolist())
            
            for i in range(len(summary_df)):
                for j in range(len(summary_df.columns)):
                    value = summary_df.iloc[i, j]
                    item = QTableWidgetItem(str(value) if not pd.isna(value) else "N/A")
                    self.table.setItem(i, j, item)  # PERBAIKAN: tambah item