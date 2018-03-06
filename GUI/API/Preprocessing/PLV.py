
import numpy as np
from scipy.signal import hilbert as hilbert_analytic
from scipy.fftpack import hilbert as hilbert

"""
Phase Lock Value.
"""
class PLV:

    """
    ***** INPUT 1 *****
    2-dm = chunks.
    3-dm = sensors
    4-dm = array of values in the chunk
    """
    @staticmethod
    def apply(data):
        plvs_examples = []
        for i in range(len(data)):
            plvs_chunks = PLV.__plv_chunks(data[i])
            plvs_examples.append(plvs_chunks)
        return plvs_examples

    """
    Calculate PLV for chunks. 
    """
    @staticmethod
    def __plv_chunks(chunk):
        plvs_chunks = []
        for i in range(len(chunk)):
            plv_channels = PLV.__plv_channels(chunk[i])
            plvs_chunks.append(plv_channels)
        return plvs_chunks

    """
    Calculate PLV for channels.
    """
    @staticmethod
    def __plv_channels(channels):
        length = len(channels)
        in_range = range(length)
        plv_channels = []
        for i in in_range:
            channel_i_phases = []
            for j in in_range:
                phase = PLV.__plv(channels[i], channels[j])
                channel_i_phases.append(phase)
            plv_channels.append(channel_i_phases)
        return plv_channels

    """
    Calculate PLV for two channels.  
    """
    @staticmethod
    def __plv(channel1, channel2):
        sig1_hill = hilbert_analytic(channel1)
        sig2_hill = hilbert_analytic(channel2)
        ip_1_con2 = np.inner(sig1_hill, np.conj(sig2_hill))
        ip_1_con1 = np.inner(sig1_hill, np.conj(sig1_hill))
        ip_2_con2 = np.inner(sig2_hill, np.conj(sig2_hill))
        pdt = ip_1_con2 / np.sqrt(ip_1_con1 * ip_2_con2)
        phase = np.angle(pdt)
        a = np.exp(np.complex(0, 1) * phase)
        plv = np.abs(a)
        return plv
