from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QListWidget, QListWidgetItem,
                            QFileDialog, QMessageBox)
from PyQt6.QtCore import Qt, pyqtSignal
from core.data_loader import DataLoader
from core.app_state import AppState
import os
from datetime import datetime

class DashboardPage(QWidget):
    data_loaded = pyqtSignal(object)  # Mengubah ke object untuk menerima dataframe
    
    def __init__(self):
        super().__init__()
        self.app_state = AppState()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Header
        header = QLabel("DASHBOARD")
        header.setStyleSheet("color: #2c3e50; font-size: 24px; font-weight: bold;")
        layout.addWidget(header)

        # Content
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)

        # Left - History
        left_panel = QWidget()
        left_panel.setFixedWidth(200)
        left_layout = QVBoxLayout(left_panel)
        
        history_label = QLabel("History")
        history_label.setStyleSheet("color: #2c3e50; font-size: 16px; font-weight: bold; margin-bottom: 10px;")
        left_layout.addWidget(history_label)

        self.history_list = QListWidget()
        self.history_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                color: #2c3e50;  /* WARNA TEKS DEFAULT */
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ecf0f1;
                color: #2c3e50;  /* WARNA TEKS ITEM */
                background-color: white;
            }
            QListWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #ecf0f1;
            }
        """)
        self.history_list.itemClicked.connect(self.on_history_click)
        left_layout.addWidget(self.history_list)

        content_layout.addWidget(left_panel)

        # Right - Load section
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        load_label = QLabel("LOAD FILE")
        load_label.setStyleSheet("color: #2c3e50; font-size: 16px; font-weight: bold; margin-bottom: 15px;")
        right_layout.addWidget(load_label)

        self.load_btn = QPushButton("Choose File")
        self.load_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.load_btn.clicked.connect(self.load_file)
        right_layout.addWidget(self.load_btn)

        # File info
        self.file_info = QLabel("No file loaded")
        self.file_info.setStyleSheet("color: #7f8c8d; font-size: 12px; margin-top: 10px;")
        right_layout.addWidget(self.file_info)

        right_layout.addStretch()
        content_layout.addWidget(right_panel, 1)

        layout.addLayout(content_layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Data File",
            "",
            "Data Files (*.csv *.xlsx *.json *.parquet *.txt);;All Files (*)"
        )
        
        if file_path:
            try:
                # Load data
                df = DataLoader.DataLoad(file_path)
                file_name = os.path.basename(file_path)
                
                # Add to app state
                key = f"{file_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                self.app_state.set_datasets(key, file_path, df)
                self.app_state.set_current_key(key)
                
                # Update UI
                self.update_history()
                rows, cols = df.shape
                self.file_info.setText(f"Loaded: {file_name} ({rows} rows × {cols} cols)")
                
                # Emit signal dengan DataFrame
                self.data_loaded.emit(df)
                
                print(f"File loaded successfully: {file_name}")  # Debug
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {str(e)}")
                print(f"Load error: {e}")  # Debug

    def update_history(self):
        self.history_list.clear()
        keys = self.app_state.list_keys()
        
        for key in keys:
            path = self.app_state.get_path(key)
            if path:
                file_name = os.path.basename(path)
                item = QListWidgetItem(f"📊 {file_name}")
                item.setData(Qt.ItemDataRole.UserRole, key)
                self.history_list.addItem(item)

    def on_history_click(self, item):
        key = item.data(Qt.ItemDataRole.UserRole)
        if key:
            self.app_state.set_current_key(key)
            df = self.app_state.get_dataframe(key)
            path = self.app_state.get_path(key)
            file_name = os.path.basename(path)
            
            if df is not None:
                rows, cols = df.shape
                self.file_info.setText(f"Loaded: {file_name} ({rows} rows × {cols} cols)")
                # Emit signal dengan DataFrame
                self.data_loaded.emit(df)
                print(f"History item clicked: {file_name}")  # Debug