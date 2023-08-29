import pytest

if __name__ == "__main__":
    # -v is for verbosity
    # --html=report.html generates an HTML report
    # ./test_suites specifies the directory where the test files are located
    pytest.main(["-v", "--html=report.html", "./test_suites"])