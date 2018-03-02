import scipy.signal as signal
import numpy as np
from GUI.Visualization import Visualization
from scipy.ndimage.filters import gaussian_laplace as gl
from typing import Union

class Filter:

    @staticmethod
    def filter(data_raw: dict, sigma: int=1) -> dict:
        """Band Filter and Laplace Filter
        This is the only public function please call all private functions from here.
        You can call Notch & Band pass filters with selectable bandwidth.

        It would be easy for me to add lowpass and highpass filters as well. if needed?

        Args:
            data_raw (dict): Has to be 2D??, non-empty, dict type and in the shape of (TimeSteps, EachEEGSensor)

        :returns
            dict: the filtered signal
        """
        data = Filter.__band_filter(data_raw, lowFreq=2, highFreq=70, filterType='bandstop')
        data = Filter.__laplacian_filter(data,sigma) #Need to write test for this once its complete
        return data

    @staticmethod
    def __band_filter(data: dict, lowFreq: Union[int, float], highFreq: Union[int, float], timestep: int=0,
                      samplingFreq: int=240, order: int=5, eegSensor: int=0, filterType: str='bandpass',
                      lengthOfTestSeconds: Union[int, float]=32, example: int=0) -> dict:
        """Bandpass and Notch filter
            Mostly done, still looking at another implementation of Unit Testing using the 'import UnitTest' lib, but this
            will do for now, it is still unit testing just needs to be made neater. The Graph code needs to be put somewhere
            else. It was only for testing purposes but seems like a nice pre-processing thing.

            Comments in code below for sugestions!

            :args
                data (dict): Has to be a 2D, non empty, dict type
                lowFreq (int, float): (Hz) Can not be higher than highFreq
                highFreq (int, float): (Hz) Can not be lower and lowFreq
                samplingFreq (int): The sampling resolution fo the EEG capture device
                order (int): How much delay to use when processing the signal. Above 6 tends to go unpredictable
                eegSensor (int): Has to be between 0-64. I'm not sure if you can get EEG's bigger than 64 sensors
                filterType (Str): There are 2 types of filters. 'bandpass' & 'bandstop'
                lengthOfTestSeconds (int, float): this is only used for the graph - not really needed for core functionality.

            :returns
                dict: The freqencies with in the bounds of lowFreq & highFreq
            """
        #Test
        # Filter.__band_filter_test(data=data, low=lowFreq, high=highFreq, samplingFreq=samplingFreq, order=order,
        #                           eegSensor=eegSensor, filterType=filterType, lengthOfTestSeconds=lengthOfTestSeconds)
        #Code
        nyq = 0.5 * samplingFreq
        low = lowFreq / nyq
        high = highFreq / nyq
        b, a = signal.butter(order, [low, high], btype=filterType)
        y = signal.lfilter(b, a, data['Signal'])
        ##Graph - This belongs somewhere else probably.
        # t = np.linspace(0, len(data), len(data), endpoint=False)
        # plt.plot(t, y, label='Sensor #' + str(eegSensor) + ' (' + str(lowFreq) + '-' + str(highFreq) + ') Hz')
        # plt.grid(True)
        # plt.axis('tight')
        # plt.xticks(range(10), range(lengthOfTestSeconds)) ##32 seconds per test?
        # plt.xlabel("Time in Seconds")
        # plt.legend(loc='upper left')
        # plt.show()
        output = {}
        timestep = []
        for index, eegChannel in enumerate(y[0]):#the extra [0] is becuase signal.lfilter() puts it in a 1D array. Grrr
            timestep.append(eegChannel)
        output['Signal'] = timestep
        Visualization.channelGraph(y[0][0])
        return output #output is 2D 64xTimeSamples


    # @staticmethod
    # def __band_filter_test(data, low, high, samplingFreq, order, eegSensor, filterType, lengthOfTestSeconds):
        # assert filterType == 'bandstop' or filterType == 'bandpass'
        # assert eegSensor >= 0 and eegSensor <= 64
        # assert order >= 0 ##Need to look at max bounds, when it gets over 6 it makes silly graphs, not sure why yet
        # assert samplingFreq > 1 and type(samplingFreq) == type(int())## maybe low resolution infra-low brain wave study could need it?
        # assert low >= 0.00001 and low  < 150 #Ask Jossip about max bounds
        # assert low < high and high > low
        # assert high >= 0.00001 and high < 150
        # assert type(data) == dict and data.shape[0] > 0 and len(data.shape) == 2
        # assert lengthOfTestSeconds > 0.00001

    @staticmethod
    # Enhance the difference between two channels.
    def __laplacian_filter(data, sigma):

        #Initialise a matrix with only zeroes to represent the positions of sensors
        #An additional column and row is added to each side
        matrix = np.zeros((13, 12))
        #data = data[0]  # Needs a for loop through the examples and ? additional dimension

        #Map the values to their respective locations to the previously created zero matrix
        data = data['Signal']
        matrix[1][4] = data[21][0]
        matrix[1][6] = data[22][0]
        matrix[1][8] = data[23][0]
        matrix[2][3] = data[24][0]
        matrix[2][4] = data[25][0]
        matrix[2][6] = data[26][0]
        matrix[2][8] = data[27][0]
        matrix[2][9] = data[28][0]
        matrix[3][2:11] = np.array(data[29:38])[:,0]
        matrix[4][3:10] = np.array(data[0:7])[:,0]
        matrix[4][2] = data[38][0]
        matrix[4][10] = data[39][0]
        matrix[5][1] = data[42][0]
        matrix[5][2] = data[40][0]
        matrix[5][3:10] = np.array(data[7:14])[:,0]
        matrix[5][10] = data[42][0]
        matrix[5][11] = data[43][0]
        matrix[6][2] = data [44][0]
        matrix[6][3:10] = np.array(data[14:21])[:,0]
        matrix[6][10] = data[45][0]
        matrix[7][2:11] = np.array(data[46:55])[:,0]
        matrix[8][3] = data[55][0]
        matrix[8][4] = data[56][0]
        matrix[8][6] = data[57][0]
        matrix[8][8] = data[58][0]
        matrix[8][9] = data[59][0]
        matrix[9][4] = data[60][0]
        matrix[9][6] = data[61][0]
        matrix[9][8] = data[62][0]
        matrix[10][6] = data[63][0]

        #filter the matrix using a laplacian gaussian filter

        matrix = gl(matrix, sigma, output=None, mode='reflect', cval=0.0)

        #Save the values of the matrix to the previous format (chanal_id)

        data[21] = matrix[1][4]
        data[22] = matrix[1][6]
        data[23] = matrix[1][8]
        data[24] = matrix[2][3]
        data[25] = matrix[2][4]
        data[26] = matrix[2][6]
        data[27] = matrix[2][8]
        data[28] = matrix[2][9]
        np.array(data[29:38])[:,0] = matrix[3][2:11]
        np.array(data[0:7])[:,0] = matrix[4][3:10]
        data[38] = matrix[4][2]
        data[39] = matrix[4][10]
        data[42] = matrix[5][1]
        data[40] = matrix[5][2]
        np.array(data[7:14])[:,0] = matrix[5][3:10]
        data[41] = matrix[5][10]
        data[43] = matrix[5][11]
        data[44] = matrix[6][2]
        np.array(data[14:21])[:,0] = matrix[6][3:10]
        data[45] = matrix[6][10]
        np.array(data[46:55])[:,0] = matrix[7][2:11]
        data[55] = matrix[8][3]
        data[56] = matrix[8][4]
        data[57] = matrix[8][6]
        data[58] = matrix[8][8]
        data[59] = matrix[8][9]
        data[60] = matrix[9][4]
        data[61] = matrix[9][6]
        data[62] = matrix[9][8]
        data[63] = matrix[10][6]
        Visualization.channelGraph(data[0])
        return data

if __name__ == "__main__":
    pass
