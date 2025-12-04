from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel
from PyQt6.QtCore import Qt
from core.data_analyzer import DataAnalyzer
import pandas as pd
from widgets.table_widget import TableWidget

class MemoryUsageDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.setWindowTitle("Memory Usage")
        self.setGeometry(200, 200, 400, 500)
        
        layout = QVBoxLayout(self)
        
        # Total memory info
        total_memory = self.df.memory_usage(deep=True).sum()
        info_label = QLabel(f"Total memory: {total_memory / 1024:.2f} KB")
        layout.addWidget(info_label)
        
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
        self.populate_memory_usage()
        
    def populate_memory_usage(self):
        memory_series = DataAnalyzer.memory_usage(self.df)
        
        # Filter out index
        memory_data = [(col, memory) for col, memory in memory_series.items() if col != "Index"]
        
        self.table.setRowCount(len(memory_data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Column", "Memory (Bytes)"])
        
        for i, (col_name, memory) in enumerate(memory_data):
            item1 = QTableWidgetItem(col_name)
            item2 = QTableWidgetItem(str(memory))
            self.table.setItem(i, 0, item1)
            self.table.setItem(i, 1, item2)