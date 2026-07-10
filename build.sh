#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Generate the static HTML pages from Sanity data
python generate_details_pages.py
python build_spa_details.py
python update_links.py