from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QComboBox, 
                            QPushButton, QLabel)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from core.chart_generator import ChartGeneratorSingle, ChartGeneratorDouble

class ChartDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.single_generator = ChartGeneratorSingle()
        self.double_generator = ChartGeneratorDouble()
        
        self.setWindowTitle("Chart Generator")
        self.setGeometry(200, 200, 800, 700)
        
        # SET STYLE UNTUK SELURUH DIALOG
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QLabel {
                color: #2c3e50;
                font-weight: bold;
            }
            QComboBox {
                background-color: white;
                color: #2c3e50;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 5px;
                min-width: 100px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
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
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Chart type selection
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Chart Type:"))
        
        self.chart_type_combo = QComboBox()
        chart_types = [
            "Single: Bar Chart",
            "Single: Pie Chart", 
            "Single: Histogram",
            "Single: Heatmap",
            "Single: Box Plot",
            "Double: Histogram",
            "Double: Bar Chart", 
            "Double: Scatter Plot"
        ]
        self.chart_type_combo.addItems(chart_types)
        self.chart_type_combo.currentTextChanged.connect(self.on_chart_type_changed)
        type_layout.addWidget(self.chart_type_combo)
        type_layout.addStretch()
        layout.addLayout(type_layout)
        
        # Column selection
        self.columns_layout = QHBoxLayout()
        layout.addLayout(self.columns_layout)
        
        # Chart area
        self.figure = Figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas, 1)
        
        # Generate button
        generate_btn = QPushButton("Generate Chart")
        generate_btn.clicked.connect(self.generate_chart)
        layout.addWidget(generate_btn)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        # Setup initial UI
        self.on_chart_type_changed(self.chart_type_combo.currentText())
        
    def on_chart_type_changed(self, chart_type):
        # Clear previous column selections
        self.clear_layout(self.columns_layout)
        
        if "Single:" in chart_type:
            # Single column selection
            self.columns_layout.addWidget(QLabel("Column:"))
            self.column_combo = QComboBox()
            self.column_combo.addItems(self.df.columns.tolist())
            self.columns_layout.addWidget(self.column_combo)
            
        elif "Double:" in chart_type:
            # Double column selection
            self.columns_layout.addWidget(QLabel("X Column:"))
            self.x_column_combo = QComboBox()
            self.x_column_combo.addItems(self.df.columns.tolist())
            self.columns_layout.addWidget(self.x_column_combo)
            
            self.columns_layout.addWidget(QLabel("Y Column:"))
            self.y_column_combo = QComboBox()
            self.y_column_combo.addItems(self.df.columns.tolist())
            self.columns_layout.addWidget(self.y_column_combo)
            
        self.columns_layout.addStretch()
        
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
    def generate_chart(self):
        chart_type = self.chart_type_combo.currentText()
        
        try:
            if chart_type == "Single: Bar Chart":
                column = self.column_combo.currentText()
                new_figure = self.single_generator.bar_chart(self.df, column)
            elif chart_type == "Single: Pie Chart":
                column = self.column_combo.currentText()
                new_figure = self.single_generator.pie_chart(self.df, column)
            elif chart_type == "Single: Histogram":
                column = self.column_combo.currentText()
                new_figure = self.single_generator.histogram(self.df, column)
            elif chart_type == "Single: Heatmap":
                column = self.column_combo.currentText()
                new_figure = self.single_generator.heatmap(self.df, column)
            elif chart_type == "Single: Box Plot":
                column = self.column_combo.currentText()
                new_figure = self.single_generator.box_plot(self.df, column)
            elif chart_type == "Double: Histogram":
                x_column = self.x_column_combo.currentText()
                y_column = self.y_column_combo.currentText()
                new_figure = self.double_generator.histogram(self.df, x_column, y_column)
            elif chart_type == "Double: Bar Chart":
                x_column = self.x_column_combo.currentText()
                y_column = self.y_column_combo.currentText()
                new_figure = self.double_generator.bar_chart(self.df, x_column, y_column)
            elif chart_type == "Double: Scatter Plot":
                x_column = self.x_column_combo.currentText()
                y_column = self.y_column_combo.currentText()
                new_figure = self.double_generator.scatter_plot(self.df, x_column, y_column)
            else:
                raise ValueError(f"Unknown chart type: {chart_type}")
            
            self.update_canvas(new_figure)
            
        except Exception as e:
            self.show_error(str(e))
            
    def update_canvas(self, new_figure):
        """Update canvas dengan figure baru"""
        self.canvas.figure = new_figure
        self.canvas.draw()
        
    def show_error(self, error_message):
        """Tampilkan error message di canvas"""
        error_fig = Figure(figsize=(8, 6))
        ax = error_fig.add_subplot(111)
        ax.text(0.5, 0.5, f"Error: {error_message}", 
               ha='center', va='center', transform=ax.transAxes, fontsize=12)
        ax.set_title("Chart Generation Error")
        ax.set_xticks([])
        ax.set_yticks([])
        
        self.canvas.figure = error_fig
        self.canvas.draw()