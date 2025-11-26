from core.data_loader import DataLoader
from core.data_analyzer import DataAnalyzer
from core.chart_generator import ChartGeneratorDouble, ChartGeneratorSingle
from matplotlib.figure import Figure 

if __name__ == "__main__":
    path = "data_tes/sample_demo.csv"
    df = DataLoader.DataLoad(path)
    
    tes = ChartGeneratorSingle()
    print(tes.__dict__)