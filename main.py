import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create main window
    window = MainWindow()
    window.show()
    
    # Connect data loading between pages, setelah window.show()
    try:
        dashboard = window.get_dashboard_page()
        data_explorer = window.get_data_explorer_page()
        
        # Connect signal
        dashboard.data_loaded.connect(data_explorer.update_data)
        print("Signals connected successfully")  
        
    except Exception as e:
        print(f"Error connecting signals: {e}")  
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()