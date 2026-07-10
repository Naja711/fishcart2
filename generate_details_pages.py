import os

data = {
    # FISH
    "prod_1_salmon": {
        "title": "Salmon", "subtitle": "Norway • Fillet", "price": "£14.99", "unit": "kg", "image": "prod_1_salmon.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From",
        "origin": "Norway, North Atlantic Ocean. Wild Caught.", "best_for": "Curry, Grill, Baking.",
        "nutrition_protein": "20.4g", "nutrition_fat": "13.4g", "nutrition_calories": "208 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "3", "speciality": "Rich, buttery flavor and firm texture.",
        "famous_for": "Norwegian Cuisine, Japanese Sushi.", "allergy": "Contains Fish.",
        "how_to_cook": "Grill or pan-sear. Great with lemon and herbs.",
        "video1": "https://www.youtube.com/embed/jH-1gV1fH-s", "video2": "https://www.youtube.com/embed/9gN2lB5B9Qo",
        "instructions": "<li>Preheat pan on medium-high.</li><li>Season salmon with salt and pepper.</li><li>Sear skin-side down for 4 mins.</li><li>Flip and cook 2 mins.</li>"
    },
    "prod_2_seabass": {
        "title": "Sea Bass", "subtitle": "Local • Whole", "price": "£18.50", "unit": "kg", "image": "prod_2_seabass.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "Mediterranean Sea.", "best_for": "Baking, Pan-frying.",
        "nutrition_protein": "18g", "nutrition_fat": "2.5g", "nutrition_calories": "97 kcal",
        "nutrition_extra_label": "B-Vitamins", "nutrition_extra_val": "High", "speciality": "Mild, delicate flavor.",
        "famous_for": "Mediterranean dishes.", "allergy": "Contains Fish.", "how_to_cook": "Bake whole with lemon and rosemary.",
        "video1": "", "video2": "", "instructions": "<li>Stuff with lemon.</li><li>Bake at 200C for 20 mins.</li>"
    },
    "prod_3_tuna": {
        "title": "Tuna Steak", "subtitle": "Pacific • Steak", "price": "£22.00", "unit": "kg", "image": "prod_3_tuna.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "Pacific Ocean.", "best_for": "Searing, Sashimi.",
        "nutrition_protein": "24g", "nutrition_fat": "1g", "nutrition_calories": "109 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "Mod", "speciality": "Meaty texture.",
        "famous_for": "Sushi, Poke Bowls.", "allergy": "Contains Fish.", "how_to_cook": "Sear 1 min per side.",
        "video1": "", "video2": "", "instructions": "<li>Season well.</li><li>Sear on screaming hot pan for 1 min per side.</li>"
    },
    "prod_4_cod": {
        "title": "Cod Fillet", "subtitle": "Atlantic • Fillet", "price": "£12.99", "unit": "kg", "image": "prod_4_cod.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "North Atlantic.", "best_for": "Fish & Chips, Baking.",
        "nutrition_protein": "17g", "nutrition_fat": "0.7g", "nutrition_calories": "82 kcal",
        "nutrition_extra_label": "Protein", "nutrition_extra_val": "High", "speciality": "Flaky white meat.",
        "famous_for": "British Fish & Chips.", "allergy": "Contains Fish.", "how_to_cook": "Batter and fry or bake.",
        "video1": "", "video2": "", "instructions": "<li>Batter lightly.</li><li>Deep fry until golden.</li>"
    },
    "prod_5_mackerel": {
        "title": "Mackerel", "subtitle": "Local • Whole", "price": "£9.50", "unit": "kg", "image": "prod_5_mackerel.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "UK Coast.", "best_for": "Grilling, Smoking.",
        "nutrition_protein": "18g", "nutrition_fat": "13g", "nutrition_calories": "205 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "High", "speciality": "Rich, oily fish.",
        "famous_for": "Smoked dishes.", "allergy": "Contains Fish.", "how_to_cook": "Grill on high heat.",
        "video1": "", "video2": "", "instructions": "<li>Score skin.</li><li>Grill for 5 mins each side.</li>"
    },
    "prod_6_haddock": {
        "title": "Haddock", "subtitle": "Atlantic • Fillet", "price": "£14.00", "unit": "kg", "image": "prod_6_haddock.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "North Atlantic.", "best_for": "Baking, Smoking.",
        "nutrition_protein": "19g", "nutrition_fat": "0.5g", "nutrition_calories": "90 kcal",
        "nutrition_extra_label": "B12", "nutrition_extra_val": "High", "speciality": "Slightly sweet taste.",
        "famous_for": "Scottish Cuisine.", "allergy": "Contains Fish.", "how_to_cook": "Poach in milk or bake.",
        "video1": "", "video2": "", "instructions": "<li>Bake with butter and herbs.</li>"
    },
    "prod_7_sardines": {
        "title": "Sardines", "subtitle": "Local • Fresh", "price": "£8.50", "unit": "kg", "image": "prod_7_sardines.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "Cornwall Coast.", "best_for": "Grilling, BBQ.",
        "nutrition_protein": "20g", "nutrition_fat": "11g", "nutrition_calories": "190 kcal",
        "nutrition_extra_label": "Calcium", "nutrition_extra_val": "High", "speciality": "Nutrient dense.",
        "famous_for": "Mediterranean BBQ.", "allergy": "Contains Fish.", "how_to_cook": "Grill whole.",
        "video1": "", "video2": "", "instructions": "<li>Grill whole with olive oil and salt.</li>"
    },
    "prod_8_trout": {
        "title": "Trout", "subtitle": "Farm • Whole", "price": "£11.99", "unit": "kg", "image": "prod_8_trout.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "UK Freshwater Farms.", "best_for": "Pan-frying, Baking.",
        "nutrition_protein": "19g", "nutrition_fat": "6g", "nutrition_calories": "140 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "Mod", "speciality": "Earthy flavor.",
        "famous_for": "European Freshwater Cuisine.", "allergy": "Contains Fish.", "how_to_cook": "Pan-fry with almonds.",
        "video1": "", "video2": "", "instructions": "<li>Pan fry with butter and almonds.</li>"
    },

    # MEAT
    "beef_chunks": {
        "title": "Beef Chunks", "subtitle": "Premium • Boneless", "price": "£10.99", "unit": "kg", "image": "beef_chunks.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Stews, Curries.",
        "nutrition_protein": "26g", "nutrition_fat": "15g", "nutrition_calories": "250 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "High", "speciality": "Tender and flavorful.",
        "famous_for": "Slow-cooked stews.", "allergy": "No known allergens.", "how_to_cook": "Slow cook for 3 hours.",
        "video1": "", "video2": "", "instructions": "<li>Brown meat.</li><li>Slow cook in broth.</li>"
    },
    "boar_meat_bonless": {
        "title": "Boar Meat", "subtitle": "Exotic • Boneless", "price": "£18.50", "unit": "kg", "image": "boar_meat_bonless.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Wild Sourced.", "best_for": "Roasting, Stews.",
        "nutrition_protein": "28g", "nutrition_fat": "9g", "nutrition_calories": "210 kcal",
        "nutrition_extra_label": "Protein", "nutrition_extra_val": "High", "speciality": "Rich, gamey flavor.",
        "famous_for": "Exotic dishes.", "allergy": "No known allergens.", "how_to_cook": "Roast slowly.",
        "video1": "", "video2": "", "instructions": "<li>Marinate overnight.</li><li>Roast slow.</li>"
    },
    "boar_meat_with_bone": {
        "title": "Boar Bone-in", "subtitle": "Exotic • Bone-in", "price": "£15.50", "unit": "kg", "image": "boar_meat_with_bone.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Wild Sourced.", "best_for": "Broths, Slow Cook.",
        "nutrition_protein": "25g", "nutrition_fat": "11g", "nutrition_calories": "220 kcal",
        "nutrition_extra_label": "Flavor", "nutrition_extra_val": "High", "speciality": "Flavorful bone marrow.",
        "famous_for": "Rich broths.", "allergy": "No known allergens.", "how_to_cook": "Simmer for hours.",
        "video1": "", "video2": "", "instructions": "<li>Simmer for rich broth.</li>"
    },
    "buffalo": {
        "title": "Buffalo Meat", "subtitle": "Premium • Cuts", "price": "£9.50", "unit": "kg", "image": "buffalo.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Farmed.", "best_for": "Curries.",
        "nutrition_protein": "24g", "nutrition_fat": "8g", "nutrition_calories": "190 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "High", "speciality": "Leaner than beef.",
        "famous_for": "Spicy curries.", "allergy": "No known allergens.", "how_to_cook": "Pressure cook.",
        "video1": "", "video2": "", "instructions": "<li>Pressure cook for tenderness.</li>"
    },
    "deer_meat": {
        "title": "Venison", "subtitle": "Exotic • Cuts", "price": "£22.99", "unit": "kg", "image": "deer_meat.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Wild Sourced.", "best_for": "Steaks, Roasts.",
        "nutrition_protein": "30g", "nutrition_fat": "3g", "nutrition_calories": "150 kcal",
        "nutrition_extra_label": "Lean", "nutrition_extra_val": "Very High", "speciality": "Extremely lean, gamey.",
        "famous_for": "Gourmet dishes.", "allergy": "No known allergens.", "how_to_cook": "Sear quickly.",
        "video1": "", "video2": "", "instructions": "<li>Do not overcook. Sear quickly.</li>"
    },
    "lamb": {
        "title": "Lamb Meat", "subtitle": "Local • Mixed", "price": "£15.99", "unit": "kg", "image": "lamb.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Roasting, Grilling.",
        "nutrition_protein": "25g", "nutrition_fat": "21g", "nutrition_calories": "290 kcal",
        "nutrition_extra_label": "Fat", "nutrition_extra_val": "High", "speciality": "Tender and sweet.",
        "famous_for": "Sunday Roasts.", "allergy": "No known allergens.", "how_to_cook": "Roast with rosemary.",
        "video1": "", "video2": "", "instructions": "<li>Roast with garlic and rosemary.</li>"
    },
    "mutton_leg": {
        "title": "Mutton Leg", "subtitle": "Local • Bone-in", "price": "£14.99", "unit": "kg", "image": "mutton_leg.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Slow Roasting.",
        "nutrition_protein": "26g", "nutrition_fat": "18g", "nutrition_calories": "270 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "Mod", "speciality": "Rich, intense flavor.",
        "famous_for": "Traditional Roasts.", "allergy": "No known allergens.", "how_to_cook": "Slow roast.",
        "video1": "", "video2": "", "instructions": "<li>Slow roast for 4 hours.</li>"
    },
    "rabbit": {
        "title": "Rabbit Meat", "subtitle": "Farm • Whole", "price": "£12.50", "unit": "kg", "image": "rabbit.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Stews, Braising.",
        "nutrition_protein": "28g", "nutrition_fat": "5g", "nutrition_calories": "160 kcal",
        "nutrition_extra_label": "Lean", "nutrition_extra_val": "High", "speciality": "Very lean white meat.",
        "famous_for": "French Cuisine.", "allergy": "No known allergens.", "how_to_cook": "Braise slowly.",
        "video1": "", "video2": "", "instructions": "<li>Braise in white wine.</li>"
    },

    # CHICKEN
    "chicken_full": {
        "title": "Whole Chicken", "subtitle": "Local Farm • Fresh", "price": "£5.99", "unit": "kg", "image": "chicken_full.jpg",
        "category": "Chicken", "category_url": "index.html#chicken", "origin_label": "Source", "origin": "UK Free Range Farms.", "best_for": "Roasting.",
        "nutrition_protein": "27g", "nutrition_fat": "14g", "nutrition_calories": "239 kcal",
        "nutrition_extra_label": "Protein", "nutrition_extra_val": "High", "speciality": "Juicy and tender.",
        "famous_for": "Sunday Roasts.", "allergy": "No known allergens.", "how_to_cook": "Roast whole.",
        "video1": "", "video2": "", "instructions": "<li>Roast at 190C for 1h 20m.</li>"
    },
    "boneless_chicken": {
        "title": "Boneless Chicken", "subtitle": "Premium Cuts", "price": "£8.50", "unit": "kg", "image": "boneless_chicken.jpg",
        "category": "Chicken", "category_url": "index.html#chicken", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Curries, Stir-fry.",
        "nutrition_protein": "31g", "nutrition_fat": "3g", "nutrition_calories": "165 kcal",
        "nutrition_extra_label": "Lean", "nutrition_extra_val": "High", "speciality": "Very lean and versatile.",
        "famous_for": "Quick meals.", "allergy": "No known allergens.", "how_to_cook": "Pan fry or boil.",
        "video1": "", "video2": "", "instructions": "<li>Pan fry for 10-15 mins.</li>"
    },
    "chicken_liver": {
        "title": "Chicken Liver", "subtitle": "Fresh Offal", "price": "£3.99", "unit": "kg", "image": "chicken_liver.jpg",
        "category": "Chicken", "category_url": "index.html#chicken", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Pâté, Sauté.",
        "nutrition_protein": "24g", "nutrition_fat": "6g", "nutrition_calories": "167 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "Very High", "speciality": "Rich in iron and vitamins.",
        "famous_for": "Pâté.", "allergy": "No known allergens.", "how_to_cook": "Sauté quickly.",
        "video1": "", "video2": "", "instructions": "<li>Sauté with onions until brown.</li>"
    },

    # EGGS
    "chicken_egg": {
        "title": "Chicken Eggs", "subtitle": "Farm Fresh • Dozen", "price": "£2.99", "unit": "dozen", "image": "chicken_egg.jpg",
        "category": "Eggs", "category_url": "index.html#eggs", "origin_label": "Source", "origin": "UK Free Range.", "best_for": "Boiling, Frying, Baking.",
        "nutrition_protein": "12g", "nutrition_fat": "10g", "nutrition_calories": "143 kcal",
        "nutrition_extra_label": "Vitamins", "nutrition_extra_val": "High", "speciality": "Daily essential.",
        "famous_for": "Breakfasts.", "allergy": "Contains Egg.", "how_to_cook": "Boil for 6 mins.",
        "video1": "", "video2": "", "instructions": "<li>Boil, fry, or scramble.</li>"
    },
    "duck_egg": {
        "title": "Duck Eggs", "subtitle": "Premium • Dozen", "price": "£4.50", "unit": "dozen", "image": "duck_egg.jpg",
        "category": "Eggs", "category_url": "index.html#eggs", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Baking, Custards.",
        "nutrition_protein": "13g", "nutrition_fat": "14g", "nutrition_calories": "185 kcal",
        "nutrition_extra_label": "Richness", "nutrition_extra_val": "High", "speciality": "Larger yolks, creamier.",
        "famous_for": "Baking fluffier cakes.", "allergy": "Contains Egg.", "how_to_cook": "Fry sunny side up.",
        "video1": "", "video2": "", "instructions": "<li>Fry on medium heat until white is set.</li>"
    },
    "quail_egg": {
        "title": "Quail Eggs", "subtitle": "Exotic • Pack", "price": "£3.99", "unit": "pack", "image": "quail_egg.jpg",
        "category": "Eggs", "category_url": "index.html#eggs", "origin_label": "Source", "origin": "Specialty Farms.", "best_for": "Salads, Garnishes.",
        "nutrition_protein": "13g", "nutrition_fat": "11g", "nutrition_calories": "158 kcal",
        "nutrition_extra_label": "Vitamins", "nutrition_extra_val": "High", "speciality": "Small, speckled, nutrient dense.",
        "famous_for": "Gourmet dishes.", "allergy": "Contains Egg.", "how_to_cook": "Boil for 2.5 mins.",
        "video1": "", "video2": "", "instructions": "<li>Boil for 2.5 mins for soft boiled.</li>"
    }
}

