
import numpy as np
from scipy.signal import hilbert as hilbert_analytic
from scipy.fftpack import hilbert as hilbert

"""
Phase difference between channels.
"""
class Phase:

    """
    ***** INPUT 1 *****
    2-dm = chunks.
    3-dm = sensors
    4-dm = array of values in the chunk
    """
    @staticmethod
    def apply(data):
        phases_examples = []
        for i in range(len(data)):
            phases_chunks = Phase.__phase_chunks(data[i])
            phases_examples.append(phases_chunks)
        return phases_examples

    """
    Calculate Phase for chunks. 
    """
    @staticmethod
    def __phase_chunks(chunk):
        phases_chunks = []
        for i in range(len(chunk)):
            phase_channels = Phase.__phase_channels(chunk[i])
            phases_chunks.append(phase_channels)
        return phases_chunks

    """
    Calculate Phase for channels.
    """
    @staticmethod
    def __phase_channels(channels):
        length = len(channels)
        in_range = range(length)
        phase_channels = []
        for i in in_range:
            channel_i_phases = []
            for j in in_range:
                phase = Phase.__phase(channels[i], channels[j])
                channel_i_phases.append(phase)
            phase_channels.append(channel_i_phases)
        return phase_channels

    """
    Calculate Phase for two channels.  
    """
    @staticmethod
    def __phase(channel1, channel2):
        hill1 = hilbert_analytic(channel1)
        hill2 = hilbert_analytic(channel2)
        inner_1_con2 = np.inner(hill1, np.conj(hill2))
        inner_1_con1 = np.inner(hill1, np.conj(hill1))
        inner_2_con2 = np.inner(hill2, np.conj(hill2))
        pdt = inner_1_con2 / np.sqrt(inner_1_con1 * inner_2_con2)
        phase = np.angle(pdt)
        return phase
