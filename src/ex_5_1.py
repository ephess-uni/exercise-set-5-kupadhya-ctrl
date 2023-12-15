import os
import subprocess

MODULE_PATH = "src/ex_5_1.py"


def test_ex_5_1_has_description(capfd):
    subprocess.run(['python', MODULE_PATH, '-h'], check=True)
    out_fd, _ = capfd.readouterr()
    assert "This program prints the number of lines in infile." in out_fd

def test_ex_5_1_prints_correct_line_count(capfd):
    infile_fixture = os.path.join(os.path.dirname(__file__), "fixtures", "ex_5_0_fixture.txt")
    subprocess.run(['python', MODULE_PATH, infile_fixture], check=True)
    out, _ = capfd.readouterr()
    assert out == "6\n"  # Adjust the expected line count as per your actual file

