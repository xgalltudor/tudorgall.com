import subprocess


def run_tests():
    # Run pytest on the test_suites directory with verbosity level 2
    subprocess.run(['pytest', '-vv', './test_suites'])


if __name__ == '__main__':
    run_tests()