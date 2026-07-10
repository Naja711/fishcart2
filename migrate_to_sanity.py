import os
import json
import requests
import uuid

PROJECT_ID = 'v5b89tvp'
DATASET = 'production'
TOKEN = os.environ.get('SANITY_API_TOKEN')
API_URL = f'https://{PROJECT_ID}.api.sanity.io/v2021-10-21/data/mutate/{DATASET}'

if not TOKEN:
    print('ERROR: Please set the SANITY_API_TOKEN environment variable.')
    exit(1)

# Import the data from build_spa_details.py
import sys
sys.path.append(os.getcwd())
try:
    from build_spa_details import data as products_data
except ImportError:
    print('Could not import products_data from build_spa_details.py')
    exit(1)

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {TOKEN}'
}

mutations = []

for prod_id, prod_data in products_data.items():
    doc = {
        '_type': 'product',
        '_id': prod_id, # Optional custom ID
        'id': prod_id,
        'title': prod_data.get('title', ''),
        'subtitle': prod_data.get('subtitle', ''),
        'price': prod_data.get('price', ''),
        'unit': prod_data.get('unit', ''),
        'origin_label': prod_data.get('origin_label', ''),
        'origin': prod_data.get('origin', ''),
        'best_for': prod_data.get('best_for', ''),
        'nutrition_protein': prod_data.get('nutrition_protein', ''),
        'nutrition_fat': prod_data.get('nutrition_fat', ''),
        'nutrition_calories': prod_data.get('nutrition_calories', ''),
        'nutrition_extra_label': prod_data.get('nutrition_extra_label', ''),
        'nutrition_extra_val': prod_data.get('nutrition_extra_val', ''),
        'speciality': prod_data.get('speciality', ''),
        'famous_for': prod_data.get('famous_for', ''),
        'allergy': prod_data.get('allergy', ''),
        'how_to_cook': prod_data.get('how_to_cook', ''),
        'video1': prod_data.get('video1', ''),
        'video2': prod_data.get('video2', ''),
        'instructions': prod_data.get('instructions', ''),
        # Ignoring image for now, as images require uploading the asset first and linking it.
    }
    
    mutations.append({
        'createOrReplace': doc
    })

# Batch upload
payload = {
    'mutations': mutations
}

response = requests.post(API_URL, headers=headers, json=payload)
if response.status_code == 200:
    print('Successfully migrated products to Sanity!')
else:
    print(f'Failed to migrate: {response.status_code}')
    print(response.text)
