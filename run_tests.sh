#!/usr/bin/env bash

# Stop script if any command fails
set -e

# Activate virtual environment
source .venv/Scripts/activate

# Run tests
pytest
