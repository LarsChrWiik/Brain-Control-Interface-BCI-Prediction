import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from typing import Union

class Filter:

    @staticmethod
    def filter(data_raw: np.ndarray) -> np.ndarray:
        """Band Filter and Laplace Filter
        This is the only public function please call all private functions from here.
        You can call Notch & Band pass filters with selectable bandwidth.

        It would be easy for me to add lowpass and highpass filters as well. if needed?

        Args:
            data_raw (np.ndarray): Has to be 2D, non-empty, ndarray type and in the shape of (TimeSteps, EachEEGSensor)

        :returns
            np.ndarray: the filtered signal
        """
        assert type(data_raw) == np.ndarray and data_raw.shape[0] > 0 and len(data_raw.shape) == 2
        data = Filter.__band_filter(data_raw, lowFreq=10, highFreq=12)
        data = Filter.__laplacian_filter(data) #Need to write test for this once its complete
        assert data == type(np.ndarray) and data.shape[0] > 0# relook after laplacian written
        return data

    @staticmethod
    def __band_filter(data: np.ndarray, lowFreq: Union[int, float], highFreq: Union[int, float], samplingFreq: int=240,
                      order: int=5, eegSensor: int=0, filterType: str='bandpass',
                      lengthOfTestSeconds: Union[int, float]=32) -> np.ndarray:
        """Bandpass and Notch filter
            Mostly done, still looking at another implementation of Unit Testing using the 'import UnitTest' lib, but this
            will do for now, it is still unit testing just needs to be made neater. The Graph code needs to be put somewhere
            else. It was only for testing purposes but seems like a nice pre-processing thing.

            Comments in code below for sugestions!

            :args
                data (np.ndarray): Has to be a 2D, non empty, ndarray type
                lowFreq (int, float): (Hz) Can not be higher than highFreq
                highFreq (int, float): (Hz) Can not be lower and lowFreq
                samplingFreq (int): The sampling resolution fo the EEG capture device
                order (int): How much delay to use when processing the signal. Above 6 tends to go unpredictable
                eegSensor (int): Has to be between 0-64. I'm not sure if you can get EEG's bigger than 64 sensors
                filterType (Str): There are 2 types of filters. 'bandpass' & 'bandstop'
                lengthOfTestSeconds (int, float): this is only used for the graph - not really needed for core functionality.

            :returns
                np.ndarray: The freqencies with in the bounds of lowFreq & highFreq
            """
        #Test
        Filter.__band_filter_test(data=data, low=lowFreq, high=highFreq, samplingFreq=samplingFreq, order=order,
                                  eegSensor=eegSensor, filterType=filterType, lengthOfTestSeconds=lengthOfTestSeconds)
        #Code
        nyq = 0.5 * samplingFreq
        low = lowFreq / nyq
        high = highFreq / nyq
        data = data[:, eegSensor]
        b, a = signal.butter(order, [low, high], btype=filterType)
        y = signal.lfilter(b, a, data)
        ##Graph - This belongs somewhere else probably.
        t = np.linspace(0, len(data), len(data), endpoint=False)
        plt.plot(t, y, label='Sensor #' + str(eegSensor) + ' (' + str(lowFreq) + '-' + str(highFreq) + ') Hz')
        plt.grid(True)
        plt.axis('tight')
        tick = np.linspace(0, len(data), len(data) / samplingFreq)
        plt.xticks(tick, range(lengthOfTestSeconds)) ##32 seconds per test?
        plt.xlabel("Time in Seconds")
        plt.legend(loc='upper left')
        plt.show()
        return y


    @staticmethod
    def __band_filter_test(data, low, high, samplingFreq, order, eegSensor, filterType, lengthOfTestSeconds):
        assert filterType == 'bandstop' or filterType == 'bandpass'
        assert eegSensor >= 0 and eegSensor <= 64
        assert order >= 0 ##Need to look at max bounds, when it gets over 6 it makes silly graphs, not sure why yet
        assert samplingFreq > 1 and type(samplingFreq) == type(int())## maybe low resolution infra-low brain wave study could need it?
        assert low >= 0.00001 and low  < 150 #Ask Jossip about max bounds
        assert low < high and high > low
        assert high >= 0.00001 and high < 150
        assert type(data) == np.ndarray and data.shape[0] > 0 and len(data.shape) == 2
        assert lengthOfTestSeconds > 0.00001

    @staticmethod
    # Enhance the difference between two channels.
    def __laplacian_filter(data):
        print("Not implemented")
        return data

if __name__ == "__main__":
    pass