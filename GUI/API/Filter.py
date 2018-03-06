import scipy.signal as signal
import numpy as np
from GUI.Visualization import Visualization
from scipy.ndimage.filters import gaussian_laplace as gl
from typing import Union

#TODO: Move to Preprocessing folder. 
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
        data = Filter.__laplacian_filter(data, sigma) #Need to write test for this once its complete
        return data

    @staticmethod
    def __band_filter(
            data,
            lowFreq: Union[int, float],
            highFreq: Union[int, float],
            timestep: int = 0,
            samplingFreq: int = 240,
            order: int = 5,
            eegSensor: int = 0,
            filterType: str = 'bandpass',
            lengthOfTestSeconds: Union[int, float] = 32,
            example: int = 0
    ):
        filtered_channels = []
        for example in data["Signal"]:
            examples = []
            for j in range(len(example)):
                filtered_channel = Filter.__band_filter_sample(
                    example[j],
                    lowFreq,
                    highFreq,
                    timestep,
                    samplingFreq,
                    order,
                    eegSensor,
                    filterType,
                    lengthOfTestSeconds,
                    example
                )
                examples.append(filtered_channel)
            filtered_channels.append(examples)
        data["Signal"] = filtered_channels
        return data

    @staticmethod
    def __band_filter_sample(
            channel,
            lowFreq: Union[int, float],
            highFreq: Union[int, float],
            timestep: int=0,
            samplingFreq: int=240,
            order: int=5,
            eegSensor: int=0,
            filterType: str='bandpass',
            lengthOfTestSeconds: Union[int, float]=32,
            example: int=0
    ):
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
        y = signal.lfilter(b, a, channel)
        ##Graph - This belongs somewhere else probably.
        # t = np.linspace(0, len(data), len(data), endpoint=False)
        # plt.plot(t, y, label='Sensor #' + str(eegSensor) + ' (' + str(lowFreq) + '-' + str(highFreq) + ') Hz')
        # plt.grid(True)
        # plt.axis('tight')
        # plt.xticks(range(10), range(lengthOfTestSeconds)) ##32 seconds per test?
        # plt.xlabel("Time in Seconds")
        # plt.legend(loc='upper left')
        # plt.show()


        #Visualization.channelGraph(y[0][0])
        return y

    @staticmethod
    def __laplacian_filter(data, sigma):
        for i in range(len(data["Signal"])):
            example = data["Signal"][i]
            transposed = np.transpose(example)
            new_time_steps = []
            for j in range(len(transposed)):
                new_time_step = Filter.__laplacian_filter_sample(transposed[j], sigma)
                new_time_steps.append(new_time_step)
            transposed_back = np.transpose(new_time_steps)
            data["Signal"][i] = transposed_back
        return data

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
    def __laplacian_filter_sample(time_step, sigma):

        #Initialise a matrix with only zeroes to represent the positions of sensors
        #An additional column and row is added to each side
        matrix = np.zeros((13, 12))
        #data = data[0]  # Needs a for loop through the examples and ? additional dimension

        #Map the values to their respective locations to the previously created zero matrix

        # Row 1
        matrix[1][4] = time_step[21]
        matrix[1][6] = time_step[22]
        matrix[1][8] = time_step[23]

        # Row 2
        matrix[2][3] = time_step[24]
        matrix[2][4] = time_step[25]
        matrix[2][6] = time_step[26]
        matrix[2][8] = time_step[27]
        matrix[2][9] = time_step[28]

        # Row 3
        matrix[3][2] = time_step[29]
        matrix[3][3] = time_step[30]
        matrix[3][4] = time_step[31]
        matrix[3][5] = time_step[32]
        matrix[3][6] = time_step[33]
        matrix[3][7] = time_step[34]
        matrix[3][8] = time_step[35]
        matrix[3][9] = time_step[36]
        matrix[3][10] = time_step[37]

        # Row 4
        matrix[4][2] = time_step[38]
        matrix[4][3] = time_step[0]
        matrix[4][4] = time_step[1]
        matrix[4][5] = time_step[2]
        matrix[4][6] = time_step[3]
        matrix[4][7] = time_step[4]
        matrix[4][8] = time_step[5]
        matrix[4][9] = time_step[6]
        matrix[4][10] = time_step[39]

        # Row 5
        matrix[5][1] = time_step[42]
        matrix[5][2] = time_step[40]
        matrix[5][3] = time_step[7]
        matrix[5][4] = time_step[8]
        matrix[5][5] = time_step[9]
        matrix[5][6] = time_step[10]
        matrix[5][7] = time_step[11]
        matrix[5][8] = time_step[12]
        matrix[5][9] = time_step[13]
        matrix[5][10] = time_step[41]
        matrix[5][11] = time_step[43]

        # Row 6
        matrix[6][2] = time_step [44]
        matrix[6][3] = time_step[14]
        matrix[6][4] = time_step[15]
        matrix[6][5] = time_step[16]
        matrix[6][6] = time_step[17]
        matrix[6][7] = time_step[18]
        matrix[6][8] = time_step[19]
        matrix[6][9] = time_step[20]
        matrix[6][10] = time_step[45]

        # Row 7
        matrix[7][2] = time_step[46]
        matrix[7][3] = time_step[47]
        matrix[7][4] = time_step[48]
        matrix[7][5] = time_step[49]
        matrix[7][6] = time_step[50]
        matrix[7][7] = time_step[51]
        matrix[7][8] = time_step[52]
        matrix[7][9] = time_step[53]
        matrix[7][10] = time_step[54]

        # Row 8
        matrix[8][3] = time_step[55]
        matrix[8][4] = time_step[56]
        matrix[8][6] = time_step[57]
        matrix[8][8] = time_step[58]
        matrix[8][9] = time_step[59]

        # Row 9
        matrix[9][4] = time_step[60]
        matrix[9][6] = time_step[61]
        matrix[9][8] = time_step[62]

        # Row 10
        matrix[10][6] = time_step[63]



        #filter the matrix using a laplacian gaussian filter

        matrix = gl(matrix, sigma, output=None, mode='reflect', cval=0.0)

        #Save the values of the matrix to the previous format (chanal_id)

        # Row 1
        time_step[21] = matrix[1][4]
        time_step[22] = matrix[1][6]
        time_step[23] = matrix[1][8]

        # Row 2
        time_step[24] = matrix[2][3]
        time_step[25] = matrix[2][4]
        time_step[26] = matrix[2][6]
        time_step[27] = matrix[2][8]
        time_step[28] = matrix[2][9]

        # Row 3
        time_step[29] = matrix[3][2]
        time_step[30] = matrix[3][3]
        time_step[31] = matrix[3][4]
        time_step[32] = matrix[3][5]
        time_step[33] = matrix[3][6]
        time_step[34] = matrix[3][7]
        time_step[35] = matrix[3][8]
        time_step[36] = matrix[3][9]
        time_step[37] = matrix[3][10]

        # Row 4
        time_step[38] = matrix[4][2]
        time_step[0] = matrix[4][3]
        time_step[1] = matrix[4][4]
        time_step[2] = matrix[4][5]
        time_step[3] = matrix[4][6]
        time_step[4] = matrix[4][7]
        time_step[5] = matrix[4][8]
        time_step[6] = matrix[4][9]
        time_step[39] = matrix[4][10]

        # Row 5
        time_step[42] = matrix[5][1]
        time_step[40] = matrix[5][2]
        time_step[7] = matrix[5][3]
        time_step[8] = matrix[5][4]
        time_step[9] = matrix[5][5]
        time_step[10] = matrix[5][6]
        time_step[11] = matrix[5][7]
        time_step[12] = matrix[5][8]
        time_step[13] = matrix[5][9]
        time_step[41] = matrix[5][10]
        time_step[43] = matrix[5][11]

        # Row 6
        time_step[44] = matrix[6][2]
        time_step[14] = matrix[6][3]
        time_step[15] = matrix[6][4]
        time_step[16] = matrix[6][5]
        time_step[17] = matrix[6][6]
        time_step[18] = matrix[6][7]
        time_step[19] = matrix[6][8]
        time_step[20] = matrix[6][9]
        time_step[45] = matrix[6][10]

        # Row 7
        time_step[46] = matrix[7][2]
        time_step[47] = matrix[7][3]
        time_step[48] = matrix[7][4]
        time_step[49] = matrix[7][5]
        time_step[50] = matrix[7][6]
        time_step[51] = matrix[7][7]
        time_step[52] = matrix[7][8]
        time_step[53] = matrix[7][9]
        time_step[54] = matrix[7][10]

        # Row 8
        time_step[55] = matrix[8][3]
        time_step[56] = matrix[8][4]
        time_step[57] = matrix[8][6]
        time_step[58] = matrix[8][8]
        time_step[59] = matrix[8][9]

        # Row 9
        time_step[60] = matrix[9][4]
        time_step[61] = matrix[9][6]
        time_step[62] = matrix[9][8]

        # Row 10
        time_step[63] = matrix[10][6]

        return time_step

if __name__ == "__main__":
    pass
