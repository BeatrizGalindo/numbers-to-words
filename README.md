# Numbers to Words Converter
## Overview
The Numbers to Words Converter is a Python project that converts a given number (ranging from 0 to 100,000) into its English word representation. This project is organized into different modules for ease of maintenance and testing.

## Project Structure
The project is structured as follows:

```
├── README.md               # Project overview and documentation
├── bin
│   └── numbers-to-words    # Main executable script for the converter
├── requirements.txt        # Python dependencies for the project
├── src
│   ├── __init__.py         # Initializes the 'src' module
│   ├── __pycache__         # Directory containing compiled Python files
│   │   ├── __init__.cpython-313.pyc
│   │   └── convert.cpython-313.pyc
│   └── convert.py          # Core conversion logic from numbers to words
└── tests
    ├── __pycache__         # Directory containing compiled Python test files
    │   └── test_convert.cpython-313-pytest-8.3.3.pyc
    └── test_convert.py      # Unit tests for the conversion logic

```


## Requirements
- Python 3.13+

## Usage
The `numbers-to-words` script is located in the bin directory and can be run from the command line. 
To convert a number to words, run the script as follows:

```
./bin/numbers-to-words [number]
```

#### Example input:

```
./bin/numbers-to-words 12345
```
#### Example output:

```
twelve thousand three hundred forty-five
```
## Exit Codes: 
`0`: Successful execution.

`1`: Invalid input (e.g., non-integer input or numbers out of the supported range).

## How it works
The `src/convert.py` module contains the core logic for converting numbers into words.
The `bin/numbers-to-words` script handles input validation, error handling, and output, making use of sys.stdin, sys.stdout, and sys.stderr for standard input/output operations.
The `tests/test_convert.py` file includes unit tests to ensure the conversion logic works as expected.

## Running tests
To run the tests, ensure you have `pytest` installed and run the following command:
```
pytest tests/test_convert.py
```

