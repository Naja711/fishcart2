#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Generate the static HTML pages from Sanity data
python generate_details_pages.py
python build_spa_details.py
python update_links.py
python generate_recipes.py
