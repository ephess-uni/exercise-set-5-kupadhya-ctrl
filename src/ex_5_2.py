""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Complete the data processing steps using numpy here.

    # Save the output to OUTFILE using numpy routines.
     # Load data from the input file
    data = np.loadtxt(INFILE, delimiter=',')

    # Modify the data to have a mean of 0
    data_mean_zero = data - np.mean(data, axis=0)

    # Modify the zero mean data to have a standard deviation of 1
    data_processed = data_mean_zero / np.std(data_mean_zero, axis=0)

    # Save the processed data to OUTFILE using numpy routines
    np.savetxt(OUTFILE, data_processed, delimiter=',')
