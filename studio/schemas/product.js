export default {
  name: 'product', title: 'Product', type: 'document',
  fields: [
    { name: 'id', title: 'ID', type: 'string' },
    { name: 'title', title: 'Title', type: 'string' },
    { name: 'subtitle', title: 'Subtitle', type: 'string' },
    { name: 'price', title: 'Price', type: 'string' },
    { name: 'unit', title: 'Unit', type: 'string' },
    { name: 'image', title: 'Image', type: 'image', options: { hotspot: true } },
    { name: 'category', title: 'Category', type: 'reference', to: [{type: 'category'}] },
    { name: 'origin_label', title: 'Origin Label', type: 'string' },
    { name: 'origin', title: 'Origin', type: 'string' },
    { name: 'best_for', title: 'Best For', type: 'string' },
    { name: 'nutrition_protein', title: 'Protein', type: 'string' },
    { name: 'nutrition_fat', title: 'Fat', type: 'string' },
    { name: 'nutrition_calories', title: 'Calories', type: 'string' },
    { name: 'nutrition_extra_label', title: 'Nutrition Extra Label', type: 'string' },
    { name: 'nutrition_extra_val', title: 'Nutrition Extra Value', type: 'string' },
    { name: 'speciality', title: 'Speciality', type: 'string' },
    { name: 'famous_for', title: 'Famous For', type: 'string' },
    { name: 'allergy', title: 'Allergy Info', type: 'string' },
    { name: 'how_to_cook', title: 'How to Cook', type: 'string' },
    { name: 'video1', title: 'Video 1 URL', type: 'url' },
    { name: 'video2', title: 'Video 2 URL', type: 'url' },
    { name: 'instructions', title: 'Instructions (HTML)', type: 'text' }
  ]
}