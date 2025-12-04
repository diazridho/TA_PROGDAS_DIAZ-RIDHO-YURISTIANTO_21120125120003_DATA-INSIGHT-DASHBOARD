from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
import pandas as pd

class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_style()
        
    def setup_style(self):
        # Setup palette untuk warna teks
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor(44, 62, 80))  # #2c3e50
        palette.setColor(QPalette.ColorRole.WindowText, QColor(44, 62, 80))
        self.setPalette(palette)
        
        self.setStyleSheet("""
            TableWidget {
                background-color: white;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                gridline-color: #ecf0f1;
                color: #2c3e50;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 6px;
                border: none;
                font-weight: bold;
            }
            QTableWidget::item {
                padding: 4px;
                border-bottom: 1px solid #ecf0f1;
                color: #2c3e50;
                background-color: white;
            }
            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        
    def load_dataframe(self, df, max_rows=50):
        """Load pandas DataFrame into table"""
        try:
            if df is None or len(df) == 0:
                self.clear_table("No data available")
                return
                
            # Show first max_rows rows
            display_rows = min(max_rows, len(df))
            self.setRowCount(display_rows)
            self.setColumnCount(len(df.columns))
            self.setHorizontalHeaderLabels(df.columns.tolist())

            for i in range(display_rows):
                for j in range(len(df.columns)):
                    value = df.iloc[i, j]
                    item_text = str(value) if not pd.isna(value) else "NaN"
                    item = QTableWidgetItem(item_text)
                    # Set warna teks hitam
                    item.setForeground(QColor(0, 0, 0))  # Hitam solid
                    self.setItem(i, j, item)

            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            
        except Exception as e:
            print(f"Table load error: {e}")
            self.clear_table(f"Error: {str(e)}")
            
    def load_data(self, data, headers):
        """Load data from list of lists with custom headers"""
        try:
            if not data:
                self.clear_table("No data available")
                return
                
            self.setRowCount(len(data))
            self.setColumnCount(len(headers))
            self.setHorizontalHeaderLabels(headers)

            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    # Set warna teks hitam
                    item.setForeground(QColor(0, 0, 0))  # Hitam solid
                    self.setItem(i, j, item)

            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            
        except Exception as e:
            print(f"Table load error: {e}")
            self.clear_table(f"Error: {str(e)}")
            
    def clear_table(self, message="No data available"):
        """Clear the table with custom message"""
        self.setRowCount(1)
        self.setColumnCount(1)
        self.setHorizontalHeaderLabels(["Info"])
        item = QTableWidgetItem(message)
        item.setForeground(QColor(0, 0, 0))  # Hitam solid
        self.setItem(0, 0, item)