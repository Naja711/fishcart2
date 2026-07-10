export default {
  name: 'homepage', title: 'Homepage Settings', type: 'document',
  fields: [
    { name: 'heroTitle', title: 'Hero Title', type: 'string' },
    { name: 'heroSubtitle', title: 'Hero Subtitle', type: 'string' },
    { name: 'featuredCategories', title: 'Featured Categories', type: 'array', of: [{type: 'reference', to: [{type: 'category'}]}] }
  ]
}