template_path = r"d:\fishcart\product_template.html"
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

# Update sidebar links in template to work with SPA
template = template.replace('href="index.html"', 'href="index.html"')
template = template.replace('href="fish.html"', 'href="index.html#fish"')
template = template.replace('href="meat.html"', 'href="index.html#meat"')
template = template.replace('href="chicken.html"', 'href="index.html#chicken"')
template = template.replace('href="eggs.html"', 'href="index.html#eggs"')

for id, p in data.items():
    html = template
    html = html.replace("{{TITLE}}", p["title"])
    html = html.replace("{{SUBTITLE}}", p["subtitle"])
    html = html.replace("{{PRICE}}", p["price"])
    html = html.replace("{{UNIT}}", p["unit"])
    html = html.replace("{{IMAGE}}", "assets/" + p["image"])
    html = html.replace("{{CATEGORY}}", p["category"])
    html = html.replace("{{CATEGORY_URL}}", p["category_url"])
    html = html.replace("{{ORIGIN_LABEL}}", p["origin_label"])
    html = html.replace("{{ORIGIN}}", p["origin"])
    html = html.replace("{{BEST_FOR}}", p["best_for"])
    html = html.replace("{{NUTRITION_PROTEIN}}", p["nutrition_protein"])
    html = html.replace("{{NUTRITION_FAT}}", p["nutrition_fat"])
    html = html.replace("{{NUTRITION_CALORIES}}", p["nutrition_calories"])
    html = html.replace("{{NUTRITION_EXTRA_LABEL}}", p["nutrition_extra_label"])
    html = html.replace("{{NUTRITION_EXTRA_VAL}}", p["nutrition_extra_val"])
    html = html.replace("{{SPECIALITY}}", p["speciality"])
    html = html.replace("{{FAMOUS_FOR}}", p["famous_for"])
    html = html.replace("{{ALLERGY}}", p["allergy"])
    html = html.replace("{{HOW_TO_COOK}}", p["how_to_cook"])
    html = html.replace("{{VIDEO1_URL}}", p["video1"])
    html = html.replace("{{VIDEO2_URL}}", p["video2"])
    html = html.replace("{{INSTRUCTIONS}}", p["instructions"])
    
    # Active tab state in sidebar
    html = html.replace("{{FISH_ACTIVE}}", "active" if p["category"] == "Fish" else "")
    html = html.replace("{{MEAT_ACTIVE}}", "active" if p["category"] == "Meat" else "")
    html = html.replace("{{CHICKEN_ACTIVE}}", "active" if p["category"] == "Chicken" else "")
    html = html.replace("{{EGGS_ACTIVE}}", "active" if p["category"] == "Eggs" else "")

    file_name = f"d:\\fishcart2\\details_{id}.html"
    with open(file_name, "w", encoding="utf-8") as out:
        out.write(html)
        print(f"Generated {file_name}")

print("All details pages generated successfully.")
