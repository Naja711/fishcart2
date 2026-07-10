import { Link } from 'react-router-dom'
import { urlFor } from '../lib/sanity'

export default function ProductCard({ product }) {
  return (
    <div className="fp-card">
      {product.image && (
        <img 
          className="fp-cimg" 
          src={urlFor(product.image).width(300).url()} 
          alt={product.title} 
        />
      )}
      <div className="fp-ct">{product.title}</div>
      <div className="fp-csub">{product.subtitle}</div>
      <div>
        <span className="fp-ctag">{product.speciality}</span>
      </div>
      <div className="fp-cbot">
        <div>
          <span className="fp-cprice">{product.price}</span>
          <span className="fp-cunit"> {product.unit}</span>
          <Link to={`/product/${product.id}`} style={{ textDecoration: 'none' }}>
            <div className="fp-clink">View Details →</div>
          </Link>
        </div>
      </div>
    </div>
  )
}
