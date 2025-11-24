from core.data_loader import DataLoader
from core.data_analyzer import DataAnalyzer

if __name__ == "__main__":
    path = "data_tes/sample_demo.csv"
    df = DataLoader.DataLoad(path)
    
    tes = DataAnalyzer.complete_rows(df)
    
    tes_mis = DataAnalyzer.missing_rows(df)
    print("Msing:\n", tes_mis)