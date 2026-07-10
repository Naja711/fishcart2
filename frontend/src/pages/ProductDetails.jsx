import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { client, urlFor } from '../lib/sanity'

export default function ProductDetails() {
  const { id } = useParams()
  const [product, setProduct] = useState(null)

  useEffect(() => {
    client.fetch(`*[_type == "product" && id == "${id}"][0]`).then(data => {
      setProduct(data)
    })
  }, [id])

  if (!product) return <div className="main-wrapper">Loading...</div>

  return (
    <div className="main-wrapper">
      <div className="top-section-row">
        <div className="product-image-col">
          <div className="hero-image-container">
            {product.image && <img src={urlFor(product.image).url()} alt={product.title} />}
          </div>
        </div>
        <div className="product-info-col">
          <h1 className="prod-title">{product.title}</h1>
          <div className="prod-desc">{product.subtitle}</div>
          <div className="purchase-price">
            {product.price} <span>{product.unit}</span>
          </div>
        </div>
      </div>
    </div>
  )
}
