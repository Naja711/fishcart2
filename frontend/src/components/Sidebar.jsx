import { Link } from 'react-router-dom'

export default function Sidebar() {
  return (
    <div className="sidebar">
      <div className="logo-area">
        <div className="logo-row">
          <div className="logo-chev">&lt;&lt;</div>
          <div className="logo-name">FishCart</div>
        </div>
        <div className="logo-tag">Daily Fresh Partner</div>
      </div>

      <div className="nav">
        <Link to="/" className="ni active">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          Home
        </Link>
        <Link to="/category/fish" className="ni">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M4 10s4-4 8-4 8 4 8 4-4 4-8 4-8-4-8-4zm0 0v4m16-4v4" /></svg>
          Fish
        </Link>
        <Link to="/category/meat" className="ni">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M6 13V4a2 2 0 012-2h8a2 2 0 012 2v9m-4-6h.01M9 7h.01M6 21v-3m12 3v-3M4 10h16M5 14h14a2 2 0 012 2v3a2 2 0 01-2 2H5a2 2 0 01-2-2v-3a2 2 0 012-2z"></path></svg>
          Meat
        </Link>
        <Link to="/category/chicken" className="ni">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M8 8c0-2 1.5-4 4-4s4 2 4 4-1.5 4-4 4-4-2-4-4z" /><path d="M4 20a8 8 0 0116 0H4z" /></svg>
          Chicken
        </Link>
        <Link to="/category/eggs" className="ni">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><ellipse cx="12" cy="12" rx="8" ry="10" /></svg>
          Eggs
        </Link>
        <div className="ni">How to Cook</div>
        <div className="ni">Benefits</div>
        <div className="ni">Our Stories</div>
        <div className="ni">About Us</div>
        <div className="ni">Contact Us</div>
      </div>

      <div className="sidebar-cta">
        <h4>Join Our Community</h4>
        <p>Be a part of our journey for healthy and delicious living.</p>
        <button className="btn-join">Join Us</button>
      </div>
    </div>
  )
}
