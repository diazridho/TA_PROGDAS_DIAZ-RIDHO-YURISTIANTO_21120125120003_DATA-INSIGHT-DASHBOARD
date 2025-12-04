from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt
from core.data_analyzer import DataAnalyzer
from widgets.table_widget import TableWidget

class DataTypesDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.setWindowTitle("Data Types")
        self.setGeometry(200, 200, 400, 500)
        
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
        self.populate_data_types()
        
    def populate_data_types(self):
        dtypes_series = DataAnalyzer.data_types(self.df)
        
        self.table.setRowCount(len(dtypes_series))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Column", "Data Type"])
        
        for i, (col_name, dtype) in enumerate(dtypes_series.items()):
            item1 = QTableWidgetItem(col_name)
            item2 = QTableWidgetItem(str(dtype))
            self.table.setItem(i, 0, item1)
            self.table.setItem(i, 1, item2)