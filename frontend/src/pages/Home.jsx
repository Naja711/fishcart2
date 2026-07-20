import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="main-wrapper">
      <div className="home">
        <div className="r1">
          <div className="hero">
            <div className="h1">Fresh Fish. <br />Healthy Life.</div>
            <div className="hp">Handpicked daily for freshness you can trust.</div>
            <button className="btn-join">
              Join Us <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14m-7-7l7 7-7 7" /></svg>
            </button>

            <div className="hero-badges">
              <div className="hb">
                <span className="hbc">✓</span>
                <span className="hbl">100% Fresh<br />Never Frozen</span>
              </div>
              <div className="hb">
                <span className="hbc">✓</span>
                <span className="hbl">Hygienic<br />&amp; Safe</span>
              </div>
              <div className="hb">
                <span className="hbc">✓</span>
                <span className="hbl">Daily<br />Delivery</span>
              </div>
              <div className="hb">
                <span className="hbc">✓</span>
                <span className="hbl">Best<br />Quality</span>
              </div>
            </div>

            <img
              className="hero-img"
              src="/assets/fresh_fish_on_ice_1783634420753.png"
              alt="Fresh salmon"
            />
          </div>

          <div className="cat-grid">
            <Link to="/category/fish" className="cat fish">
              <div className="cat-inf">
                <div>
                  <div className="cat-name">Fish</div>
                  <div className="cat-cnt">100+ Items</div>
                </div>
                <div className="cat-arr">→</div>
              </div>
              <img className="cimg" src="/assets/cat_fish.png" alt="Fish" />
            </Link>

            <Link to="/category/meat" className="cat meat">
              <div className="cat-inf">
                <div>
                  <div className="cat-name">Meat</div>
                  <div className="cat-cnt">50+ Items</div>
                </div>
                <div className="cat-arr">→</div>
              </div>
              <img className="cimg" src="/assets/cat_meat.png" alt="Meat" />
            </Link>

            <Link to="/category/chicken" className="cat chicken">
              <div className="cat-inf">
                <div>
                  <div className="cat-name">Chicken</div>
                  <div className="cat-cnt">30+ Items</div>
                </div>
                <div className="cat-arr">→</div>
              </div>
              <img className="cimg" src="/assets/cat_chicken.png" alt="Chicken" />
            </Link>

            <Link to="/category/eggs" className="cat eggs">
              <div className="cat-inf">
                <div>
                  <div className="cat-name">Eggs</div>
                  <div className="cat-cnt">Farm Fresh</div>
                </div>
                <div className="cat-arr">→</div>
              </div>
              <img className="cimg" src="/assets/cat_eggs.png" alt="Eggs" />
            </Link>
          </div>
        </div>

        <div className="r2">
          <div className="cook">
            <div className="ct">How to Make Delicious</div>
            <div className="cs">Step by step cooking videos for every taste</div>
            <div className="rrow">
              <div className="rec">
                <div className="rthumb">
                  <img src="/assets/fish_showcase.png" alt="Fish Curry" />
                  <div className="play">
                    <div className="playbtn">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="m10 8 6 4-6 4" /></svg>
                    </div>
                  </div>
                </div>
                <div className="rlbl">Fish Curry</div>
                <div className="rslbl">Spicy &amp; Tangy</div>
              </div>
              <div className="rec">
                <div className="rthumb">
                  <img src="/assets/header_fish3_nobg.png" alt="Grilled Fish" />
                  <div className="play">
                    <div className="playbtn">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="m10 8 6 4-6 4" /></svg>
                    </div>
                  </div>
                </div>
                <div className="rlbl">Grilled Fish</div>
                <div className="rslbl">Healthy &amp; Tasty</div>
              </div>
              <div className="rec">
                <div className="rthumb">
                  <img src="/assets/header_fish2_nobg.png" alt="Fish Fry" />
                  <div className="play">
                    <div className="playbtn">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="m10 8 6 4-6 4" /></svg>
                    </div>
                  </div>
                </div>
                <div className="rlbl">Fish Fry</div>
                <div className="rslbl">Crispy &amp; Juicy</div>
              </div>
            </div>
            <button className="btn-view">View All Recipes →</button>
          </div>

          <div className="r2-right">
            <div className="bene">
              <div className="ct">Benefits &amp; Nutrition</div>
              <div className="bene-desc">
                Fish, meat, eggs and chicken are rich in protein, vitamins and minerals for a stronger, healthier you.
              </div>
              <button className="lnk">Learn More →</button>
              <div className="bene-inner">
                <div className="bene-left">
                  <div className="bic">
                    <div className="bicc">✓</div>
                    <div>High in Protein</div>
                  </div>
                  <div className="bic">
                    <div className="bicc">✓</div>
                    <div>Rich in Vitamins</div>
                  </div>
                  <div className="bic">
                    <div className="bicc">✓</div>
                    <div>Good for Heart</div>
                  </div>
                </div>
                <img className="bene-img" src="/assets/prod_1_salmon.jpg" alt="Salmon Benefits" />
              </div>
            </div>

            <div className="rev">
              <div className="rev-title">What Our Customers Say</div>
              <div className="stars">★★★★★</div>
              <div className="qm">“</div>
              <div className="rev-text">
                Super fresh products and great variety. Fishcart is our family’s choice.
              </div>
              <div className="rev-name">– Priya S.</div>
              <div className="rdots">
                <span className="rd"></span>
                <span className="rd off"></span>
                <span className="rd off"></span>
              </div>
            </div>
          </div>
        </div>

        <div className="r3">
          <Link to="/category/fish" className="prod">
            <img src="/assets/fish_showcase.png" alt="All Fish Items" />
            <div className="prod-ov">
              <div className="pn">All Fish Items</div>
              <div className="pe">Explore Now</div>
            </div>
          </Link>
          <Link to="/category/meat" className="prod">
            <img src="/assets/meat_showcase.png" alt="All Meat Items" />
            <div className="prod-ov">
              <div className="pn">All Meat Items</div>
              <div className="pe">Explore Now</div>
            </div>
          </Link>
          <Link to="/category/chicken" className="prod">
            <img src="/assets/chicken_showcase.png" alt="Chicken Items" />
            <div className="prod-ov">
              <div className="pn">Chicken Items</div>
              <div className="pe">Explore Now</div>
            </div>
          </Link>
          <Link to="/category/eggs" className="prod">
            <img src="/assets/eggs_showcase.png" alt="Eggs" />
            <div className="prod-ov">
              <div className="pn">Eggs</div>
              <div className="pe">Explore Now</div>
            </div>
          </Link>
        </div>

        <div className="r4">
          <div className="feat fb">
            <div className="ftop">
              <div className="ftitle">Freshness You Can Trust</div>
              <div className="ficon fw">✓</div>
            </div>
            <div className="fdesc">We ensure premium quality and freshness in every product we deliver.</div>
          </div>
          <div className="feat flb">
            <div className="ftop">
              <div className="ftitle">Daily Selection</div>
              <div className="ficon fbl">✓</div>
            </div>
            <div className="fdesc">Handpicked daily from trusted suppliers for the best quality.</div>
          </div>
          <div className="feat ft">
            <div className="ftop">
              <div className="ftitle">Hygienic &amp; Safe</div>
              <div className="ficon ftl">✓</div>
            </div>
            <div className="fdesc">Cleaned, packed and delivered with highest hygiene standards.</div>
          </div>
          <div className="feat fg">
            <div className="ftop">
              <div className="ftitle">Sourced Responsibly</div>
              <div className="ficon fgl">✓</div>
            </div>
            <div className="fdesc">We care for the ocean and the environment for a better future.</div>
          </div>
          <div className="feat fl">
            <div className="ftop">
              <div className="ftitle">Join Our Community</div>
              <img className="qr" src="/assets/ice_cubes_bg.png" alt="QR code" />
            </div>
            <div className="fdesc">Be a part of our journey for healthy and delicious living.</div>
          </div>
        </div>

        <div className="r5">
          <div className="fcol">
            <div className="fct">About Us</div>
            <div className="fctxt">We are passionate about delivering fresh and healthy food to your family.</div>
          </div>
          <div className="fcol">
            <div className="fct">Our Stories</div>
            <div className="fctxt">From ocean to your kitchen, our journey of freshness.</div>
          </div>
          <div className="fcol">
            <div className="fct">Contact Us</div>
            <div className="fctxt">We are here to help you. Reach out anytime.</div>
          </div>
          <div className="fcol">
            <div className="fct">Location</div>
            <div className="fdi">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 21s-7-4.35-7-10a7 7 0 0 1 14 0c0 5.65-7 10-7 10z" /><circle cx="12" cy="11" r="2" /></svg>
              <span>Unit 5 Hythe Quay, Colchester, England, CO2 8JB</span>
            </div>
            <div className="fdi">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 16.92V19a2 2 0 0 1-2.18 2A19.79 19.79 0 0 1 3 5.18 2 2 0 0 1 5 3h2.09a2 2 0 0 1 2 1.72c.12 1.2.35 2.37.69 3.5a2 2 0 0 1-.45 2.11L8.09 11.91a16 16 0 0 0 6.36 6.36l1.58-1.14a2 2 0 0 1 2.11-.45c1.13.34 2.3.57 3.5.69A2 2 0 0 1 22 16.92z" /></svg>
              <span>+44 1206 123456</span>
            </div>
            <div className="fdi">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M4 4h16v16H4z" /><path d="M4 8h16" /><path d="M8 20V8" /></svg>
              <span>hello@fishcart.co.uk</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
