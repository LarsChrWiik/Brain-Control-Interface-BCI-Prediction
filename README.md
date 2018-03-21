# CE903-group6

## Purpose

The main purpose of this study is to perform a binary classification of **P300 occurrence** based upon _prior_ _signals_.
The two classifications available are: P300 will occur, P300 will not occur.
By using a portion of a P300 signal before its occurrence, it could be possible for a classifier to interpret a pattern which might be transferable between subjects.
If this pattern exists it could open up a new avenue of investigation and research about how we look at the P300 wave.

### Raw Signal Data

This graph shows unprocessed signal data for a single example 

![logo](./Raw_data.jpg?raw=true)

### Filtered Data

This graph shows the signal data after undergoing bandpass and Laplacian filtering for a single example.

![logo](./Filtered.jpg?raw=true)

### Chunked Data

This graph shows a single window of 300 milliseconds after the occurance of a flashing signal.

![logo](./Chunked.jpg?raw=true)

## Results

The highest average accuracy on a balanced training set using cross validation was achieved using KNN.
The picture below shows the results obtained using that classifier.

![logo](./KNN.JPG?raw=true)
     


## Future work

Future work includes conducting a study to test if the system is transferable between two separate subjects.
One example would be to train a classifier on one participant and predict P300 occurrences using brain waves from another participant.
This could be further extended by training a system on a much larger sample group. 

Future works also includes extending the current implementation to participate in BCI competitions, as the system currently doesn’t predict the type of P300, just that it will occur.
The standard approach uses an assumption of a gaussian distribution around 300 ms after a flashing signal, this window containing the given data is then used for a prediction.
As opposed to the previously mentioned method, this study attempts to predict the P300 signal using data from the flashing signal to 300 milliseconds after its occurrence.
The end goal was to evaluate the classification accuracy by using the previously mentioned interval, additional adaptation would be required to make it applicable for a BCI competition.
If these modification were made the system could be tested against the results of the BCI competition as a way of validating the system performance. 
