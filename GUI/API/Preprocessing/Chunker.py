
"""
Contain function to divide signals into chunks
with corresponding targets.

Works for both labelled and non-labelled data.

***** FIRST OUTPUT (X) *****
1-dm = examples
2-dm = chunks = 156.
3-dm = sensors = 64
4-dm = array of values in the chunk = 1250

**** SECOND OUTPUT (Y) *****
1-dm = examples
2-dm = chunks = 156.
"""
class Chunker:

    # Define chunk size.
    sampling_rate = 240
    ms = 1000
    p300_time = 300
    timestep_ms_ratio = ms / sampling_rate
    chunk_size = int(p300_time * timestep_ms_ratio)

    @staticmethod
    def chunk(data: dict, with_targets):
        if (with_targets):
            return Chunker.chunk_train(data)
        return Chunker.chunk_test(data)

    # Chunk for train input.
    @staticmethod
    def chunk_train(data: dict):
        return Chunker.__chunk(data)

    # Chunk for test input.
    @staticmethod
    def chunk_test(data: dict):
        return Chunker.__chunk(data)


    """
    Chunk input examples. 
    Try-except is needed due to difference in 
    training and test dictionary. (StimulusType does not exist in test)
    """
    @staticmethod
    def __chunk(data: dict):
        flashing_raw = data["Flashing"]
        signal_raw = data["Signal"]
        stimulus_raw = []
        try:
            stimulus_raw = data["StimulusType"]
        except:
            pass

        # Chunking all input examples.
        examples_all = []
        stimulus_all = []
        for i in range(len(flashing_raw)):
            stimulus_example = None
            try:
                stimulus_example = stimulus_raw[i]
            except:
                pass
            chunks, stimulus = Chunker.__generate_chunks(
                signal_raw[i],
                flashing_raw[i],
                Chunker.chunk_size,
                stimulus_example
            )
            examples_all.append(chunks)
            stimulus_all.append(stimulus)

        return examples_all, stimulus_all

    # Chunking single input example.
    @staticmethod
    def __generate_chunks(signal, flashing, chunk_size, stimulus_raw):
        # Get the first flash.
        # 0 = no previous flash.
        old_flash = 0
        chunks = []
        stimulus_all = []
        length = len(flashing)
        for i in range(len(flashing)):
            flash = flashing[i]

            # Only record after a flashing signal occurs.
            if old_flash == 0 and flash == 1 and i + chunk_size < length:
                try:
                    stimulus_all.append(stimulus_raw[i])
                except:
                    pass

                chunk_sensor = Chunker.__chunk_sensor(
                    signal,
                    i,
                    chunk_size
                )
                chunks.append(chunk_sensor)

            # Update the old flash.
            old_flash = flash

        return chunks, stimulus_all

    # Chunking each sensor.
    @staticmethod
    def __chunk_sensor(signal, ts_index, chunk_size):
        chunk_sensor = []
        for i in range(len(signal)):
            # Slice a chunk after a flashing occurs.
            chunk = signal[i][ts_index:ts_index + chunk_size]
            chunk_sensor.append(chunk)
        return chunk_sensor
