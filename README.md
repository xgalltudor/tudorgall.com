# Test Automation for www.tudorgall.com

This repository contains automated test scripts for [www.tudorgall.com](http://www.tudorgall.com). The tests are divided into two frameworks: Selenium (using Python and Pytest) and Robot Framework.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
   - [Selenium Tests](#selenium-tests)
   - [Robot Framework Tests](#robot-framework-tests)
3. [Running the Tests](#running-the-tests)
   - [Selenium Tests](#running-selenium-tests)
   - [Robot Framework Tests](#running-robot-framework-tests)
4. [Contact Information](#contact-information)

## Prerequisites

- Python 3.8+
- Pip
- ChromeDriver

## Installation

Clone this repository and navigate into the project folder.

### Selenium Tests

For Selenium tests, run the following command:

```bash
pip install -r SeleniumTests/requirements.txt
```

### Robot Framework Tests

For Robot Framework tests, run:

```bash
pip install -r RobotFrameworkTests/requirements.txt
```

## Running the Tests

### Running Selenium Tests

To run the Selenium tests, execute the following command from the root directory:

```bash
python ./SeleniumTests/run.py
```

### Running Robot Framework Tests

To run the Robot Framework tests, execute the following command from the root directory:

```bash
robot ./RobotFrameworkTests/Tests/*.robot
```

## Contact Information

For any queries, please contact Tudor Gall at xgalltudor@yahoo.com.
