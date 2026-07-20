import { useParams, Link } from 'react-router-dom'

const categoryLabels = {
  fish: 'Fish',
  meat: 'Meat',
  chicken: 'Chicken',
  eggs: 'Eggs',
}

export default function CategoryPage() {
  const { slug } = useParams()
  const label = categoryLabels[slug] || 'Category'

  return (
    <div className="main-wrapper">
      <div className="home" style={{ padding: '24px' }}>
        <div style={{ background: '#fff', borderRadius: '14px', padding: '24px', boxShadow: '0 10px 30px rgba(0,0,0,0.05)' }}>
          <h1 style={{ margin: 0, fontSize: '2rem', color: '#0A2848' }}>{label}</h1>
          <p style={{ color: '#4B5563', margin: '12px 0 20px' }}>
            Browse fresh {label.toLowerCase()} selections curated for you.
          </p>
          <Link to="/" style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: '#1565C0', color: '#fff', padding: '10px 16px', borderRadius: '10px', textDecoration: 'none' }}>
            ← Back to Home
          </Link>
        </div>
      </div>
    </div>
  )
}
