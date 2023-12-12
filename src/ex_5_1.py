"""ex_5_1.py"""
python ex_5_1.py C:\Users\karun\OneDrive\Desktop\exercise-set-5-kupadhya-ctrl\src
import argparse
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
   # Create an argument parser object
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")

    # Add a positional argument for the input file
    parser.add_argument("infile", help="The input file to count lines from.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the infile argument
    main(args.infile)
