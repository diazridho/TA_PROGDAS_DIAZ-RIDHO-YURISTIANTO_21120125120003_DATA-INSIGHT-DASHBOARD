class AppState:
    def __init__(self):
        self.__datasets = {}
        self.current_key = None

    # format yang akan dimasukkan ke self.__datasets
    def set_datasets(self, key, path, df):
        self.__datasets[key] = {'path': path, 'dataframe': df}

    # mendapatkan dataframe berdasarkan key
    def get_dataframe(self, key):
        rec = self.__datasets.get(key)
        return rec['dataframe'] if rec else None
    
    # mendapatkan path berdasarkan key
    def get_path(self, key):
        rec = self.__datasets.get(key)
        return rec['path'] if rec else None
    
    # key yang digunakan saat ini, akan terus berubah sesuai dengan pilihan user
    def set_current_key(self, key):
        if key in self.__datasets:
            self.current_key = key

    # mendapatkan key yang sedang digunakan
    def get_current_key(self):
        return self.current_key
    
    # mendapatkan dataframe yang sedang digunakan
    def get_current_dataframe(self):
        return self.get_dataframe(self.current_key) if self.current_key else None
    
    # mendapatkan semua key yang tersedia
    def list_keys(self):
        return list(self.__datasets.keys())

            