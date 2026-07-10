export default function Topnav() {
  return (
    <div className="topnav">
      <div className="tn-left">
        <div className="search-bar">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" placeholder="Search for fresh fish, meat, eggs..." />
        </div>
      </div>
      <div className="tn-right">
        <div className="cart-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
          <span className="cart-badge">3</span>
        </div>
        <img className="profile-img" src="https://i.pravatar.cc/100?img=11" alt="Profile" />
      </div>
    </div>
  )
}
