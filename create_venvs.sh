#!/bin/bash

set -e

# Create venv_a and install requirements
python3 -m venv venv_a
(
	source venv_a/bin/activate
	pip install --upgrade pip
	pip install -r requirements_a.txt
)

# Create venv_b and install requirements
python3 -m venv venv_b
(
	source venv_b/bin/activate
	pip install --upgrade pip
	pip install -r requirements_b.txt
)

echo "Virtual environments venv_a and venv_b created and requirements installed."