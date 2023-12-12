python ex_5_1.py "C:\\Users\\karun\\OneDrive\\Desktop\\exercise-set-5-kupadhya-ctrl\\src"

import argparse
import os
from subprocess import check_output

try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

def main(infile):
    """Call line_count with the infile argument."""
    if os.path.isdir(infile):
        # If the input is a directory, list files and call line_count for each file
        for root, dirs, files in os.walk(infile):
            for file in files:
                file_path = os.path.join(root, file)
                line_count(file_path)
    else:
        # If the input is a file, call line_count directly
        line_count(infile)

if __name__ == "__main__":
    # Create an argument parser object
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")

    # Add a positional argument for the input file or directory
    parser.add_argument("infile", help="The input file or directory to count lines from.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the infile argument
    main(args.infile)
