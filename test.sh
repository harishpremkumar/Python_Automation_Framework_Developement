#!/bin/bash

echo "Installing Python Packages"
pip install -r requirements.txt

# Run pytest command on all tests in the current directory or specific directory
echo "Running pytest tests..."

# Run pytest (you can specify a directory or file, e.g., "tests/")
pytest

# Exit with the same code as pytest (0 for success, 1 for failure)
exit $?
