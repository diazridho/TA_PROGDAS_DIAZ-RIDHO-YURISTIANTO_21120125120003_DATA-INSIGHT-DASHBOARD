from abc import ABC, abstractmethod

class abstract_single(ABC):
    # Data kategori
    @abstractmethod
    def bar_chart(self, data, column):
        pass

    @abstractmethod
    def pie_chart(self, data, column):
        pass
    
    # Data numerik
    @abstractmethod
    def histogram(self, data, column):
        pass

    @abstractmethod
    def box_plot(self, data, column):
        pass
    
    # Metadata chart/ data tentang data
    @abstractmethod
    def chart_type(self, data, column):
        ''' 
        Return jenis data:
        - univariat = 1 variabel
        - bivariate = 2 variabel
        
        '''
        pass

    

class abstract_double(ABC):
    @abstractmethod
    def line_chart(self, data, x_column, y_column):
        pass

    @abstractmethod
    def scatter_plot(self, data, x_column, y_column):
        pass

    @abstractmethod
    def chart_type(self, data, column):
        pass
