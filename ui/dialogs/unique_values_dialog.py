from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt
from core.data_analyzer import DataAnalyzer
from widgets.table_widget import TableWidget

class UniqueValuesDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.setWindowTitle("Unique Values")
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
        self.populate_unique_values()
        
    def populate_unique_values(self):
        unique_series = DataAnalyzer.unique_values(self.df)
        
        self.table.setRowCount(len(unique_series))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Column", "Unique Values"])
        
        for i, (col_name, unique_count) in enumerate(unique_series.items()):
            self.table.setItem(i, 0, QTableWidgetItem(col_name))
            self.table.setItem(i, 1, QTableWidgetItem(str(unique_count)))
            # PERBAIKAN: sebenarnya ini sudah benar, tapi pastikan seperti ini:
            item1 = QTableWidgetItem(col_name)
            item2 = QTableWidgetItem(str(unique_count))
            self.table.setItem(i, 0, item1)
            self.table.setItem(i, 1, item2)