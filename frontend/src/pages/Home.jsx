import { useEffect, useState } from 'react'
import { client } from '../lib/sanity'
import ProductCard from '../components/ProductCard'

export default function Home() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    client.fetch('*[_type == "product"]').then(data => {
      setProducts(data)
    })
  }, [])

  return (
    <div className="main-wrapper">
      <div className="fish-page">
        <div className="fp-banner">
          <div className="fp-bread">Home &nbsp;&rsaquo;&nbsp; All Products</div>
          <div className="fp-title">Fresh Catch & Premium Meat</div>
          <div className="fp-desc">Directly from the source to your kitchen.</div>
        </div>
        <div className="fp-grid">
          {products.map(p => (
            <ProductCard key={p._id} product={p} />
          ))}
        </div>
      </div>
    </div>
  )
}
