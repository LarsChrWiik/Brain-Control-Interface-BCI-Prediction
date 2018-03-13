import scipy.signal as signal
import numpy as np
from scipy.ndimage.filters import gaussian_laplace as gl
from typing import Union

class Filter:

    @staticmethod
    def filter(data_raw: dict, sigma: int=1, verbose=False) -> dict:
        if verbose: print("band filter")
        data = Filter.__band_filter(data_raw, lowFreq=2, highFreq=70, filterType='bandstop')
        if verbose: print("laplacian filter")
        data = Filter.__laplacian_filter(data, sigma) #Need to write test for this once its complete
        return data

    @staticmethod
    def __band_filter(
            data,
            lowFreq: Union[int, float],
            highFreq: Union[int, float],
            samplingFreq: int = 240,
            order: int = 5,
            filterType: str = 'bandpass',
    ):
        filtered_channels = []
        for example in data["Signal"]:
            examples = []
            for j in range(len(example)):
                filtered_channel = Filter.__band_filter_sample(
                    channel=example[j],
                    lowFreq=lowFreq,
                    highFreq=highFreq,
                    samplingFreq=samplingFreq,
                    order=order,
                    filterType=filterType
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
            samplingFreq: int=240,
            order: int=5,
            filterType: str='bandpass'
    ):
        nyq = 0.5 * samplingFreq
        low = lowFreq / nyq
        high = highFreq / nyq
        b, a = signal.butter(order, [low, high], btype=filterType)
        y = signal.lfilter(b, a, channel)

        return y

    @staticmethod
    def __laplacian_filter(data, sigma):
        for i in range(len(data["Signal"])):
            example = data["Signal"][i]
            transposed = np.transpose(example)
            new_time_steps = []
            for trans in transposed:
                new_time_step = Filter.__laplacian_filter_sample(trans, sigma)
                new_time_steps.append(new_time_step)
            transposed_back = np.transpose(new_time_steps)
            data["Signal"][i] = transposed_back
        return data

    @staticmethod
    # Enhance the difference between two channels.
    def __laplacian_filter_sample(time_step, sigma):

        matrix = np.zeros((13, 12))

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

        matrix = gl(matrix, sigma, output=None, mode='reflect', cval=0.0)

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