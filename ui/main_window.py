from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
                            QStackedWidget, QListWidget, QListWidgetItem, QLabel)
from PyQt6.QtCore import Qt
from .dashboard_page import DashboardPage
from .data_explorer_page import DataExplorerPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Insight Dashboard")
        self.setGeometry(100, 100, 1000, 700)
        self.setup_ui()
        
    def setup_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Content area
        self.content_area = self.create_content_area()
        main_layout.addWidget(self.content_area, 1)
        
    def create_sidebar(self):
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #2c3e50;")
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(10, 20, 10, 20)
        layout.setSpacing(15)
        
        # App title
        title = QLabel("DATA INSIGHT")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Navigation
        self.nav_list = QListWidget()
        self.nav_list.setStyleSheet("""
            QListWidget {
                background-color: transparent;
                border: none;
                color: #bdc3c7;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 10px;
                border-radius: 3px;
            }
            QListWidget::item:selected {
                background-color: #34495e;
                color: white;
            }
        """)
        
        # Add pages
        pages = ["Dashboard", "Data Explorer"]
        for page in pages:
            item = QListWidgetItem(page)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.nav_list.addItem(item)
        
        self.nav_list.setCurrentRow(0)
        self.nav_list.currentRowChanged.connect(self.switch_page)
        layout.addWidget(self.nav_list)
        layout.addStretch()
        
        return sidebar
        
    def create_content_area(self):
        content = QWidget()
        content.setStyleSheet("background-color: #f8f9fa;")  # Background abu-abu muda
        
        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Stacked widget for pages
        self.stacked_widget = QStackedWidget()
        
        # Create pages
        self.dashboard_page = DashboardPage()
        self.data_explorer_page = DataExplorerPage()
        
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.data_explorer_page)
        
        layout.addWidget(self.stacked_widget)
        
        return content
        
    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        
    def get_dashboard_page(self):
        return self.dashboard_page
        
    def get_data_explorer_page(self):
        return self.data_explorer_page