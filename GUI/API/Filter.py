import scipy.signal as signal
import pandas as pd
import numpy as np

class Filter:

    @staticmethod
    def filter(data_raw):
        data = Filter.__band_filter(data_raw)
        data = Filter.__laplacian_filer(data)
        return data

    @staticmethod
    # Band filter that removes the spectrum of the signal.
    def __band_filter(data, low=0.00001, high=80):
        pd.DataFrame(data).plot(legend=False)
        nyq = 0.5 * 240
        low = low / nyq
        high = high / nyq
        a = signal.butter(20, [low, high], btype='band', analog=False, output='sos')
        y = signal.sosfilt(a, data)
        pd.DataFrame(y).plot(legend=False)
        print("Not implemented")
        return data

    @staticmethod
    # Enhance the difference between two channels.
    def __laplacian_filer(data):
        print("Not implemented")
        return data

    @staticmethod
    def fftnoise(f):
        f = np.array(f, dtype='complex')
        Np = (len(f) - 1) // 2
        phase = np.random.rand(Np) * 2 * np.pi
        phase = np.cos(phase) + 1j * np.sin(phase)
        f[1:-1-Np:-1] = np.conj(f[1:Np+1])
        return np.fft.ifft(f).real