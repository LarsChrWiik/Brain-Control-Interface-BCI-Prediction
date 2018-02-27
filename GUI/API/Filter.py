

class Filter:

    @staticmethod
    def filter(self, data_raw):
        data = self.band_filter(data_raw)
        data = self.laplacian_filer(data)
        return data

    @staticmethod
    # Band filter that removes the spectrum of the signal.
    def __band_filter(data):
        print("Not implemented")
        return data

    @staticmethod
    # Enhance the difference between two channels.
    def __laplacian_filer(data):
        print("Not implemented")
        return data
        
