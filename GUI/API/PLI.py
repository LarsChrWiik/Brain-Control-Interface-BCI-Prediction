
import numpy as np
from scipy.signal import hilbert as hilbert_analytic
from scipy.fftpack import hilbert as hilbert

"""
Phase Lag Index.
"""
class PLI:

    """
    ***** INPUT 1 *****
    2-dm = chunks.
    3-dm = sensors
    4-dm = array of values in the chunk
    """
    @staticmethod
    def apply(data):
        plis_examples = []
        for i in range(len(data)):
            plis_chunks = PLI.__pli_chunks(data[i])
            plis_examples.append(plis_chunks)
        return plis_examples

    """
    Calculate PLI for chunks. 
    """
    @staticmethod
    def __pli_chunks(chunk):
        plis_chunks = []
        for i in range(len(chunk)):
            pli_channels = PLI.__pli_channels(chunk[i])
            plis_chunks.append(pli_channels)
        return plis_chunks

    """
    Calculate PLI for channels.
    """
    @staticmethod
    def __pli_channels(channels):
        length = len(channels)
        in_range = range(length)
        pli_channels = []
        for i in in_range:
            channel_i_phases = []
            for j in in_range:
                phase = PLI.__pli(channels[i], channels[j])
                channel_i_phases.append(phase)
            pli_channels.append(channel_i_phases)
        return pli_channels

    """
    Calculate PLI for two channels.
    """
    @staticmethod
    def __pli(channel1, channel2):
        sig1_hill = hilbert_analytic(channel1)
        sig2_hill = hilbert_analytic(channel2)
        ip_1_con2 = np.inner(sig1_hill, np.conj(sig2_hill))
        ip_1_con1 = np.inner(sig1_hill, np.conj(sig1_hill))
        ip_2_con2 = np.inner(sig2_hill, np.conj(sig2_hill))
        pdt = ip_1_con2 / np.sqrt(ip_1_con1 * ip_2_con2)
        phase = np.angle(pdt)
        sign_func = np.sign(phase)
        return sign_func
