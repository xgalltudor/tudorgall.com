import subprocess
import os


def run_tests():
    # Get the directory where the script resides
    script_dir = os.path.dirname(__file__)

    # Create the full path to the test_suites directory
    test_suites_dir = os.path.join(script_dir, 'test_suites')

    # Run pytest on the test_suites directory with verbosity level 2
    subprocess.run(['pytest', '-vv', test_suites_dir])


if __name__ == '__main__':
    run_tests()
