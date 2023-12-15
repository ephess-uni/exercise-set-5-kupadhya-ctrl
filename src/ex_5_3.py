import numpy as np
import pandas as pd
from argparse import ArgumentParser
import os

def process_data(infile, outfile):
    # Read the data from the input file using pandas
    data = pd.read_csv(infile)

    # Perform the standard scale transform
    scaled_data = (data - data.mean()) / data.std()

    # Write the scaled data to the output file
    scaled_data.to_csv(outfile, index=False)

if __name__ == "__main__":
    # Create an argument parser object
    parser = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")

    # Add positional arguments for the input and output files
    parser.add_argument("infile", help="The input filename for the data file to be processed.")
    parser.add_argument("outfile", help="The output filename for the processed data.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the process_data function with the infile and outfile arguments
    process_data(args.infile, args.outfile)

